📘 TAITS_策略宇宙全集（STRATEGY_UNIVERSE）__251219
PART 1｜文件定位 × 策略的法律地位 × 策略白名單原則

# TAITS_策略宇宙全集（STRATEGY_UNIVERSE）
## Strategy Universe & Governance-Aligned Specification

---

## 策略前言（Why Strategies Must Be Tamed）

在多數交易系統中，  
策略被視為「創造 Alpha 的引擎」。

在 TAITS 中，  
**策略被視為一種「假設生成器（Hypothesis Generator）」**。

策略的責任不是預測未來，  
而是 **在特定條件下，提出「如果……那麼……」的可檢驗假設**。

---

## 第 1 章｜STRATEGY_UNIVERSE 的治理位階與適用範圍

### 1.1 文件位階
- 治理等級：**B（策略治理級）**
- 上位文件：
  - `MASTER_ARCH`
  - `MASTER_CANON`
- 平行約束：
  - `ARCH_FLOW`
  - `RISK_COMPLIANCE`
  - `DATA_SOURCES`
- 下位文件：
  - `STRATEGY_FEATURE_INDEX`

📌 **任何策略不得凌駕風控或治理流程。**

---

### 1.2 適用範圍（Scope）
本文件規範：

- 所有可被系統生成、呈現、評估的策略
- 不論是否啟用、不論是否進入 Execution
- 含股票、期貨、選擇權（僅分類，不授權下單）

📌 **只要被稱為「策略」，就受本文件約束。**

---

## 第 2 章｜策略在 TAITS 中的法律地位

### 2.1 策略 ≠ 訊號 ≠ 下單
在 TAITS 中：

- **策略（Strategy）**：  
  一組結構化假設與前提條件
- **訊號（Signal）**：  
  Feature 或 Evidence 的狀態描述
- **下單（Order）**：  
  人類裁決後的執行行為

📌 策略 **永遠不能直接產生 Order**。

---

### 2.2 策略的唯一合法輸出
策略 **只能輸出**：

- Strategy Hypothesis
- 適用 Universe
- 前提條件（Assumptions）
- 失效條件（Invalidation Conditions）
- 風險型態描述（非數值）

📌 **缺失效條件的策略，制度上不成立。**

---

### 2.3 策略與 Canonical Flow 的位置
策略僅能存在於：

- **L8｜Strategy & Universe**

策略 **不得**：
- 介入 L6 Regime 判定
- 介入 L7 Risk 否決
- 介入 L9 Governance Gate

📌 **策略是被審查的對象，不是審查者。**

---

## 第 3 章｜策略白名單與分類總則（Whitelist & Taxonomy）

### 3.1 白名單制度
TAITS 採用 **策略白名單制度**：

- 列於本文件 → 可被生成
- 未列於本文件 → 不得出現於系統

📌 **不存在「實驗性但未列管」的策略。**

---

### 3.2 策略分類主軸（高階）
策略分類以「**市場行為假設**」為主軸，而非技術指標：

1. **趨勢型（Trend-following）**
2. **均值回歸型（Mean Reversion）**
3. **區間 / 震盪型（Range-bound）**
4. **動能 / 突破型（Momentum / Breakout）**
5. **事件驅動型（Event-driven）**
6. **結構 / 套利型（Structural / Arbitrage）**
7. **風險管理輔助型（Risk Overlay）**

📌 分類是為了 **禁用與適用判定**，不是績效比較。

---

### 3.3 策略共通治理欄位（Mandatory Fields）
所有策略，**不論類型**，必須定義：

- Strategy ID
- 分類（Category）
- 適用 Regime
- 禁用 Regime
- 所需 Evidence 類型
- 關鍵假設
- 失效條件
- 已知風險型態

📌 缺任一欄位 → **策略不可被引用**。

---

（STRATEGY_UNIVERSE · PART 1 結束）

PART 2｜趨勢・動能・均值回歸・區間策略（治理對齊）

## 第 4 章｜趨勢型 / 動能型 / 突破型策略（Trend / Momentum / Breakout）

### 4.1 治理前提（Governance Premise）
本類策略的核心假設為：
> **價格行為在特定市場狀態下具有延續性或加速性。**

📌 治理重點不是「抓到趨勢」，  
📌 而是 **何時不應該使用趨勢策略**。

---

### 4.2 趨勢型策略（Trend-following）

**Strategy ID**：`STR_TREND_BASE`

**適用 Regime**：
- 趨勢明確
- 波動具方向性

**禁用 Regime**：
- 高噪音震盪
- 事件密集但未消化

**必要 Evidence 類型**：
- 趨勢結構 Evidence
- 成交結構一致性

**核心假設**：
- 趨勢尚未被破壞

**失效條件（必須）**：
- 結構性反轉
- Evidence 衝突上升

**已知風險型態**：
- 假突破
- 趨勢末端追高

---

### 4.3 動能 / 突破型策略（Momentum / Breakout）

**Strategy ID**：`STR_MOM_BREAK`

**適用 Regime**：
- 波動擴張
- 流動性集中

**禁用 Regime**：
- 低流動性
- Regime 不穩定

**必要 Evidence 類型**：
- 波動擴張 Evidence
- 成交量放大

**核心假設**：
- 新資訊正在被快速定價

**失效條件**：
- 成交量未延續
- 價格快速回落區間

**已知風險型態**：
- 追高殺低
- 流動性瞬間消失

---

## 第 5 章｜均值回歸 / 區間震盪策略（Mean Reversion / Range）

### 5.1 治理前提
本類策略的核心假設為：
> **價格偏離常態後，會回歸至結構中心。**

