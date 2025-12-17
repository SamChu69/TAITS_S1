# 📘 TAITS_DataFlow_and_EventFlow.md
## TAITS 資料流與事件流（Phase S2）

---

## 0. 文件定位（S2 核心約束）

本文件定義 TAITS 的「單向資料流」與「事件驅動決策模型」：

- DataFlow：資料如何從外部進入、被標準化、被解讀、被治理、最終進入決策
- EventFlow：哪些事件會觸發資料更新、Evidence 更新、Gate 更新與 Decision 產生

> 本文件受 S0 / S1 約束，並必須與《TAITS_System_Architecture_Blueprint.md》一致。

---

## 1. 核心原則（Hard Rules）

### R1｜資料單向流（No Backflow）
合法流向只允許：

```

Source → Ingestion → Normalize → Store/Cache → Compute → Evidence → Governance → Decision → Execution

```

嚴格禁止：
- Strategy / Agent 反向要求 Source 改變資料
- Execution 反向改 Decision
- Evaluation（S5）即時干預 S3 / S4

---

### R2｜事件驅動（Event-Driven, Not “Always-On”）
TAITS 不假設高頻、不中斷監控。  
所有更新與決策必須由明確事件觸發，且可被審計回放。

---

### R3｜缺資料保守（Conservative on Missing Data）
- Gate 層缺資料：偏向 WAIT / NO_TRADE
- Tier-4（不確定性）缺資料：視為存在（踩煞車）
- Evidence 缺資料：不加分、不否決（除非屬 Gate 必要資料）

---

## 2. DataFlow（資料流）總覽

### 2.1 DataFlow Pipeline（分段定義）

**Stage D0｜Source（資料來源）**
- TWSE（行情、成交量等）
- TAIFEX（期貨/選擇權、OI 等）
- MOPS（財報、重大訊息）
- Calendar（結算/假期/事件）
- Internal Config（模式、風控、Lane 啟用）

**Stage D1｜Ingestion（擷取）**
- Adapter 只負責取回資料，不做判斷
- 需標註：來源、時間戳、完整性

**Stage D2｜Normalize（標準化）**
- 統一欄位命名、時區、頻率、單位
- 產出 Canonical Schema（標準欄位集合）
- 做基本檢核：缺漏、重複、時間對齊

**Stage D3｜Store/Cache（存儲與快取）**
- 目的：可回放、可審計、可重算
- 需區分：
  - Raw Store（原始）
  - Canonical Store（標準化後）
  - Snapshot Store（決策當下快照）

**Stage D4｜Compute（計算）**
- 計算指標（如 ATR/HV、趨勢判定、量價結構）
- 產出：Signals（訊號）/ Features（特徵）

**Stage D5｜Evidence（證據層）**
- Agent 將 Signals/Features 轉為 Evidence（Tier-1~4）
- Evidence 必須可解釋與可降權/禁用

**Stage D6｜Governance（治理）**
- Gate：Regime / MR / Compliance / Risk Budget
- Strategy Availability：哪些 Lane/策略可用
- 產出：允許清單 + 否決原因

**Stage D7｜Decision（決策）**
- 統一輸出：TRADE / WAIT / NO_TRADE
- 同步寫入 Audit Log + Snapshot

**Stage D8｜Execution（執行）**
- 依 Mode 執行（RESEARCH/PAPER/SHADOW/LIVE_RESTRICTED）
- 必須套用 Safety Locks
- 回寫 Execution Log（但不得改 Decision）

---

## 3. Data Contracts（資料契約）

### 3.1 Canonical Schema（概念性欄位集合）
（此處不綁定任何單一資料源命名，僅定義 TAITS 內部標準欄位概念）

- `ts`：時間戳（Asia/Taipei）
- `symbol`：標的代碼（股票/指數/期貨代碼）
- `ohlc`：open/high/low/close
- `volume`：成交量
- `value`：成交額（如可得）
- `oi`：未平倉（期貨/選擇權，如可得）
- `corp_actions`：除權息/分割（如可得）
- `event_flags`：事件旗標（結算/重大事件）
- `data_quality`：完整性/延遲/缺漏標記

### 3.2 Data Quality Flags（必要）
每筆資料必須帶至少一組品質旗標：

- `is_missing`：是否缺漏
- `is_delayed`：是否延遲（超過允許閾值）
- `is_stale`：是否過期（時間戳落後）
- `source_priority`：主來源/備援來源
- `confidence`：資料可信度（由規則產生，不是模型自信）

---

## 4. EventFlow（事件流）總覽

### 4.1 事件分類（Event Types）

