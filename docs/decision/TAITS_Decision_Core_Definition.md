# 📘 TAITS_Decision_Core_Definition.md
## TAITS 決策核心定義（Phase S3）

---

## 0. 文件定位（Decision 層最高權威）

本文件定義 TAITS 的 **唯一合法決策核心（Decision Core）**。

> 在 TAITS 中：
> - 策略不決策
> - Agent 不決策
> - 模型不決策
> - 只有 Decision Core 可以決策

優先級：
S0 > S1 > S2 > **本文件** > S4 / S5

---

## 1. Decision Core 的角色與責任

### 核心責任（Only These）

Decision Core 僅負責：

1. 接收「被允許的輸入」
2. 執行強制 Gate 與否決檢查
3. 整合 Evidence 與風險狀態
4. 輸出 **唯一決策**

### 明確不負責（Never）

- 不分析市場
- 不預測價格
- 不選股
- 不下單
- 不解釋策略內部邏輯

---

## 2. 合法輸入（Authorized Inputs）

Decision Core 只接受以下輸入：

### 2.1 Governance 狀態（最高優先）

- Regime State
- MR Level
- Risk Budget / System State
- Strategy & Lane Availability

📌 **任何 Gate FAIL → 直接 NO_TRADE（不進入後續步驟）**

---

### 2.2 Evidence Summary（已解讀）

- Tier-1（結構 / 行為）
- Tier-2（背景 / 基本面）
- Tier-3（戰術 / 執行）
- Tier-4（不確定性）

📌 Evidence 必須來自 Agent 層，不得直接來自 Strategy

---

### 2.3 Data Quality & Integrity Flags

- Missing / Delayed / Stale
- Source Confidence
- Snapshot Completeness

📌 資料品質不足 → 決策偏向 WAIT / NO_TRADE

---

## 3. 決策流程（Strict Order, Non-Reversible）

Decision Core **必須依下列順序執行**，不可跳步、不可重排：

### Step 1｜Hard Gate Check（硬性否決）

依序檢查：

1. 系統狀態（Maintenance / Mode）
2. Regime 是否允許交易
3. MR Level 是否超標
4. Risk Budget 是否可用
5. 合規 / 人工鎖定

📌 **任一 FAIL → 輸出 NO_TRADE（結束）**

---

### Step 2｜Structural Veto（結構性否決）

- Tier-1 Evidence 是否存在否決？
- 是否存在「主力操盤 / 結構假突破」警示？

📌 成立 → NO_TRADE 或 WAIT（依規則）

---

### Step 3｜Uncertainty Brake（不確定性煞車）

- Tier-4 Evidence 是否過高？
- 資料品質是否不足？

📌 成立 → 降權或 WAIT

---

### Step 4｜Support Aggregation（支持度彙整）

僅在 **通過前述所有否決**後，才進行：

- Tier-2（基本面 / 背景）
- Tier-3（戰術 / 技術）

📌 此步 **只能增加信心，不能推翻否決**

---

### Step 5｜Decision Mapping（決策映射）

依支持度、風險狀態、Lane 可用性，  
映射為以下之一：

- TRADE（允許進入 S4）
- WAIT（觀察，不進場）
- NO_TRADE（禁止交易）

📌 **NO_TRADE 是正常且健康的輸出**

---

## 4. 決策輸出（唯一合法）

Decision Core 的唯一合法輸出為：

```

Decision = {
action: TRADE | WAIT | NO_TRADE,
lane: A | B | C | NONE,
confidence_band: LOW | MEDIUM | HIGH,
rationale_summary: {
gates,
key_evidence,
veto_reasons,
uncertainty_flags
}
}

```

📌  
- `lane = NONE` 僅在 WAIT / NO_TRADE  
- `confidence_band` 不等於倉位大小

---

## 5. 禁止行為（Hard Prohibitions）

Decision Core 嚴格禁止：

- ❌ 因策略多數決而進場
- ❌ 因模型信心高而進場
- ❌ 因錯過行情而進場
- ❌ 因短期績效壓力而放寬否決

---

## 6. 與 Execution 的關係（Strict Separation）

- Decision Core **不產生任何下單參數**
- Execution **不得修改 Decision**
- Execution 失敗不得反向觸發新 Decision

---

## 7. 審計與回放（Auditability）

每一筆 Decision 必須：

- 綁定 Snapshot ID
- 可回放相同輸入 → 相同輸出
- 可查詢「為何 NO_TRADE」

📌 **無法解釋 NO_TRADE 的系統是危險的**

---

## 8. 設計定錨語（不可刪）

> **TAITS 的決策不是為了「不錯過」，  
> 而是為了「不做錯」。**

---

## 9. 文件狀態

- ✔ Phase S3（決策核心）
- ✔ 僅受 S0–S2 約束
- ✔ 全系統唯一決策來源
- ✔ 可審計、可回放、可演進
```

---

## ✅ S3 進度確認

你現在完成：

* **S3-1：Decision Core Definition**

這代表 **TAITS 已經有「大腦」**，而且是**受憲法約束的大腦**。

---
