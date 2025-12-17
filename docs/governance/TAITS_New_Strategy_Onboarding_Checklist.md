# 📘 TAITS_New_Strategy_Onboarding_Checklist.md
## TAITS 新策略接入檢查清單（Strategy Onboarding Checklist）

---

## 0. 文件定位（必讀）

本文件定義：  
**任何新策略、新模型、新指標、新交易邏輯，  
在接入 TAITS 之前，必須完整通過的標準化檢查流程。**

> 未通過本清單者：
> - 不得進入 Decision Core
> - 不得影響 Trade / Wait / No Trade
> - 不得在實盤環境啟用

本文件屬於：**[GOV] Strategy Governance 強制規範**

---

## 1. 策略基本資訊（必填）

- 策略名稱：
- 策略類型：
  - ⬜ 技術型
  - ⬜ 基本面
  - ⬜ 行為 / 結構（如威科夫）
  - ⬜ 跨市場（期貨 / 選擇權）
  - ⬜ 其他（說明）
- 策略來源：
  - ⬜ 原創
  - ⬜ 改寫既有策略
  - ⬜ 研究論文 / 專案（需標註）

---

## 2. 策略層級定位（不可模糊）

請明確選擇 **唯一主要角色**：

- ⬜ Evidence（證據 / 解讀）
- ⬜ Filter（過濾 / 否決）
- ⬜ Weight Adjuster（權重調整）
- ⬜ Execution（僅限已批准的執行層）

📌 **禁止直接標註為「Decision / Entry / Alpha」**

---

## 3. Decision Lane 歸屬（必選）

此策略屬於哪一條決策風格線：

- ⬜ Lane A｜Market Structure / 行為線
- ⬜ Lane B｜Value / Fundamental 價值線
- ⬜ Lane C｜Execution / Short-Term 執行線
- ⬜ Lane D｜（新增需審核）

---

## 4. Regime 相容性檢查（必填）

此策略在下列市場狀態中是否允許存在：

| Regime | 允許 | 不允許 |
|---|---|---|
| Trend | ⬜ | ⬜ |
| Range | ⬜ | ⬜ |
| High Volatility | ⬜ | ⬜ |
| Event / Settlement | ⬜ | ⬜ |

📌 **未填寫視為「不允許」**

---

## 5. Manipulation Risk（MR）相容性

請標註在以下操盤風險等級時的策略狀態：

| MR Level | 行為 |
|---|---|
| MR-0 | ⬜ 正常 |
| MR-1 | ⬜ 正常 / ⬜ 降權 |
| MR-2 | ⬜ 降權 / ⬜ 禁用 |
| MR-3 | ⬜ 禁用（必選） |

📌 **MR-3 必須為「禁用」**

---

## 6. 風險與失效模式（強制揭露）

請明確說明：

- 策略最容易失效的情境：
- 是否會在「假突破 / 派發盤」誤判？
- 是否在「消息行情」容易被誘導？
- 最大可接受誤判成本（方向錯 / 時間錯）：

📌 **未能說清失效模式 → 不准接入**

---

## 7. 是否涉及「預測」？（高風險區）

- 是否使用未來價格預測？
  - ⬜ 否（推薦）
  - ⬜ 是 → 僅允許作為「Uncertainty Flag」

若選「是」，必須同意以下限制（全選）：

- ⬜ 不可直接觸發進場
- ⬜ 不可提高倉位
- ⬜ 不可否決 Gate / Risk
- ⬜ 僅用於降權或 NO_TRADE 傾向

---

## 8. Decision Core 輸入對應確認（必選）

請確認此策略 **只會透過以下合法入口影響 Decision Core**：

- ⬜ Evidence Summary（摘要）
- ⬜ Risk / Uncertainty Flag
- ⬜ Strategy Availability（可用 / 不可用）

📌 **禁止直接輸入價格預測值或原始訊號**

---

## 9. 回測與驗證要求（最低標準）

- 是否通過基本歷史驗證？
  - ⬜ 是
  - ⬜ 否（僅限研究狀態，不可實盤）
- 是否觀察過「最差情境」？
  - ⬜ 是
  - ⬜ 否

📌 **TAITS 不要求高勝率，但要求可解釋失敗**

---

## 10. 最終接入審核（必填）

- 是否通過所有 Gate / MR / Governance 規則？
  - ⬜ 是 → 可進入沙盒（Paper / Shadow）
  - ⬜ 否 → 禁止接入

審核者：
- 日期：
- 備註：

---

## 11. TAITS 官方接入準則（不可刪）

> **TAITS 不拒絕新策略，  
> 但拒絕無法被治理的新策略。  
> 能被清楚否決的策略，  
> 才有資格被使用。**
