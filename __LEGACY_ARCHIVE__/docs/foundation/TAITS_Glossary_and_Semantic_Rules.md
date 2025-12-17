# 📘 TAITS_Glossary_and_Semantic_Rules.md
## TAITS 名詞定義與語義規則（Phase S1）

---

## 0. 文件定位（語義最高權威）

本文件定義 TAITS 系統內 **所有關鍵名詞的唯一合法語義**。

> 語義錯誤會導致：
> - 錯誤設計
> - 錯誤決策
> - 錯誤風控
>
> 因此，本文件優先級：
> **S0 > S1-1（Charter）> S1-2（Principles）> 本文件**

---

## 1. 核心名詞定義（Authoritative Definitions）

### 1.1 Strategy（策略）

**定義**：  
策略是「**產生證據（Evidence）或偏好（Bias）的方法**」。

**策略不是**：
- 下單者
- 決策者
- 風控者

**硬性規則**：
- 策略不得直接影響資金
- 策略只能輸出 Evidence / Flags

---

### 1.2 Agent（代理 / 智能體）

**定義**：  
Agent 是「**負責解讀、彙整、轉譯資訊的角色**」。

**Agent 可以**：
- 解讀策略輸出
- 彙整多來源證據
- 提供 Decision Input

**Agent 不可以**：
- 直接下單
- 繞過治理規則
- 自行決定 Trade / No-Trade

---

### 1.3 Signal（訊號）

**定義**：  
Signal 是「**單一條件成立的觀察結果**」。

**語義規則**：
- Signal ≠ Decision
- Signal ≠ Entry
- Signal 只能作為 Evidence 的組成部分

---

### 1.4 Evidence（證據）

**定義**：  
Evidence 是「**經過解讀後、可被決策系統使用的資訊**」。

**分類**：
- Tier-1：結構性證據（可否決）
- Tier-2：背景性證據
- Tier-3：戰術性證據
- Tier-4：不確定性證據

**硬性規則**：
- Evidence 可加權、可否決
- Evidence 不可直接下單

---

### 1.5 Decision（決策）

**定義**：  
Decision 是「**經治理流程後的唯一行動輸出**」。

**合法輸出僅限**：
- TRADE
- WAIT
- NO_TRADE

**硬性規則**：
- Decision 只能由 Decision Core 產生
- 任何其他模組不得宣稱「已決策」

---

### 1.6 Decision Core（決策核心）

**定義**：  
Decision Core 是「**負責整合 Gate / Risk / Evidence / Governance 的唯一決策單元**」。

**語義規則**：
- 單一存在
- 不可複製
- 不可被策略繞過

---

### 1.7 Regime（市場狀態）

**定義**：  
Regime 是「**市場的高階結構狀態**」。

**例**：
- TREND
- RANGE
- HIGH_VOL
- EVENT

**語義規則**：
- Regime 用來「限制策略可用性」
- 不用來預測方向

---

### 1.8 Manipulation Risk（MR）

**定義**：  
MR 是「**市場被操盤、扭曲的風險等級**」。

**等級**：
- MR-0 ～ MR-3

**硬性規則**：
- MR-3 → NO_TRADE
- MR ≥ 2 → 禁止加碼

---

### 1.9 Execution（執行）

**定義**：  
Execution 是「**在被允許的模式下，將 Decision 轉為行為**」。

**語義規則**：
- Execution 不產生 Decision
- Execution 必須服從 Safety Locks

---

### 1.10 Model（模型）

**定義**：  
Model 是「**輔助分析的數學或統計工具**」。

**硬性規則**：
- Model ≠ Strategy（除非明確定義）
- Model 輸出屬於 Evidence 或 Uncertainty
- Model 不得直接影響倉位

---

## 2. 禁止語義混用（Common Violations）

以下用語 **在 TAITS 中視為錯誤**：

- ❌「這個策略決定要買」
- ❌「AI 判斷應該進場」
- ❌「訊號很強所以一定會漲」
- ❌「模型下單」

正確說法應為：

- ✔「策略產生 Tier-3 Evidence」
- ✔「Decision Core 輸出 TRADE」
- ✔「Gate 通過但風險受限」

---

## 3. 語義檢查規則（Mandatory）

所有新文件 / 新策略 / AI 輸出，必須檢查：

- 是否將 Strategy 說成 Decision？
- 是否將 Signal 當成 Entry？
- 是否將 Model 當成 Authority？

若任一成立 → **語義違規，必須修正**

---

## 4. 對 AI 的明確指令（可引用）

> 在 TAITS 中，  
> **你不得將任何策略、模型或訊號，  
> 描述為「決策者」或「下單者」。**

---

## 5. 一句話語義鐵律（不可刪）

> **語義一亂，系統必崩。  
> TAITS 先定義語言，  
> 才允許行為。**

---

## 6. 文件狀態

- ✔ Phase S1（語義層）
- ✔ 所有文件必須遵守
- ✔ 防止 AI 與人類誤解
- ✔ 可長期引用
