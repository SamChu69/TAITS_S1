📘 TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）__251219
PART 1｜文件定位 × Feature 的法律地位 × 索引治理原則

# TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）
## Strategy Feature & Factor Index (Governance-Aligned)

---

## Feature 前言（Why Features Must Stay Silent）

在 TAITS 中，  
Feature 的價值不在於「預測」，  
而在於 **提供可被質疑、可被反證的市場描述**。

任何會「暗示方向」的 Feature，  
在制度上都是 **越權的 Feature**。

---

## 第 1 章｜STRATEGY_FEATURE_INDEX 的治理位階與適用範圍

### 1.1 文件位階
- 治理等級：**B（方法論與特徵治理級）**
- 上位文件：
  - `MASTER_ARCH`
  - `MASTER_CANON`
- 平行約束：
  - `ARCH_FLOW`
  - `DATA_SOURCES`
  - `STRATEGY_UNIVERSE`
- 下位文件：
  - 各策略實作文件（不得覆寫本索引）

📌 **任何策略僅能使用本文件列管之 Feature。**

---

### 1.2 適用範圍（Scope）
本文件規範：

- 所有技術、統計、結構性特徵
- 所有被 Strategy / Evidence / Regime 引用之因子
- 不論是否最終進入 Execution

📌 **被計算、被顯示、被引用，即受本文件約束。**

---

## 第 2 章｜Feature 在 TAITS 中的法律地位

### 2.1 Feature ≠ Signal ≠ Decision
在 TAITS 中：

- **Feature**：  
  對 Snapshot 的定量或結構描述
- **Signal**：  
  Feature 在特定條件下的狀態表述（僅限 Evidence）
- **Decision**：  
  人類在 UI 中的選擇

📌 Feature **不得單獨形成 Signal**。

---

### 2.2 Feature 的唯一合法輸出
Feature **只能輸出**：

- 數值或分類結果
- 計算方法論描述
- 適用 / 禁用 Regime 標註
- 已知限制（Limitations）

📌 **任何「建議、方向、分數」屬於非法輸出。**

---

### 2.3 Feature 與 Canonical Flow 的位置
Feature 僅能存在於：

- **L4｜Feature & Methodology**

Feature **不得**：
- 介入 L5 Evidence 組裝邏輯
- 介入 L6 Regime 裁決
- 影響 L7 Risk 否決

📌 **Feature 是被使用的材料，不是裁判。**

---

## 第 3 章｜Feature 白名單與索引結構（Index Schema）

### 3.1 Feature 白名單制度
TAITS 採用 **嚴格 Feature 白名單**：

- 列於本文件 → 可被計算、顯示、引用
- 未列於本文件 → 禁止存在於系統

📌 **不存在「策略內私有 Feature」。**

---

### 3.2 Feature 索引的最小欄位（Mandatory）
每一 Feature，**必須完整定義**：

- Feature ID（唯一）
- 類型（技術 / 統計 / 結構 / 事件）
- 資料來源（Source IDs）
- 方法論版本
- 適用 Regime
- 禁用 Regime
- 計算頻率
- 已知限制
- 可引用策略類型

📌 缺任一欄位 → **Feature 不可被載入**。

---

### 3.3 Feature 版本化與凍結
- Feature 方法論變更：
  - 視為 **新 Feature**
- 舊版本：
  - 必須可回放
  - 不得覆寫

📌 **Feature 變更 ≠ 參數微調，而是制度事件。**

---

（STRATEGY_FEATURE_INDEX · PART 1 結束）

PART 2｜趨勢・結構・波動・動能・流動性 Feature 全集（治理對齊）

## 第 4 章｜趨勢與結構型 Feature（Trend & Structure）

### 4.1 治理前提
趨勢與結構型 Feature 的任務是：
> **描述價格結構的形態與穩定性，而非預測方向。**

📌 任一趨勢 Feature 若被解讀為「多空建議」，即屬誤用。

---

### 4.2 趨勢強度 Feature（Trend Strength）

**Feature ID**：`FEAT_TREND_STRENGTH`

- 類型：技術 / 結構
- 資料來源：`TWSE_MKT`, `TPEX_MKT`
- 方法論：結構斜率 + 穩定度（非方向）
- 輸出形式：等級 / 區間值
- 適用 Regime：趨勢 / 波動擴張
- 禁用 Regime：高噪音震盪
- 計算頻率：日 / 盤中
- 已知限制：
  - 趨勢末端可能誤判
- 可引用策略：
  - Trend / Momentum

📌 不得用於判斷進出場方向。

---

### 4.3 趨勢一致性 Feature（Trend Consistency）

**Feature ID**：`FEAT_TREND_CONSISTENCY`

- 描述：多時間尺度結構是否一致
- 治理用途：
  - 作為 Evidence 的「穩定性描述」
- 禁止用途：
  - 單獨形成 Signal

---

### 4.4 結構破壞 Feature（Structure Break）

**Feature ID**：`FEAT_STRUCT_BREAK`

- 類型：結構
- 描述：既有價格結構是否被破壞
- 治理用途：
  - 觸發策略失效條件
- 已知風險：
  - 偽破壞（False Break）

📌 結構破壞 ≠ 反轉確認。

---

## 第 5 章｜波動、動能與流動性 Feature（Volatility / Momentum / Liquidity）

### 5.1 波動狀態 Feature（Volatility Regime）

**Feature ID**：`FEAT_VOL_STATE`

- 類型：統計
- 資料來源：`TWSE_MKT`, `TAIFEX_FUT`
- 描述：
  - 波動擴張 / 收斂狀態
