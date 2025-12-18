📘 TAITS_交易執行與控制規範（EXECUTION_CONTROL）__251219
PART 1｜文件定位 × Execution 的法律地位 × 不可越權原則

# TAITS_交易執行與控制規範（EXECUTION_CONTROL）
## Execution & Control Specification

---

## 執行前言（Why Execution Is Dangerous）

在交易系統中，  
**Execution 是唯一會造成真實世界後果的行為**。

因此在 TAITS 中，  
Execution 不被視為「流程的一部分」，  
而被視為 **在所有條件成立後，才被允許發生的例外行為**。

---

## 第 1 章｜EXECUTION_CONTROL 的治理位階與約束

### 1.1 文件位階
- 治理等級：**A（執行控制級）**
- 上位文件：
  - `MASTER_ARCH`
  - `MASTER_CANON`
  - `ARCH_FLOW`
  - `RISK_COMPLIANCE`
- 平行約束：
  - `UI_SPEC`

📌 **本文件不得創造任何繞過風控或人類主權的執行路徑。**

---

### 1.2 Execution 的法律地位
Execution 在 TAITS 中被定義為：

> **在人類明確裁決後，  
> 於合法條件仍然成立的瞬間，  
> 對外部市場發生影響的最終行為。**

📌 Execution **不是權力來源**，只是責任承擔點。

---

### 1.3 不可越權原則（Hard Limits）
Execution **永遠不得**：

- 判斷是否該交易
- 推論缺失參數
- 改寫策略假設
- 合理化風控否決
- 在無人類裁決下行動

📌 **Execution 的任何「聰明行為」都是風險。**

---

### 1.4 Execution 的三大責任
Execution 只負責三件事：

1. **正確接收** 人類裁決與執行參數  
2. **忠實執行** 合法委託  
3. **即時中止** 任何被否決或異常的行為  

除此之外，**一律屬於越權**。

---

## 第 2 章｜Execution 與 Canonical Flow 的硬性關係

### 2.1 Execution 在流程中的唯一位置
- 僅存在於：**L11**
- 所有其他層級：
  - 不得觸發任何實際交易行為

📌 **任何在 L11 以外發生的成交，視為違規。**

---

### 2.2 Execution 的最小前置條件（全部必須成立）
Execution 啟動前，**必須同時驗證**：

1. L1–L9 Canonical Flow 全部完成  
2. Governance Gate = Allow  
3. Risk / Compliance = Pass（仍有效）  
4. Human Decision = Approve  
5. Scope Freeze 驗證通過  
6. 文件版本與 Correlation ID 一致  

📌 任一條件失效 → **Execution 不得啟動**。

---

### 2.3 Execution 的即時再驗證（Pre-Execution Check）
即使已通過前置條件，  
Execution 在**送出每一個行為前**，仍必須即時再驗證：

- Risk 狀態是否仍為 Pass
- 市場是否仍開放
- 系統是否穩定
- Kill Switch 是否可用

📌 **再驗證失敗 → 立即中止。**

---

## 第 3 章｜執行參數的合法性與完整性

### 3.1 合法的執行參數來源
Execution 僅能接收來自：

- **Human Decision（L10）**
- 經文件定義的 UI 表單欄位

📌 不得接收：
- 策略自動推論參數
- AI 猜測值
- 預設隱含參數

---

### 3.2 執行參數的最小集合（示例）
每一筆 Execution **至少**需包含：

- 標的（Symbol）
- 交易方向（Buy / Sell）
- 交易單位（odd_lot）
- 委託類型
- 數量
- 有效時間
- Correlation ID

📌 缺任一項 → **Execution 不合法**。

---

### 3.3 參數不可補全原則
- Execution **不得**：
  - 自動補齊數量
  - 調整價格
  - 拆單或合單（除非文件明定）

📌 **不知道就不做，是正確行為。**

---

（EXECUTION_CONTROL · PART 1 結束）

PART 2｜下單前控制 × 下單中監控 × Kill Switch 與失敗處理

## 第 4 章｜下單前控制（Pre-Order Controls）

### 4.1 下單前控制的存在目的
Pre-Order Controls 的目的，是在**任何指令離開系統之前**，  
再次確認「此一執行行為在當下仍然合法、合理、可承擔」。

📌 **所有錯誤，越早被阻止，成本越低。**

---

### 4.2 強制檢查清單（Hard Checklist）
每一筆下單請求，**必須全部通過**以下檢查：

1. **Risk 狀態檢查**  
   - RISK_COMPLIANCE = Pass  
   - 無即時 Degrade / Reject

2. **Human Decision 驗證**  
   - Decision = Approve  
   - 決策時間仍在有效區間內

3. **Scope Freeze 驗證**  
   - 市場 / 商品 / 交易單位皆符合鎖定範圍

4. **參數完整性檢查**  
   - 所有必要欄位齊備
   - 無預設或隱含值

5. **市場狀態檢查**  
   - 市場開放
   - 非禁止交易時段

6. **系統健康檢查**  
   - API 連線正常
   - Kill Switch 可即時觸發

📌 任一項未通過 → **立即阻止下單**。

---

### 4.3 下單前風險重算（Last-Mile Risk Check）
在送單前，Execution 必須進行一次**最後一公里風險確認**：

- 成交假設惡化（滑價、部分成交）
- 流動性瞬間下降
- 成本與曝險是否仍可承受

📌 若最壞情境不可承受 → **即使先前 Pass，仍必須中止**。

---

### 4.4 下單前禁止事項
- 不得：
  - 因「已經走完流程」而忽略即時狀態
  - 將下單失敗視為例外
  - 嘗試「再試一次」以求成交

📌 **下單不是賭博，不存在「試看看」。**

---

## 第 5 章｜下單中監控（In-Order Monitoring）

