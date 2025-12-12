# TAITS Data Validation Rules

## 0. 文件定位與權威性

本文件定義 TAITS 在 S2（Research）階段的 **資料品質驗證（Validation）硬規則**。

權威性聲明：
- 本文件高於 Strategy / Agent / AI 的任何資料使用偏好
- Validator 的 `BLOCK` 結論可直接中止 DataBundle
- Risk / Compliance 仍保有最高否決權（可覆寫任何 OK/WARN）

適用模式：
- S2：RESEARCH（僅研究，不下單）
- 後續 S3/S4 可擴充規則，但不得弱化既有規則

---

## 1. 驗證目標（Why Validation）

Validator 的目的不是「把資料修到能用」，而是：

1) **揭露風險**（而非掩蓋）
2) **阻止垃圾資料污染系統**
3) **為 Fallback 與 Audit 提供客觀依據**
4) **確保研究結果可重現、可解釋**

---

## 2. 驗證層級（Validation Levels）

TAITS 將資料驗證分為三個層級：

| 層級 | 說明 |
|---|---|
| Schema Level | 結構與型別是否符合 Schema |
| Content Level | 內容合理性（價格、量、連續性） |
| Temporal Level | 時間與交易日一致性 |

任一層級出現致命問題，Validator 可直接給出 `BLOCK`。

---

## 3. 驗證結果狀態（Status）

### 3.1 狀態枚舉
- **OK**：資料可直接使用
- **WARN**：資料可使用，但需警示（下游可選擇降權/跳過）
- **BLOCK**：資料不可用，必須中止或切換來源（Fallback）

### 3.2 狀態升級原則
- 多個 WARN 可累積升級為 BLOCK
- BLOCK 不得被自動降級
- 任何 BLOCK 必須產生 Audit 記錄

---

## 4. Schema Level 規則（結構與型別）

### RULE-S-001：必填欄位存在
**說明**：OHLCV 必填欄位缺失即不可用  
**適用**：bars  
**條件**：缺少 `ts/symbol/open/high/low/close/volume/freq/source/schema_version`  
**狀態**：BLOCK

---

### RULE-S-002：欄位型別錯誤
**說明**：欄位存在但型別不正確  
**條件**：例如價格為字串、ts 非 timestamp  
**狀態**：BLOCK

---

## 5. Content Level 規則（內容合理性）

### RULE-C-001：價格為負或為零
**說明**：價格 <= 0 視為異常  
**條件**：open/high/low/close 任一 <= 0  
**狀態**：BLOCK

---

### RULE-C-002：高低價邏輯錯誤
**說明**：high < low 或 open/close 超出 high/low  
**條件**：  
- high < low  
- open < low or open > high  
- close < low or close > high  
**狀態**：BLOCK

---

### RULE-C-003：缺值率（Missing Rate）
**說明**：資料缺漏比例過高  
**計算**：缺值列數 / 總列數  

| 缺值率 | 狀態 |
|---|---|
| ≤ 1% | OK |
| > 1% 且 ≤ 5% | WARN |
| > 5% | BLOCK |

---

### RULE-C-004：成交量異常（Zero Volume）
**說明**：連續零成交量代表資料品質或交易異常  

| 條件 | 狀態 |
|---|---|
| 單一 bar volume = 0 | WARN |
| 連續 ≥ 3 bars volume = 0 | BLOCK |

---

### RULE-C-005：價格跳躍（Price Spike）
**說明**：非合理範圍的價格跳動  
**方法**：以 ATR 或固定比例檢測（S2 可用固定比例）

| 條件（相對前一 bar） | 狀態 |
|---|---|
| 變動 ≤ 20% | OK |
| > 20% 且 ≤ 50% | WARN |
| > 50% | BLOCK |

> 註：S3 可引入 Regime-aware 門檻（高波動期放寬）

---

## 6. Temporal Level 規則（時間一致性）

### RULE-T-001：時間順序錯亂
**說明**：時間戳未嚴格遞增  
**條件**：ts 非嚴格遞增  
**狀態**：BLOCK

---

### RULE-T-002：頻率不一致
**說明**：bar 間隔不符合 freq 定義  
**條件**：例如 freq=5m，但出現 7 分鐘間隔  
**狀態**：WARN（少量）／BLOCK（大量）

---

### RULE-T-003：非交易日資料
**說明**：出現在非交易日的 bar  

| 情況 | 狀態 |
|---|---|
| 單筆 | WARN |
| 多筆或連續 | BLOCK |

---

### RULE-T-004：資料延遲（Latency）
**說明**：資料時間距離現在過久（S2 Research 僅作提示）  

| 延遲 | 狀態 |
|---|---|
| ≤ 1 交易日 | OK |
| > 1 且 ≤ 5 交易日 | WARN |
| > 5 交易日 | BLOCK |

---

## 7. 規則彙總與升級策略

### 7.1 升級建議
- 任一 BLOCK → DataBundle.status = BLOCK
- 2 個以上 WARN（同 dataset 同 symbol）→ 升級為 BLOCK（可配置）

### 7.2 Dataset 與 Symbol 隔離
- BLOCK 可只影響單一 symbol
- 不得因單一 symbol BLOCK 導致整個 Universe 無法研究（除非明確設定）

---

## 8. ValidationReport 輸出格式（摘要）

Validator 必須輸出：

- dataset
- symbol
- status（OK/WARN/BLOCK）
- issues[]（命中規則）
- summary（rows、missing_rate、zero_volume_bars…）

此報告必須被：
- DataBundle 收納
- AuditRecord 引用
- Orchestrator 可讀取並做決策

---

## 9. 與 Fallback Policy 的關係

- Validator 的 BLOCK 是啟動 Fallback 的 **合法條件**
- Fallback 必須在 Audit 中記錄：
  - 命中哪些 RULE
  - 原始來源 validator 結果

---

## 10. S2 驗收標準（Acceptance）

在 S2 Research 模式下：

1. 任一 dataset 必須經過 Validator
2. Validator 結果必須進入 DataBundle
3. BLOCK 狀態必須中止該資料使用或觸發 Fallback
4. 所有規則命中必須可被 log / report 查詢

---

## 11. 版本紀錄

- 1.0.0：建立 TAITS S2 資料品質驗證最小可用規格（Schema / Content / Temporal）。
