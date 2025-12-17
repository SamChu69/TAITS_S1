# 📘 TAITS_Strategy_Onboarding_and_Governance.md
## TAITS 策略接入與治理規範（Phase S2）

---

## 0. 文件定位（策略治理最高權威）

本文件定義 TAITS **所有策略的合法存在方式**。

> 未通過本文件流程的策略：
> - 不得影響 Evidence
> - 不得影響 Decision
> - 視為「未接入 TAITS」

優先級：
S0 > S1 > S2-1~S2-3 > **本文件**

---

## 1. 策略在 TAITS 中的法律地位

在 TAITS 中：

- 策略不是決策者
- 策略不是下單者
- 策略不是風控者

策略的**唯一合法功能**是：

> **產生「可被治理的 Evidence 或 Flags」**

---

## 2. 策略接入流程（Strategy Onboarding）

任何新策略，必須完整通過以下流程：

### Step 1｜策略基本定義（必填）

- 策略名稱（唯一）
- 策略類型：
  - Technical / Fundamental / Structure / Cross-Market / Other
- 策略目的：
  - 產生 Evidence
  - 產生 Uncertainty Flag

---

### Step 2｜Evidence 映射（Mandatory）

策略必須明確指定：

- Evidence Tier：
  - Tier-1（結構）
  - Tier-2（背景）
  - Tier-3（戰術）
  - Tier-4（不確定性）

- Evidence 性質：
  - 支持（Support）
  - 否決（Veto）
  - 降權（De-weight）

📌 **未指定 Evidence Tier → 不得接入**

---

### Step 3｜Regime / MR 相容性

策略必須聲明：

- 適用 Regime（可多選）
- 禁用 Regime（必填）
- 最高允許 MR 等級

📌 **未聲明 MR 限制 → 預設 MR ≤ 1**

---

### Step 4｜Lane 掛載（Decision Lane）

策略必須掛載至以下其中之一：

- Lane A｜結構 / 行為
- Lane B｜價值 / 基本面
- Lane C｜執行 / 短線

📌 **策略不可同時掛載多條 Lane**

---

### Step 5｜禁止事項聲明（Hard Check）

策略必須聲明並同意：

- 不直接下單
- 不繞過 Decision Core
- 不放寬風控
- 不因績效主張權力

---

### Step 6｜SHADOW 驗證（Required）

- 策略必須先在：
  - RESEARCH
  - PAPER
  - SHADOW  
  模式下運行
- 不得直接進實盤

---

## 3. 策略治理（Strategy Governance）

### 3.1 啟用條件（Enable）

策略僅在以下條件下啟用：

- Gate PASS
- Regime 相容
- MR ≤ 策略允許值
- 所屬 Lane 啟用

---

### 3.2 降權條件（De-weight）

以下任一成立即降權：

- MR 上升
- 不確定性（Tier-4）增加
- 回撤期間

---

### 3.3 停用條件（Disable）

以下任一成立即停用：

- Gate FAIL
- MR > 策略允許值
- 結構性否決 Evidence 成立
- 策略表現長期不穩定

---

## 4. 策略淘汰（Retirement）

### 4.1 合法淘汰理由

- 長期無效
- 風險不對稱
- 結構假設失效
- 與現實（S0）不相容

📌 **不需要績效證明即可淘汰**

---

### 4.2 淘汰流程

1. 標記為 Deprecated
2. 禁止新決策使用
3. 保留歷史資料供審計
4. 永久移除 Decision 路徑

---

## 5. 策略數量與系統穩定性

TAITS 明確定義：

- 策略數量 **不構成風險**
- 未治理的策略才是風險

因此：

> **TAITS 允許策略宇宙無限擴充，  
> 但只允許「被治理的策略」影響決策。**

---

## 6. 與 Decision Core 的隔離規則（Hard Isolation）

- 策略不得知道：
  - 決策結果
  - 是否實盤
  - 倉位大小

- 決策核心不得知道：
  - 策略內部細節
  - 策略「自信度」

📌 **避免回饋迴圈污染**

---

## 7. 策略違規處理（Mandatory）

若策略：

- 越權
- 試圖下單
- 試圖影響風控

必須：

1. 立即停用
2. 記錄違規
3. 回退安全狀態
4. 檢討是否永久淘汰

---

## 8. 策略治理定錨語（不可刪）

> **策略可以很多，  
> 但權力必須很少。**

---

## 9. 文件狀態

- ✔ Phase S2（策略治理）
- ✔ 與 Blueprint / Flow / Modules 完全一致
- ✔ 支援 285+ 策略宇宙
- ✔ 防止策略失控
```

---

## 🎯 Phase S2 完整完成確認（重要里程碑）

你現在已 **完整完成 Phase S2**：

* S2-1 系統架構藍圖
* S2-2 資料流與事件流
* S2-3 模組總覽與介面契約
* **S2-4 策略接入與治理（完成）**

這代表：

> **TAITS 的「骨架、血管、器官、免疫系統」全部建好。**
