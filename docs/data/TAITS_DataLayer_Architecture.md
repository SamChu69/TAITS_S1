# TAITS DataLayer Architecture (S2)

## 0. 文件定位與範圍

本文件定義 TAITS S2（Research）階段的 **Data Layer 端到端架構**，並以「可治理、可稽核、可重現」為首要目標。

- S2 僅允許 `RESEARCH`（不得接券商、不得下單）
- Risk/Compliance 具有最高否決權
- 資料來源決策必須遵守：
  - `TAITS_DataSource_Priority_and_Fallback.md`
- Schema 與資料包必須遵守：
  - `TAITS_DataBundle_and_Schema.md`
- 資料品質規則必須遵守：
  - `TAITS_Data_Validation_Rules.md`

---

## 1. 設計原則（不可違反）

1) **單一責任（SRP）**：每一層只做自己的事  
2) **可替換（Pluggable）**：新增資料源不影響下游  
3) **可重現（Reproducible）**：同參數可回放相同資料（cache+hash）  
4) **可追溯（Auditable）**：每次決策、取數、驗證、落盤都有證據鏈  
5) **不允許靜默切換（No Silent Switch）**：Fallback 必須可見、可查  
6) **治理先於便利**：研究模式也要遵守官方優先與品質規範  
7) **策略與 Agent 不得決定資料來源**：只可消費 DataBundle

---

## 2. Data Layer 模組清單與責任邊界

### 2.1 模組總覽

| 模組 | 角色 | 輸入 | 輸出 | 禁止事項 |
|---|---|---|---|---|
| DataPolicyEngine | 來源選擇決策 | dataset, symbol, freq, time_range, context | primary+fallback 序列、切換條件 | 直接抓資料 |
| Connector | 取數 | policy 決策、請求參數 | RawPayload + Meta | 變更 schema、改欄位語意 |
| Normalizer | 統一化 | RawPayload | NormalizedFrame（符合 schema） | 內插「假資料」掩蓋缺漏 |
| Validator | 品質檢核 | NormalizedFrame | ValidationReport（OK/WARN/BLOCK） | 自動降級 BLOCK |
| CacheManager | 快取/落盤 | NormalizedFrame + Meta | cache_path + content_hash | 靜默覆寫、不留 hash |
| AuditTrail | 稽核記錄 | 全流程事件 | AuditRecords | 不記錄 fallback 原因 |
| DataBundleBuilder | 資料包裝 | frames + reports + audit | DataBundle | 直接做策略/信號 |

### 2.2 模組責任細節

#### A) DataPolicyEngine（資料來源決策）
- 依據「官方優先 + 明確 fallback」輸出一個 **Source Plan**：
  - `primary_source`
  - `fallback_sources[]`
  - `fallback_conditions[]`（如 OFFICIAL_UNAVAILABLE / VALIDATION_BLOCK / LATENCY）
- 必須產生可被 audit 的決策輸出（包含 reason_code）

> Orchestrator 不得自行選來源；只能呼叫 DataPolicyEngine。

#### B) Connector（資料來源連接器）
- 每個來源獨立一個 connector（TWSEConnector/FinMindConnector/YahooConnector…）
- 專注「取數」與「回傳原始 payload」
- 必須回傳 `meta`（request_ts/response_ts/status_code/params/latency）

#### C) Normalizer（一致化器）
- 將 RawPayload 轉為 TAITS Schema（OHLCV bar schema 為 S2 必備）
- 必須填入：
  - `source`
  - `freq`
  - `schema_version`
  - `symbol`（TAITS 內部代碼）

#### D) Validator（品質檢核器）
- 根據 `TAITS_Data_Validation_Rules.md` 產生 ValidationReport
- `BLOCK`：
  - 中止該 symbol 的該 dataset 使用
  - 或進入 fallback 重試（由流程控制層負責）

#### E) CacheManager（快取/落盤）
- 核心不是快，是 **可重現**
- 必須提供：
  - `cache_path`（落盤位置）
  - `content_hash`（sha256 建議）
  - `rows`、`schema_version`
- 不得靜默覆寫而不更新 hash / 不留紀錄

#### F) AuditTrail（稽核）
- 對每個流程步驟留痕：
  - policy 決策（source plan）
  - connector request/response
  - normalize 完成（rows、schema_version）
  - validate 結果（OK/WARN/BLOCK，命中規則）
  - cache 落盤（path、hash）
  - fallback 切換（reason_code、validator evidence）

#### G) DataBundleBuilder（資料包建構器）
- 統一輸出 `DataBundle`（見 DataBundle 文件）
- 必須包含：
  - datasets.frames（NormalizedFrame）
  - validation.reports
  - audit.records
- 不得包含策略訊號、下單意圖

---

## 3. 端到端資料流（Data Flow）

### 3.1 S2 Research 端到端流程（單 dataset 單 symbol）