📌 在趨勢市場使用均值回歸，  
📌 本身即是治理風險。

---

### 5.2 均值回歸策略（Mean Reversion）

**Strategy ID**：`STR_MEAN_REV`

**適用 Regime**：
- 低趨勢強度
- 結構穩定震盪

**禁用 Regime**：
- 強趨勢
- 結構破壞中

**必要 Evidence 類型**：
- 偏離度 Evidence
- 波動收斂

**核心假設**：
- 偏離屬於噪音而非新趨勢

**失效條件**：
- 偏離持續擴大
- Regime 轉為趨勢

**已知風險型態**：
- 接刀風險
- 趨勢反轉誤判

---

### 5.3 區間震盪策略（Range-bound）

**Strategy ID**：`STR_RANGE`

**適用 Regime**：
- 明確價格區間
- 成交量穩定

**禁用 Regime**：
- 區間被突破
- 事件風險升高

**必要 Evidence 類型**：
- 區間邊界 Evidence
- 成交衰竭

**核心假設**：
- 市場缺乏突破動機

**失效條件**：
- 區間邊界被有效突破

**已知風險型態**：
- 偽區間
- 事件突發突破

---

## 第 6 章｜策略使用的共通治理限制（Cross-Strategy Constraints）

### 6.1 策略互斥原則
- 趨勢型 與 均值回歸型：
  - 不得在同一 Snapshot 同時啟用

📌 若同時生成 → **Evidence 衝突過高，需降級或否決**。

---

### 6.2 策略密度限制
- 單一標的：
  - 同時呈現策略數量需受限
- 策略過多：
  - 本身即為不確定性訊號

📌 **多策略 ≠ 多信心**。

---

### 6.3 策略與 Evidence 的硬性關係
- 無對應 Evidence → 策略不得生成
- Evidence 衰退 → 策略需重新評估

📌 策略不能「撐著用」。

---

（STRATEGY_UNIVERSE · PART 2 結束）

PART 3｜事件驅動 × 結構型 × 風險輔助策略（最終閉環）

## 第 7 章｜事件驅動型與結構 / 套利型策略（Event / Structural）

### 7.1 事件驅動型策略（Event-driven）

**治理前提**  
事件驅動策略的核心假設為：
> **市場尚未完全消化已發生或即將發生的公開事件。**

📌 事件策略不是「賭消息」，  
📌 而是對 **已知事實的反應速度差**。

---

**Strategy ID**：`STR_EVENT`

**適用 Regime**：
- 事件密集期
- 波動擴張但結構未破壞

**禁用 Regime**：
- 資料延遲不明
- 事件資訊不對稱嚴重

**必要 Evidence 類型**：
- 公告時間戳 Evidence
- 價格反應延遲 Evidence

**核心假設**：
- 市場反應尚未完成

**失效條件**：
- 價格已完全反應
- 事件影響被修正

**已知風險型態**：
- 事件誤讀
- 延遲資訊

---

### 7.2 結構 / 套利型策略（Structural / Arbitrage）

**治理前提**  
結構型策略假設：
> **不同市場、商品或合約之間存在可解釋的結構關係。**

📌 結構 ≠ 免費利潤，  
📌 結構失效通常伴隨 **系統性風險**。

---

**Strategy ID**：`STR_STRUCT_ARB`

**適用 Regime**：
- 結構穩定
- 相關性高

**禁用 Regime**：
- 結構破裂
- 流動性失衡

**必要 Evidence 類型**：
- 結構關係 Evidence
- 偏離合理區間 Evidence

**核心假設**：
- 結構關係仍然成立

**失效條件**：
- 結構長期偏離
- 相關性瓦解

**已知風險型態**：
- 結構突然失效
- 系統性連鎖反應

---

## 第 8 章｜風險管理輔助策略（Risk Overlay）

### 8.1 Risk Overlay 的制度定位
風險輔助策略不是 Alpha 來源，  
而是 **保護系統不犯致命錯誤的安全層**。

📌 Overlay **永遠不能推動交易，只能限制交易**。

---

### 8.2 常見 Risk Overlay 類型

#### 8.2.1 波動率過濾（Volatility Filter）

**Strategy ID**：`STR_RISK_VOL_FILTER`

- 功能：
  - 禁止在極端波動下交易
- 禁用條件：
  - 不存在（Overlay 永遠可用）

---

#### 8.2.2 流動性門檻（Liquidity Gate）

**Strategy ID**：`STR_RISK_LIQ_GATE`

- 功能：
  - 禁止在流動性不足標的交易
- 治理要求：
  - 與 DATA_SOURCES 對齊

---

#### 8.2.3 相關性與集中度限制（Correlation / Concentration）

**Strategy ID**：`STR_RISK_CORR_LIMIT`

- 功能：
  - 限制隱性集中風險
- 治理要求：
  - 與 RISK_COMPLIANCE 協同

---

### 8.3 Overlay 的權限邊界
Overlay **可以**：
- 禁止策略啟用
- 限制參數上限

Overlay **不得**：
- 產生方向
- 替代 Risk / Compliance 否決

📌 Overlay 是保險絲，不是煞車系統。

---

## STRATEGY_UNIVERSE 最終宣告（Closing）

在 TAITS 中，  
策略不是越多越好，  
而是 **越受控越好**。

如果一套系統：
- 容許策略自行行動
- 允許策略繞過風控
- 讓策略用績效為自己辯護

那它終將在某一次錯誤中，  
把所有累積的優勢一次吐回市場。

> **真正成熟的策略系統，  
> 不是找到最多機會，  
> 而是清楚知道：  
> 哪些時候不該出手。**

---

（STRATEGY_UNIVERSE · PART 3 完成）
