📘 TAITS_使用者介面與人機決策規範（UI_SPEC）__251219
PART 1｜文件定位 × UI 的法律地位 × 人機決策總原則

# TAITS_使用者介面與人機決策規範（UI_SPEC）
## User Interface & Human Decision Specification

---

## UI 前言（Why UI Is a Legal Surface）

在 TAITS 中，  
UI 不是「顯示結果的地方」，  
而是 **人類主權被正式行使的唯一合法場域**。

因此，UI 的每一個畫面、欄位、順序與提示文字，  
都具有 **治理與法律意義**。

---

## 第 1 章｜UI_SPEC 的治理位階與不可動搖性

### 1.1 文件位階
- 治理等級：**A（人類主權介面級）**
- 上位文件：
  - `MASTER_ARCH`
  - `MASTER_CANON`
  - `ARCH_FLOW`
  - `RISK_COMPLIANCE`
- 平行約束：
  - `EXECUTION_CONTROL`

📌 **任何 UI 設計不得削弱風控、流程或人類責任。**

---

### 1.2 UI 的法律地位
UI 在 TAITS 中被定義為：

> **人類在完整知情與可被追責的前提下，  
> 對是否承擔風險所做出裁決的法定介面。**

📌 UI **不是建議引擎，也不是績效展示器**。

---

### 1.3 UI 的三大不可越權原則（Hard Limits）

UI **永遠不得**：

- 引導人類做出特定交易選擇
- 隱藏或淡化風險、反證、不確定性
- 將「Approve」設計為預設或推薦選項
- 以績效、勝率、信心度誘導決策

📌 **任何降低決策摩擦的設計，都可能是治理風險。**

---

### 1.4 UI 的唯一正當目的
UI 只為一個目的存在：

> **讓人類在理解風險後，  
> 清楚地表達「要不要承擔後果」。**

---

## 第 2 章｜人機決策的總體原則（Human-in-the-Loop by Design）

### 2.1 人類主權的制度化呈現
人類主權在 UI 中必須被呈現為：

- 明確的選項（Approve / Reject / Defer）
- 清楚的責任提示
- 完整的決策上下文

📌 不得以：
- 自動勾選
- 預設流程
- 快捷鍵  
取代明確決策。

---

### 2.2 UI 不得替人類「想好答案」
UI **可以**：
- 整理資訊
- 揭露衝突
- 顯示不確定性

UI **不得**：
- 告訴人類「該怎麼做」
- 用色彩、排序暗示方向
- 用語言弱化拒絕選項

📌 **UI 的中立性，是 TAITS 的核心防線之一。**

---

### 2.3 決策摩擦（Decision Friction）的必要性
TAITS **刻意保留決策摩擦**：

- 需要閱讀
- 需要確認
- 需要承認風險

📌 若 UI 讓決策「太輕鬆」，  
那不是好體驗，而是風險。

---

### 2.4 UI 與 Canonical Flow 的關係
- UI 僅能出現在：
  - **L10**
- UI 不得：
  - 介入 L7 風控
  - 介入 L8 策略生成
  - 繞過 L9 Governance Gate

📌 **UI 是流程的結果，不是流程的起點。**

---

## 第 3 章｜UI 的強制輸入條件（UI Must-Show）

### 3.1 UI 啟用的前置條件
UI 僅能在以下條件 **全部成立** 時啟用：

1. L1–L9 Canonical Flow 完整
2. Governance Gate = Allow
3. Risk / Compliance ≠ Reject
4. Evidence Bundle 可回放
5. Correlation ID 完整

📌 任一不成立 → **UI 不得要求人類決策**。

---

### 3.2 UI 必須呈現的核心區塊（Overview）
UI **至少**必須包含以下區塊（不得隱藏）：

- 流程狀態總覽（L1–L9）
- Evidence Bundle（支持 / 反證 / 不確定）
- Regime 判定與限制
- Risk / Compliance 狀態與 Reason Codes
- Strategy Hypothesis（含失效條件）
- 決策選項與責任聲明

📌 **UI 的完整性，高於美觀。**

---

（UI_SPEC · PART 1 結束）

PART 2｜資訊呈現秩序 × 決策按鈕法定設計 × 風險與反證強制揭露

## 第 4 章｜資訊呈現順序與視覺中立性（Visual Neutrality）

### 4.1 呈現順序的治理意義
在 TAITS 中，  
**資訊呈現的順序本身即是一種價值判斷**。

因此 UI 的資訊排列，必須遵循治理順序，  
而非使用者習慣或轉換率最佳化。

---

### 4.2 強制資訊呈現順序（不得調換）
UI 必須依照以下順序呈現主要區塊：

1. **流程完整性狀態（L1–L9）**
2. **Risk / Compliance 狀態與 Reason Codes**
3. **Market Regime 與限制**
4. **Evidence Bundle**
   - 支持證據
   - 反證
   - 不確定性
5. **Strategy Hypothesis**
   - 前提
   - 失效條件
6. **Human Decision 區塊**

📌 不得將 Strategy 或決策按鈕提前顯示。

---

### 4.3 視覺中立性（Visual Neutrality）
UI **必須避免任何隱性引導**：

- 顏色：
  - 不得以紅綠暗示方向
- 字體：
  - 不得放大「Approve」
- 位置：
  - Approve / Reject / Defer 必須等權重

📌 **中立不是冷漠，而是負責。**

---

