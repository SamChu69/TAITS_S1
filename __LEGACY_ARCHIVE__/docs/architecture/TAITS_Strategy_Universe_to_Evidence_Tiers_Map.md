# 📘 TAITS_Strategy_Universe_to_Evidence_Tiers_Map.md
## TAITS 策略宇宙 → 證據層級映射（Single Mapping Authority）

---

## 0. 文件定位（必讀）

本文件是 TAITS 中 **「策略如何影響決策」的唯一映射權威**。

- 所有策略（技術 / 基本面 / 行為 / 跨市場 / 未來新增）
- **不得直接影響 Decision Core**
- 必須先被映射為：
  - Evidence（證據）
  - Filter（否決）
  - Weight Adjuster（權重調整）
  - Governance Flag（可用性）

> 若策略未出現在本映射表中，  
> 視為 **「未接入 TAITS」**。

---

## 1. Evidence Tier 定義（由高到低）

### Tier-1｜結構性證據（Structural Evidence）
**權限：可否決、可降權（最高）**

- 市場結構（威科夫：吸籌 / 派發 / Spring / UTAD）
- 主力操盤風險（MR-0 ～ MR-3）
- Regime 狀態（Trend / Range / High Vol / Event）
- 結算 / 制度性扭曲

📌 特性：
- 不追求進場點
- 專門用來 **防止被割**
- 可直接導致 WAIT / NO_TRADE

---

### Tier-2｜基本面與中期證據（Contextual Evidence）
**權限：可降權、可延後、不直接否決**

- 財報品質 / 現金流
- 估值區間 / 安全邊際
- 產業趨勢 / 景氣循環
- 長線資金偏好

📌 特性：
- Explore 主導
- 決定「值不值得研究 / 等待」
- 不給精準時點

---

### Tier-3｜行為與短期證據（Tactical Evidence）
**權限：可加權、可減權（需受 Gate 限制）**

- 技術型策略（MA / RSI / MACD / 型態）
- 成交量行為
- 短線動能 / 反轉訊號
- Execution Timing Signals

📌 特性：
- 只在 Gate 允許時有效
- 不可單獨觸發交易

---

### Tier-4｜不確定性與風險提示（Uncertainty Evidence）
**權限：僅能降權 / 提高 NO_TRADE 傾向**

- 波動擴張 / 分布不穩
- 時間結構異常
- 預測模型不確定性（如 Kronos 類）

📌 特性：
- 永遠不能當 Alpha
- 只能踩煞車

---

## 2. 策略類型 → Evidence Tier 映射表（核心）

| 策略類型 | Evidence Tier | Decision Lane | 主要作用 |
|---|---|---|---|
| 威科夫行為 | Tier-1 | Lane A | 否決 / 防割 |
| 主力操盤風險 | Tier-1 | Lane A | 禁用策略 |
| 市場 Regime | Tier-1 | All | 啟用 / 停用 |
| 基本面評分 | Tier-2 | Lane B | 篩選 / 等待 |
| 估值策略 | Tier-2 | Lane B | 值得布局 |
| 技術突破 | Tier-3 | Lane C | 進場時機 |
| 技術回檔 | Tier-3 | Lane C | 補倉時機 |
| 成交量策略 | Tier-3 | Lane C | 確認 |
| 期貨影響 | Tier-1 / 3 | Lane A / C | Regime / 權重 |
| 選擇權壓力 | Tier-1 | Lane A | 支撐 / 壓力 |
| 預測模型 | Tier-4 | All | 風險提示 |

---

## 3. Regime × Tier 啟用矩陣（摘要）

| Regime | Tier-1 | Tier-2 | Tier-3 | Tier-4 |
|---|---|---|---|---|
| Trend | ✔ | ✔ | ✔ | ✔ |
| Range | ✔ | ✔ | ⚠（降權） | ✔ |
| High Vol | ✔ | ⚠ | ❌ | ✔ |
| Event / Settlement | ✔ | ⚠ | ❌ | ✔ |

---

## 4. MR（操盤風險）× Tier 規則

| MR 等級 | Tier-1 | Tier-2 | Tier-3 | Tier-4 |
|---|---|---|---|---|
| MR-0 | 正常 | 正常 | 正常 | 正常 |
| MR-1 | 正常 | 正常 | ⚠ | 正常 |
| MR-2 | 正常 | ⚠ | ❌ | 正常 |
| MR-3 | 正常 | ❌ | ❌ | 正常 |

📌 **MR-3 時：只允許 Tier-1 與 Tier-4 存在**

---

## 5. Decision Core 的使用方式（重點）

Decision Core **不讀任何單一策略訊號**，只讀：

- Tier-1：是否存在否決？
- Tier-2：是否值得等待？
- Tier-3：在 Gate 允許下的加權摘要
- Tier-4：是否提高 NO_TRADE 傾向？

---

## 6. 新策略接入流程（對應文件）

所有新策略，必須：

1. 填寫《TAITS_New_Strategy_Onboarding_Checklist.md》
2. 指定 Evidence Tier
3. 指定 Regime / MR 條件
4. 更新本映射文件

---

## 7. 官方準則（可引用）

> **策略可以很多，  
> 但只有被正確分類的策略，  
> 才能進入決策系統。  
> TAITS 的強度，  
> 來自治理，而不是數量。**

---

## 8. 文件狀態

- ✔ 可直接存入 GitHub
- ✔ 與 Decision Core Inputs Index 完全相容
- ✔ 不限制未來策略擴充
- ✔ 防止策略污染決策

