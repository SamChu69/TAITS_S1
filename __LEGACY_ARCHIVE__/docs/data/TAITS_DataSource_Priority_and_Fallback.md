# TAITS DataSource Priority and Fallback Policy

## 0. 文件定位與權威性

本文件定義 TAITS 對「資料來源選擇」的**最高決策規範**。

適用範圍：
- S2：Research（僅研究，不下單）
- 後續 S3/S4 亦需遵循，除非有更高版本明確覆寫

優先權聲明：
- 本文件高於 Strategy / Agent / AI 的任何建議
- 若與任何模組邏輯衝突，以本文件為準
- Risk / Compliance 仍保有最高否決權

---

## 1. 核心原則（不可違反）

### 1.1 官方資料優先（Official First）
只要官方資料「可用且品質合格」，**不得**使用第三方或聚合來源。

### 1.2 多層 Fallback（Explicit Fallback）
Fallback 必須：
- 有明確條件
- 可被記錄（Audit）
- 可被重現（Reproducibility）

### 1.3 不允許靜默切換（No Silent Switch）
任何資料來源切換：
- 必須產生 AuditRecord
- 必須能在 log / report 中被看見

### 1.4 Research 不等於隨便
即使是研究階段：
- 來源選擇仍需可解釋
- 不可因「方便」而跳過官方

---

## 2. 資料來源分級（Source Tiering）

TAITS 將資料來源分為四級：

| Tier | 類型 | 說明 |
|---|---|---|
| T0 | 官方交易所 | 最優先、最權威 |
| T1 | 官方衍生單位 | 交易所附屬或官方指定 |
| T2 | 第三方結構化資料 | 聚合、清洗後資料 |
| T3 | 公開抓取/試驗來源 | 僅限研究備援 |

---

## 3. 台灣市場（TW）資料來源優先表

### 3.1 股票（TWSE / TPEX）OHLCV

#### 優先順序
1. **TWSE / TPEX 官方**
   - Tier：T0
   - 說明：交易所公告或 API（若有）
2. **MOPS（補充性，不含即時行情）**
   - Tier：T1
   - 說明：財務與事件為主，非主要 K 線來源
3. **FinMind**
   - Tier：T2
   - 說明：結構化、穩定、研究友善
4. **Yahoo Finance**
   - Tier：T3
   - 說明：僅限備援與對照

#### 使用規則
- 若 TWSE/TPEX 官方可用且 validator = OK/WARN → **禁止使用其他來源**
- FinMind 僅能在官方不可用或資料缺口時啟用
- Yahoo 僅能作為：
  - 對照驗證
  - 官方與 T2 同時失效時的臨時研究用途

---

### 3.2 期貨 / 選擇權（TAIFEX）

#### 優先順序
1. **TAIFEX 官方**
   - Tier：T0
2. **官方公告檔（CSV/ZIP）**
   - Tier：T1
3. **第三方整理資料（若有）**
   - Tier：T2
4. **公開網站抓取**
   - Tier：T3（不建議）

#### 特別規則
- 合約規格（乘數、到期日）一律以官方為準
- 若第三方資料與官方衝突，**以官方否決第三方**

---

## 4. 資料類型 × 來源對照表（S2 最小集）

| Dataset | 首選 | Fallback | 禁止 |
|---|---|---|---|
| bars (OHLCV) | TWSE/TPEX | FinMind → Yahoo | 未標示來源 |
| volume | 官方 | FinMind | 推算值 |
| fundamentals | MOPS | 官方公告 | 非官方轉載 |
| corporate_actions | 官方公告 | FinMind | 推測資料 |

---

## 5. Fallback 啟動條件（明確化）

Fallback **只能**在以下情況啟動（需滿足至少一項）：

### 5.1 官方不可用
- API 無回應
- 官方未提供該頻率/期間

### 5.2 Validator 判定 BLOCK
- 缺值率超過門檻
- 時間序列斷裂
- 價格為 0 或負值

### 5.3 時效性不足（僅限 Research）
- 官方資料延遲
- 研究需要即時近端數據做假設測試

> 註：時效性理由 **不得**用於 S3/S4（交易前/交易中）

---

## 6. Fallback 稽核要求（Audit 必備）

每次啟用 Fallback，AuditRecord **必須包含**：

| 欄位 | 說明 |
|---|---|
| primary_source | 原本應使用的來源 |
| fallback_source | 實際使用來源 |
| reason_code | OFFICIAL_UNAVAILABLE / VALIDATION_BLOCK / LATENCY |
| validator_status | 官方 validator 結果 |
| decision_ts | 決策時間 |
| approved_by | 系統模組（如 DataPolicyEngine） |

---

## 7. 禁止行為（Hard Rules）

以下行為一律視為系統錯誤（Error）：

- Agent 自行指定資料來源
- Strategy 內硬編碼資料來源
- AI 推薦直接覆寫官方來源
- 無 Audit 的資料切換
- 使用來源但 `source` 欄位為空或模糊

---

## 8. 與 Orchestrator 的關係

- Orchestrator **不得**直接決定資料來源
- 必須呼叫 DataPolicy / DataSourceSelector
- Orchestrator 僅負責：
  - 接收決策結果
  - 傳遞給 Connector / Loader
  - 紀錄 audit

---

## 9. S2 驗收標準（Acceptance）

在 S2 Research 模式下，系統必須能：

1. 明確指出「本次使用哪個來源」
2. 若非官方，能清楚說明「為何 fallback」
3. 在 DataBundle.audit 中完整呈現決策紀錄
4. 同一研究條件下可重現相同來源選擇結果

---

## 10. 版本紀錄

- 1.0.0：建立 TAITS 資料來源分級、官方優先與 Fallback 決策規範（S2 專用）。