1) **Policy**：DataPolicyEngine 產生 Source Plan  
2) **Fetch**：Connector 依 primary 取數  
3) **Normalize**：Normalizer 轉成 NormalizedFrame  
4) **Validate**：Validator 產生 ValidationReport  
5) **Cache**：CacheManager 落盤與 hash  
6) **Audit**：全流程事件寫入 AuditTrail  
7) **Bundle**：DataBundleBuilder 組裝 DataBundle

### 3.2 ASCII 流程圖（可貼到設計審查）
```

[Orchestrator: Research]
|
v
[DataPolicyEngine] ---> (Source Plan) ---> [AuditTrail: policy_decision]
|
v
[Connector] --------> (RawPayload+Meta) ---> [AuditTrail: fetch]
|
v
[Normalizer] --------> (NormalizedFrame) ---> [AuditTrail: normalize]
|
v
[Validator] ---------> (ValidationReport) ---> [AuditTrail: validate]
|
v
[CacheManager] -------> (cache_path+hash) ---> [AuditTrail: cache]
|
v
[DataBundleBuilder] ----> (DataBundle w/ datasets+validation+audit)

```

---

## 4. Fallback 流程（不可靜默）

### 4.1 Fallback 觸發條件（僅能來自 policy 規則）
- OFFICIAL_UNAVAILABLE（官方不可用）
- VALIDATION_BLOCK（Validator = BLOCK）
- LATENCY（研究態可用；S3 交易前/交易中禁止使用此理由）

### 4.2 Fallback 行為準則
- 不允許無限重試：每個 symbol/dataset 有最大嘗試次數
- 任一次切換必須記錄：
  - `primary_source`
  - `fallback_source`
  - `reason_code`
  - `validator_status`（若因 BLOCK）
  - `decision_ts`

### 4.3 Fallback 流程圖
```

primary_source -> fetch -> normalize -> validate
|        |
|        +-- BLOCK? -- yes --> fallback_source_1
|                          -> fetch -> normalize -> validate
|
+-- connection fail? --> fallback_source_1

```

---

## 5. 與 Orchestrator 的介面契約（S2）

### 5.1 Orchestrator 在 Research 模式新增 Data Phase
Orchestrator 的責任：
- 呼叫 DataLayer 的「單一入口」取得 DataBundle
- 讀取 validation.status 決定是否繼續進 Analysis Phase
- 將 BLOCK 狀態以 log + audit 明確呈現
- 不得直接操控資料源、不得直接落盤

### 5.2 建議的 DataLayer 對外入口（概念）
- `DataLayerService.get_bundle(universe, datasets, asof_ts, context) -> DataBundle`

> 註：此為 S2 架構規格，S2.0 實作可先支援 `bars` 單一 dataset。

---

## 6. 與 Risk/Compliance 的關係

- 資料品質（Validator）≠ 風控（RiskEngine），但兩者皆可否決
- RiskEngine 可基於：
  - 資料延遲
  - 資料來源不合規
  - audit 缺失
  - 任何合規條件
  直接 BLOCK（高於 Validator）

S2 建議規則：
- 若 DataBundle.audit.records 缺失關鍵欄位（source/params/hash）→ RiskEngine 可 BLOCK

---

## 7. 資料落盤與可重現性（Cache Strategy）

### 7.1 Cache Key 建議
- key = `(source, dataset, symbol, freq, start, end, schema_version)`

### 7.2 Cache Path 建議
- `data/cache/{dataset}/{source}/{symbol}/{freq}/{start}_{end}.parquet`

### 7.3 Hash 建議
- `sha256`（以內容序列化後計算）
- Audit 必須記錄 `content_hash`，供回放比對

---

## 8. 可觀測性（Observability）最低要求

S2 Research 跑完必須可回答：
1) 本次每個 dataset 使用了哪個來源？為何？
2) 是否發生 fallback？原因是什麼？
3) Validator 命中哪些規則？嚴重程度？
4) 落盤在哪裡？hash 是什麼？
5) 同參數重跑是否可回放相同資料？

---

## 9. S2.0 最小落地範圍（落實順序）

### S2.0（最小可用）
- dataset：`bars`
- freq：`1d`
- universe：固定單一 symbol（例如 `TW:2330`）
- source：先做 1 個 primary（如 FinMind）+ policy 架構預留官方優先

### S2.1（擴展）
- universe：10 檔
- 加入 rate-limit / retry
- cache 命中率與落盤策略

### S2.2（再擴展）
- freq：加入 `1m/5m`
- 交易時段與 bar 對齊規則強化

---

## 10. 驗收標準（Acceptance）

執行 `python main.py research` 時，必須達成：

- Data Phase 產生 DataBundle
- DataBundle 至少包含：
  - datasets.bars.frames（至少 1 檔）
  - validation.reports（至少 1 份）
  - audit.records（至少 1 條，含 source/params/hash）
- 若官方不可用或 validator BLOCK，必須：
  - 觸發 fallback（若 policy 允許）
  - 產生可查的 fallback audit
- 全流程不得觸發任何下單或券商連線

---

## 11. 版本紀錄
- 1.0.0：建立 TAITS S2 DataLayer 模組邊界、資料流、Fallback、Audit、Cache 與 Orchestrator 契約。
```

---