- 適用 Regime：
  - 風險評估
- 禁止用途：
  - 預測方向

📌 僅能用於「是否適合交易」。

---

### 5.2 動能持續 Feature（Momentum Persistence）

**Feature ID**：`FEAT_MOM_PERSIST`

- 描述：
  - 動能是否具延續性
- 治理用途：
  - 評估 Momentum 策略前提是否仍成立
- 已知限制：
  - 事件驅動下易失效

---

### 5.3 流動性充足度 Feature（Liquidity Adequacy）

**Feature ID**：`FEAT_LIQ_ADEQ`

- 類型：結構 / 風險
- 資料來源：`TWSE_MKT`, `TPEX_MKT`
- 描述：
  - 是否滿足最低流動性門檻
- 治理用途：
  - Risk Overlay
- 禁用情境：
  - 流動性快速惡化

📌 此 Feature 可直接導致策略禁用，但不可導致下單。

---

## 第 6 章｜事件與市場狀態描述 Feature（Event & State）

### 6.1 事件接近度 Feature（Event Proximity）

**Feature ID**：`FEAT_EVENT_PROXIMITY`

- 類型：事件 / 狀態
- 資料來源：`MOPS_CORP`
- 描述：
  - 重大事件距離當前時間的接近程度
- 治理用途：
  - 調高不確定性權重
- 禁止用途：
  - 事件方向預測

---

### 6.2 市場壓力狀態 Feature（Market Stress）

**Feature ID**：`FEAT_MKT_STRESS`

- 類型：結構 / 風險
- 描述：
  - 市場整體壓力狀態
- 治理用途：
  - Regime 裁決輔助
- 已知限制：
  - 高度情緒性

---

### 6.3 狀態穩定度 Feature（State Stability）

**Feature ID**：`FEAT_STATE_STABILITY`

- 描述：
  - Regime 是否頻繁切換
- 治理用途：
  - 防止策略過度切換
- 禁止用途：
  - 交易時點判斷

---

（STRATEGY_FEATURE_INDEX · PART 2 結束）

PART 3｜Feature 組合治理 × 誤用防呆 × 最終宣告（最大完備）

## 第 7 章｜Feature 組合、Evidence 生成與禁用規則

### 7.1 Feature 組合的治理定位
在 TAITS 中，Feature **可以被組合**，但組合本身並不等於 Evidence。

> **Feature 組合僅是描述的豐富化，  
> Evidence 才是可被質疑與反證的判斷單元。**

📌 任何將 Feature 組合直接視為「訊號」的行為，皆屬越權。

---

### 7.2 合法的 Feature 組合原則
Feature 組合必須遵守：

1. **同層級原則**  
   - 不得跨 L4 / L5 / L6 混用
2. **非方向性原則**  
   - 組合後不得形成多空暗示
3. **可反證原則**  
   - 必須能被其他 Evidence 否定

📌 不可反證的組合，視為無效組合。

---

### 7.3 Feature → Evidence 的轉換邊界
Feature 轉為 Evidence 時，必須：

- 明確說明使用了哪些 Feature
- 標示不確定性來源
- 指出 Evidence 的適用範圍

📌 Evidence 的生成責任在 **L5 模組**，  
📌 **Feature 模組不得自行升級角色**。

---

### 7.4 Feature 禁用與降級規則
以下情境，Feature **必須被禁用或降級**：

- 資料來源異常
- 延遲超標
- Regime 不適用
- 與其他 Feature 出現結構性衝突

📌 禁用 Feature 是風控行為，不是策略失敗。

---

## 第 8 章｜Feature 誤用清單與強制防呆（Misuse Guardrails）

### 8.1 永久禁止的 Feature 誤用行為
以下行為 **制度上禁止**：

- 將 Feature 顯示為「買賣建議」
- 以 Feature 數值排序標的
- 用 Feature 打分數、信心度
- 將 Feature 直接連結至 Execution

📌 違反任一項 → 視為治理違規。

---

### 8.2 常見誤用情境（必須被攔截）

| 誤用情境 | 治理處置 |
|---|---|
| Feature 被單獨使用 | 阻擋生成 Evidence |
| 多 Feature 疊加形成方向 | 標記為越權 |
| Feature 被策略硬編碼 | 禁止載入 |
| Feature 被 UI 強調呈現 | UI 必須中立化 |

📌 **防呆不是限制研究，而是保護系統。**

---

### 8.3 Feature 與 AI 的互動邊界
AI Agent 在使用 Feature 時：

- 可以：
  - 描述
  - 比較
  - 質疑
- 不得：
  - 強化方向
  - 壓低不確定性
  - 給出結論性建議

📌 **AI 不得替 Feature 發聲。**

---

### 8.4 Feature 的審計與回放
每一被使用的 Feature，必須可：

- 回放當時計算結果
- 查詢方法論版本
- 追溯資料來源

📌 **不可回放的 Feature，等同不存在。**

---

## STRATEGY_FEATURE_INDEX 最終宣告（Closing）

在 TAITS 中，  
Feature 的存在不是為了更聰明，  
而是為了更誠實地描述市場。

如果一套系統：
- 讓 Feature 偷偷說話
- 讓數值暗示方向
- 讓模型代替人類判斷

那它最終會在「看似科學」的外衣下，  
做出無法被追責的決策。

> **真正成熟的 Feature 系統，  
> 不是計算得多精巧，  
> 而是永遠知道：  
> 自己不能決定任何事。**

---

（STRATEGY_FEATURE_INDEX · PART 3 完成）
