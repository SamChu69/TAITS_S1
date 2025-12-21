# 📘 TAITS_Evidence_Model_and_Weighting.md
## TAITS 證據模型與權重規則（Phase S3）

---

## 0. 文件定位（Evidence 層最高權威）

本文件定義 TAITS 中 **Evidence 的唯一合法模型**。

> 在 TAITS 中：
> - Evidence 是被治理後、可被決策使用的資訊
> - Evidence 不是訊號、不是策略、不是模型輸出
> - Evidence 可以支持、可以降權、可以否決

優先級：
S0 > S1 > S2 > S3-1 > **本文件**

---

## 1. Evidence 的法律地位

Evidence 在 TAITS 中具有以下屬性：

- 可被加權
- 可被否決
- 可被忽略
- 可被淘汰

📌 Evidence **永遠不是決策者**，但 **可以阻止決策**。

---

## 2. Evidence 分級（Tier Model）

### Tier-1｜結構性證據（Structural Evidence）

**來源**
- Market Structure Agent
- Regime / 行為結構
- 主力操盤 / 結構假突破

**特性**
- 具有否決權
- 不參與加權計分
- 優先級最高

**例**
- 吸籌未完成
- 派發階段
- 假突破結構成立

📌 **Tier-1 否決 → 直接 NO_TRADE / WAIT**

---

### Tier-2｜背景性證據（Contextual Evidence）

**來源**
- Fundamental Agent
- 宏觀 / 產業背景
- 長期價值狀態

**特性**
- 不單獨否決
- 作為穩定性背景
- 影響信心帶（confidence_band）

---

### Tier-3｜戰術性證據（Tactical Evidence）

**來源**
- Technical Agent
- 執行層級策略
- 短中期結構

**特性**
- 僅在 Gate PASS 時有效
- 不可推翻 Tier-1 / Tier-4
- 主要影響「是否 TRADE」

---

### Tier-4｜不確定性證據（Uncertainty Evidence）

**來源**
- Risk Context Agent
- 資料缺漏 / 延遲
- 異常波動 / 事件風險

**特性**
- 具有「煞車」效果
- 不直接否決，但可降權或轉 WAIT

📌 **Tier-4 高 → 降權 / WAIT**

---

## 3. Evidence 合法來源（Hard Constraint）

Evidence **必須**來自 Agent 層輸出，且滿足：

- 已標註來源（Agent / Strategy Family）
- 已標註 Tier
- 已標註方向性（Support / Veto / De-weight）
- 已標註資料品質摘要

📌 未標註完整 → 視為無效 Evidence

---

## 4. Evidence 權重模型（Weighting Model）

### 4.1 權重的基本原則

- 權重不是「自信度」
- 權重不等於倉位
- 權重僅用於 **支持度彙整**

---

### 4.2 Tier 權重邏輯（概念性）

| Tier | 角色 | 權重邏輯 |
|---|---|---|
| Tier-1 | 否決 | 不加權，只否決 |
| Tier-2 | 背景 | 穩定加權 |
| Tier-3 | 戰術 | 動態加權 |
| Tier-4 | 煞車 | 反向影響（降權） |

📌 **Tier-1 / Tier-4 永遠優先於 Tier-2 / Tier-3**

---

### 4.3 Regime / MR 對權重的影響

- 高波動 Regime：
  - Tier-3 權重下修
  - Tier-4 敏感度上升

- MR ≥ 2：
  - Tier-3 明顯降權
  - 禁止「強支持 → 直接 TRADE」

---

## 5. Evidence 彙整流程（Aggregation）

Decision Core 在彙整 Evidence 時，**必須依下列順序**：

1. 檢查 Tier-1 是否存在否決
2. 檢查 Tier-4 是否超過不確定性門檻
3. 彙整 Tier-2（背景穩定性）
4. 彙整 Tier-3（戰術支持）

📌 **不得反向彙整**

---

## 6. Evidence → Decision 映射（Conceptual）

### 6.1 合法映射區間

- Tier-1 否決成立 → NO_TRADE / WAIT
- Tier-4 高 → WAIT
- Tier-2 穩定 + Tier-3 支持 → 可進入 TRADE 判斷

📌 **TRADE 不是預設結果**

---

## 7. Evidence 與 Data Quality 的關係

- 資料缺漏 → 自動產生 Tier-4 Evidence
- 來源可信度下降 → Tier-3 降權
- 無法回放 → Evidence 無效

---

## 8. Evidence 違規行為（Hard Prohibitions）

Evidence 層嚴格禁止：

- ❌ 未經 Agent 解讀直接使用 Strategy 輸出
- ❌ 用模型信心當權重
- ❌ 讓 Evidence 直接影響倉位
- ❌ 事後調整 Evidence 以合理化決策

---

## 9. 審計與回放（Auditability）

每一筆 Evidence 必須：

- 可追溯來源
- 可回放生成條件
- 可解釋「為何被忽略 / 否決」

📌 **Evidence 不可成為黑箱**

---

## 10. 定錨語（不可刪）

> **在 TAITS 中，  
> 證據的力量不在於「多強」，  
> 而在於「是否該被聽見」。**

---

## 11. 文件狀態

- ✔ Phase S3（Evidence 模型）
- ✔ 與 Decision Core 完全對齊
- ✔ 支援多策略、多 Agent
- ✔ 可長期演進