### 5.1 監控的必要性
一旦下單，Execution 必須假設：
- 市場可能惡化
- 系統可能失效
- 風控條件可能改變

📌 **下單 ≠ 放手不管。**

---

### 5.2 即時監控項目（Mandatory）
Execution 在下單後，**必須持續監控**：

- 訂單狀態（Pending / Partial / Filled / Rejected）
- 市場狀態變化
- Risk / Compliance 即時狀態
- 系統健康狀態

---

### 5.3 即時中止條件（Trigger）
以下任一事件發生，必須立即中止：

- Risk 狀態轉為 Reject
- Kill Switch 被觸發
- 市場進入異常狀態
- 系統錯誤或 API 不穩定

📌 **中止優先於成交。**

---

### 5.4 部分成交的處理原則
- 部分成交屬於：
  - 常態情境
- Execution 必須：
  - 如實記錄
  - 不嘗試補齊剩餘數量（除非文件明定）

📌 **補單 ≠ 修正，而是新風險。**

---

## 第 6 章｜Kill Switch 與 Failure Handling（立即止血機制）

### 6.1 Kill Switch 的法律地位
Kill Switch 為：
- **最高優先權的即時中止機制**
- 不需理由
- 不需確認
- 不可延遲

📌 Kill Switch 的存在，是為了在錯誤發生時**立即停止擴散**。

---

### 6.2 Kill Switch 的觸發來源
Kill Switch 可由以下任一來源觸發：

- RISK_COMPLIANCE
- 系統完整性監測
- 人類主權（手動）

📌 Execution 對 Kill Switch **不具否決權**。

---

### 6.3 Failure Handling 的基本原則
當執行失敗或異常發生時：

- 第一優先：**停止進一步行為**
- 第二優先：**保存狀態與證據**
- 第三優先：**回報與標記**

📌 **修復永遠在事後進行。**

---

### 6.4 常見 Failure 類型與處置
- API Timeout → 停止下單，標記系統風險
- 委託拒絕 → 記錄原因，不重試
- 連線中斷 → 啟動 Kill Switch

---

### 6.5 Failure 的審計要求
每一次 Failure 必須記錄：
- Failure ID
- 類型
- 發生時間
- 影響訂單
- Correlation ID

📌 **沒有 Failure Log → 視為隱性風險。**

---

（EXECUTION_CONTROL · PART 2 結束）

PART 3｜下單後處理 × 模組硬性介面 × 執行最終宣告

## 第 7 章｜下單後處理（Post-Order Handling）

### 7.1 下單後處理的定位
Post-Order Handling 的目的，不是優化績效，  
而是**完整記錄已發生的事實，並確保後續行為不失控**。

📌 成交已發生，系統的責任是「承認現實」，不是「修正結果」。

---

### 7.2 成交結果的法定分類
Execution 對成交結果，僅做以下分類與處理：

- **Fully Filled**：完整成交
- **Partially Filled**：部分成交
- **Rejected / Cancelled**：未成交

📌 不得以事後邏輯重定義成交狀態。

---

### 7.3 成交後的禁止行為
- 不得：
  - 因未滿足策略預期而補單
  - 因價格不理想而追單
  - 因部分成交而自動調整策略

📌 **任何後續動作，都是新流程，必須重新走 Canonical Flow。**

---

### 7.4 成交後資訊回寫（Write-back）
成交後，Execution 僅可回寫：

- Execution Log
- Order / Fill 明細
- 實際成交價格與數量
- 時間戳與 Correlation ID

📌 不得回寫：
- 策略評價
- 成敗判斷
- 合理化註解

---

### 7.5 與績效分析的關係
- Execution **不負責**績效分析
- Execution 的資料：
  - 僅作為事後研究輸入

📌 **績效永遠是事後研究，不是執行指令。**

---

## 第 8 章｜Execution 與其他模組的硬性介面（Hard Interfaces）

### 8.1 與 RISK_COMPLIANCE 的介面
- Execution 必須：
  - 在任何行為前即時查詢 Risk 狀態
  - 尊重最新 Reject / Degrade
- Execution 不得：
  - 緩存 Risk 結果
  - 忽略即時變化

📌 **Risk 狀態以「最新」為準，不以「先前通過」為準。**

---

### 8.2 與 Governance Gate 的介面
- Execution 僅在：
  - Governance Gate = Allow
  - 且 Gate 尚未失效
  時才可啟動

📌 Gate 狀態一旦改變 → Execution 必須立即停止。

---

### 8.3 與 UI / Human Decision 的介面
- Execution 僅能接收：
  - 明確、結構化的人類指令
- 不得：
  - 解讀模糊語句
  - 推論人類意圖

📌 **人類沒說清楚，就不要做。**

---

### 8.4 與 Strategy / AI 的介面
- Strategy / AI：
  - 不得直接呼叫 Execution
  - 不得要求重試、追單
- Execution：
  - 不回饋「好不好」
  - 不提供績效建議

📌 **Execution 是單向責任終點。**

---

### 8.5 與 Log / Audit 的介面
Execution 必須提供：

- Pre-Order Check Log
- In-Order Monitoring Log
- Post-Order Execution Log
- Failure / Kill Switch Log
- Correlation ID

📌 **Log 不齊全 → 執行視為不合法。**

---

## EXECUTION_CONTROL 最終宣告（Closing）

在 TAITS 中，  
Execution 的存在，不是為了讓交易「發生」，  
而是為了確保：

- 不該發生的交易，**不會發生**
- 已經發生的交易，**可以被完整追責**
- 發生錯誤時，**能立即停下來**

> **真正成熟的交易系統，  
> 不是下單最快的系統，  
> 而是最不容易在壓力下做出多餘動作的系統。**

---

（EXECUTION_CONTROL · PART 3 完成）