- **E0 System Events（系統事件）**
  - 啟動/停止
  - 模式切換（RESEARCH/PAPER/SHADOW/LIVE）
  - 設定更新（風控、Lane 啟用）

- **E1 Market Data Events（行情事件）**
  - New Bar（新 K 棒產生：1m/5m/日等）
  - Price Spike（價格急變）
  - Volume Spike（量能急變）

- **E2 Calendar & Regime Events（日曆/狀態事件）**
  - Settlement Window（結算視窗進入/離開）
  - Holiday / Half Day（休市/半日）
  - Regime Change（狀態轉換）

- **E3 Fundamental / News Events（基本面/消息事件）**
  - MOPS Update（財報/公告更新）
  - Corporate Action（除權息等）

- **E4 Governance Events（治理事件）**
  - MR Level Change
  - Gate Pass/Fail Change
  - Risk Budget Update

- **E5 Decision Events（決策事件）**
  - Decision Request（請求產生決策）
  - Decision Finalized（決策已落地並寫入審計）

- **E6 Execution Events（執行事件）**
  - Order Simulated / Placed / Rejected
  - Safety Lock Triggered

---

### 4.2 事件來源（Who Can Emit Events）
合法事件發送者：

- Scheduler（排程器）
- Data Adapters（資料擷取層）
- Governance Engines（Regime/MR/Risk）
- Decision Core（僅能發送 Decision 類事件）
- Execution Interface（僅能發送 Execution 類事件）

嚴格禁止：
- Strategy 直接發送 Decision Request
- Model 直接發送 Execution 事件
- Evaluation（S5）直接插入即時事件流

---

## 5. 決策觸發規則（Decision Trigger Rules）

### 5.1 合法觸發點（Only These Can Trigger Decision）
TAITS 只允許以下情況觸發「Decision Request」：

1. **新 K 棒完成（New Bar Closed）**
2. **Regime 或 MR 發生變化（Change Event）**
3. **風險狀態更新（Risk Budget / System State）**
4. **人工要求（Manual Decision Request）**
   - 仍必須走完整 Checklist，不得跳步

### 5.2 禁止觸發點（Never Trigger Decision）
- 單一 Signal 觸發
- 模型預測值觸發
- Execution 失敗反向觸發「再試一次」
- 因錯過行情觸發

---

## 6. 排程與頻率（Scheduler & Frequencies）

### 6.1 建議頻率（符合 S0）
- 日級（Daily）：Regime / 基本面 / 大多數 Tier-1 結構檢查
- 5–60 分（Intraday）：僅用於 Tier-3 執行時機（需 Gate PASS）
- 事件驅動：結算/公告/重大事件

📌 原則：  
**頻率越高，治理越嚴格，越偏向 NO_TRADE**

---

## 7. Cache / Snapshot 規則（可審計）

### 7.1 Snapshot（決策快照）必存內容
每次 Decision Finalized 必須寫入：

- `decision`（TRADE/WAIT/NO_TRADE）
- `regime`、`MR_level`、`system_state`
- Evidence Summary（Tier-1~4 摘要）
- Strategy/Lane 可用性狀態
- Data Quality Summary（缺漏/延遲/來源）

### 7.2 重算一致性（Reproducibility）
- 回放同一快照，應可重現同一 Decision
- 若無法重現，視為資料治理或版本治理問題（需檢討）

---

## 8. 失效與降級（Degradation Rules）

### 8.1 資料擷取失敗
- 主來源失敗 → 切備援
- 備援也失敗 → 啟用缺資料保守規則

### 8.2 關鍵 Gate 資料缺失
- 無法判定 Regime/MR → Decision Bias 強制 WAIT/NO_TRADE

### 8.3 異常延遲（Stale/Delayed）
- 超過延遲閾值 → 標記 `is_stale = true`
- Decision Core 不得輸出 TRADE（除非明確允許且有人工確認）

---

## 9. 與 S0 / S1 對齊聲明

- 本文件避免「永遠即時」假設（符合 S0）
- 本文件禁止跨層觸發與反向依賴（符合 S1-4）
- 本文件缺資料偏保守（符合 S1-5）
- 本文件可審計可回放（符合 S1-2 / S1-3）

---

## 10. 定錨語（不可刪）

> **資料先被治理，  
> 決策才有資格成立；  
> 決策先可回放，  
> 執行才有資格發生。**

---

## 11. 文件狀態

- ✔ Phase S2（資料流與事件流權威）
- ✔ 與架構藍圖一致
- ✔ 不假設高頻、不假設全天盯盤
- ✔ 支援可審計、可回放、可演進
```

---
