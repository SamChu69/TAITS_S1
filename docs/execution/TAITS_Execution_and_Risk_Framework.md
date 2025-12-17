# 📘 TAITS_Execution_and_Risk_Framework.md
## TAITS 執行與風控框架（Phase S4）

---

## 0. 文件定位（Execution 層最高權威）

本文件定義 TAITS **所有「把 Decision 變成行為」的唯一合法方式**。

> 在 TAITS 中：
> - Decision 決定「能不能做」
> - Execution 只負責「安全地做」
> - 任何偏離，都視為高風險事件

優先級：
S0 > S1 > S2 > S3 > **本文件** > S5

---

## 1. Execution Layer 的法律地位

### 1.1 核心責任

Execution Layer 僅負責：

- 接收已完成的 Decision
- 套用所有 Safety Locks
- 依模式執行或模擬
- 回報執行結果（不可影響 Decision）

---

### 1.2 明確禁止

Execution **不得**：

- ❌ 重新解讀 Evidence
- ❌ 修改 Decision（TRADE / WAIT / NO_TRADE）
- ❌ 自行補單、追單、加碼
- ❌ 因滑價或失敗而重試進場

---

## 2. 執行模式（Execution Modes）

### 2.1 RESEARCH（研究模式）

- 僅計算理論執行
- 不產生任何模擬資金變動
- 用於策略驗證與壓力測試

---

### 2.2 PAPER（模擬模式）

- 模擬下單與損益
- 套用完整風控規則
- 不接觸真實券商

---

### 2.3 SHADOW（影子模式）

- 與實盤同步時間
- 不送單，但紀錄「如果有下」
- 用於驗證穩定性與延遲

---

### 2.4 LIVE_RESTRICTED（限制實盤）

- 真實下單
- 僅允許：
  - 低風險 Lane
  - 小倉位
  - 嚴格 Safety Locks

📌 **任何系統初期只允許到 LIVE_RESTRICTED**

---

## 3. Safety Locks（安全鎖，核心）

### 3.1 全域安全鎖（Global Locks）

以下任一成立，**立即鎖死 Execution**：

- 系統異常
- 連續重大錯誤
- 回撤超過上限
- 人工 Emergency Stop

---

### 3.2 資金風控鎖（Capital Locks）

- 單筆最大風險（R per Trade）
- 單日最大損失
- 單標的最大曝險
- Lane 專屬風險上限

---

### 3.3 行為風控鎖（Behavioral Locks）

- 禁止加碼
- 禁止攤平
- 禁止追價
- 禁止補單

📌 **Execution 不相信任何「這次不一樣」**

---

## 4. 決策 → 執行 的不可逆規則

- NO_TRADE → Execution 必須為空操作
- WAIT → Execution 只監控
- TRADE → 僅執行一次，不重試

📌 **Execution 是一次性的，不是互動式的**

---

## 5. 零股與低資本執行（重要）

TAITS 明確支援：

- 零股交易
- 低資本測試
- 漸進式放量（需 S5 批准）

### 原則

- 零股 ≠ 放鬆風控
- 小錢 ≠ 可以亂來
- 風控比例與大資本一致

---

## 6. 失敗與異常處理

### 6.1 下單失敗

- 記錄失敗
- 不重試
- 不追單
- 回到 WAIT

---

### 6.2 滑價 / 延遲

- 視為市場風險
- 不修改 Decision
- 記錄於 Execution Log

---

## 7. 審計與回放

Execution 必須記錄：

- 接收到的 Decision
- 套用的 Safety Locks
- 實際行為（或未行為）
- 結果與異常

📌 **必須能回答：「為什麼這一單會下 / 為什麼沒下」**

---

## 8. 常見致命錯誤（Explicitly Forbidden）

- ❌ Execution 自動補救 Decision
- ❌ 因連續成功而放寬鎖
- ❌ 因市場快速變動而加碼
- ❌ 因資金小而忽略比例

---

## 9. 定錨語（不可刪）

> **執行層存在的目的，  
> 不是幫你多賺，  
> 而是幫你活下來。**

---

## 10. 文件狀態

- ✔ Phase S4（執行與風控總框架）
- ✔ 僅服從 S0–S3
- ✔ 支援零股與低資本
- ✔ 可長期演進