### 4.4 禁止的視覺與互動設計
UI 永久禁止：

- 倒數計時迫使決策
- 勝率、信心指標、大字報
- 「推薦」「最佳」「高勝率」字樣
- 自動聚焦在 Approve

📌 **任何促使快速決策的設計，都是治理風險。**

---

## 第 5 章｜Approve / Reject / Defer 的法定設計

### 5.1 三種決策的法律地位
三種決策在 TAITS 中：

- **Approve**：人類承擔實際風險
- **Reject**：人類選擇不承擔
- **Defer**：人類選擇暫不行動

📌 三者 **法律地位等同**，不得差別對待。

---

### 5.2 決策按鈕的強制規範
UI 中的三個決策按鈕必須：

- 同尺寸
- 同色系
- 同層級
- 不設預設值

📌 預設選項 = 隱性建議（嚴格禁止）。

---

### 5.3 Approve 的責任提示（強制）
在點擊 Approve 前，UI 必須：

- 顯示責任提示文字
- 要求再次確認（Explicit Confirmation）

📌 確認文字不得弱化風險描述。

---

### 5.4 Reject / Defer 的尊重性設計
- Reject / Defer：
  - 不得被隱藏
  - 不得被視為「失敗」
  - 不得要求理由（除非使用者自願）

📌 **不交易，是正確且成熟的選項。**

---

## 第 6 章｜風險、反證與不確定性的強制呈現規則

### 6.1 Risk 區塊的呈現要求
UI 必須清楚呈現：

- 當前 Risk 狀態
- Reason Codes（可展開）
- 是否曾被 Degrade
- 是否存在即時風控監控

📌 Risk 區塊不得摺疊預設。

---

### 6.2 Evidence 的雙面呈現
Evidence 必須以「雙欄或等權」方式呈現：

- 左：支持證據
- 右：反證

📌 不得只呈現支持面。

---

### 6.3 不確定性的獨立區塊
UI 必須保留 **Uncertainty 區塊**：

- 資料不足
- 方法論限制
- Regime 不穩定性

📌 不確定性不得被隱藏在附註中。

---

### 6.4 禁止的語言與敘事
UI 永久禁止使用：

- 必然、確定、穩賺
- 機會難得、稍縱即逝
- AI 強烈建議

📌 **TAITS 不說服，只揭露。**

---

（UI_SPEC · PART 2 結束）

PART 3｜決策記錄 × 模組介面 × 人類主權最終宣告

## 第 7 章｜決策記錄、審計與回放（Decision Logging & Replay）

### 7.1 決策記錄的法律地位
在 TAITS 中：

> **沒有被記錄的人類決策，  
> 在制度上視為「從未發生」。**

UI 的第一責任，不是方便操作，  
而是**確保每一次人類裁決都可被完整追責**。

---

### 7.2 決策記錄的最小集合（Mandatory Fields）
每一次 Human Decision，UI **必須記錄**：

- Decision ID
- 決策類型（Approve / Reject / Defer）
- 決策人識別
- 決策時間（Timestamp）
- 對應 Correlation ID
- 決策時所見文件版本（doc_key + version）
- 當下 Risk / Regime 狀態摘要

📌 缺任一項 → **該決策不合法**。

---

### 7.3 決策前狀態快照（Pre-Decision Snapshot）
UI 必須在決策發生前：

- 凍結當下顯示內容
- 產生 UI Snapshot

📌 以防止事後爭議或畫面被回寫。

---

### 7.4 回放（Replay）的最低要求
UI 回放必須能夠：

- 重現當時畫面結構
- 顯示支持證據 / 反證 / 不確定性
- 還原 Risk / Regime 狀態
- 顯示人類選擇

📌 **回放不是重算，而是重現。**

---

## 第 8 章｜UI 與其他模組的硬性介面（Hard Contracts）

### 8.1 與 Governance Gate（L9）的介面
UI 僅在以下條件成立時顯示決策按鈕：

- Governance Gate = Allow
- Gate 未過期

📌 Gate 狀態一旦改變 → UI 必須立即鎖定。

---

### 8.2 與 RISK_COMPLIANCE（L7）的介面
UI 必須：

- 即時顯示最新 Risk 狀態
- 即時更新 Reason Codes
- 在 Reject 時：
  - 禁止 Approve
  - 清楚說明否決來源

📌 UI 不得延遲或緩存 Risk 狀態。

---

### 8.3 與 EXECUTION_CONTROL（L11）的介面
UI 僅能傳遞：

- 人類裁決結果
- 明確執行參數（若 Approve）

UI **不得**：
- 呼叫 Execution
- 預測成交結果
- 嘗試重送指令

📌 **UI 是裁決者，不是操作者。**

---

### 8.4 與 Strategy / AI 的介面
- Strategy / AI：
  - 僅能提供分析內容
  - 不得影響 UI 排序與樣式
- UI：
  - 不得轉述 AI 的「建議語氣」

📌 **AI 沒有立場，人類才有。**

---

## UI_SPEC 最終宣告（Closing）

在 TAITS 中，  
UI 並不是為了讓交易更快發生，  
而是為了確保：

- 人類知道自己在做什麼
- 人類理解自己在承擔什麼
- 人類的選擇可以被完整追責

> **一套真正成熟的系統，  
> 不是替人類做決定，  
> 而是迫使人類為自己的決定負責。**

---

（UI_SPEC · PART 3 完成）
