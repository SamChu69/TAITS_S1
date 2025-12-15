# TAITS_MASTER_ARCHITECTURE.md
（TAITS 系統母體最高憲章｜Architecture-Locked｜Regime-First｜Risk/Governance Veto）

> 文件地位：最高權威（Constitution）
> 本文件定義 TAITS 不可違反的原則、邊界、優先序與「什麼不是 TAITS」。
> 任何策略、模組、實作、文件若與本文件衝突，一律以本文件為準。

---

## 0. 名詞與中譯（避免新對話看不懂）

- TAITS：Taiwan Alpha Intelligence Trading System（台灣阿爾法智能交易系統）
- Regime：Market Regime（市場狀態/盤勢狀態）
- Governance：Strategy Governance（策略治理）
- Permission Gate：策略權限閘門（允許/降級/人工/禁止）
- Risk / Compliance：風控與合規（具有最高否決權）
- Observe-only：僅觀察模式（不允許送單）
- Execution：下單執行（實作層能力，不屬於母體邏輯）
- Evidence Bundle：證據包（可回放、可審計的決策依據集合）

---

## 1. TAITS 的定位（這不是 Demo）

TAITS 是一套專為台灣市場（TWSE/TPEX/TAIFEX）設計、可長期演進的交易決策系統母體，其核心工作是：

1) 以多來源資料建構「可審計」的市場觀察  
2) 判定市場狀態 Regime（盤勢屬性）  
3) 在 Regime 之上，治理策略可用性（Permission Gate）  
4) 由風控/合規進行否決或降級（Veto）  
5) 產出可被人類決策採用的「建議與限制」

> TAITS 的核心不是「下單」，而是「可治理的交易決策」。

---

## 2. 不可違反的最高原則（Architecture Laws）

### 2.1 策略 ≠ 下單
- 策略層只負責：訊號、條件、適用性、風險敞口建議
- 是否下單、下單方式、拆單節奏屬於實作層（Execution Layer），必須被 Gate 約束

### 2.2 Agent ≠ 策略
- Agent（分析代理）負責：資料解讀、證據整理、假設檢查、交叉驗證
- Strategy（策略）負責：可重複規則化的訊號定義與適用條件

### 2.3 AI ≠ 唯一真理
- AI 僅能提供建議與證據彙整
- 最終結論必須可被「規則、資料、審計」支持

### 2.4 Regime 高於任何單一訊號
- 任一訊號若與 Regime 不一致，策略必須降級或禁止
- Regime 是系統級優先序

### 2.5 Risk / Compliance 具有最高否決權
- 風控/合規可否決所有策略、所有意圖、所有執行
- 任何模組不得繞過 Risk Gate

### 2.6 觀察型產品不得直接下單（你已明確要求）
下列工具在 TAITS 中定位為「市場觀察/結構證據」，不是交易標的：
- 指數期貨、個股期貨（Futures）
- 選擇權（Options）
- 融資融券（Margin/Short）
- 外資避險與部位行為（Institutional Hedging）

> 它們只能影響：Regime、Filter、Weight Adjuster、Risk Override。

### 2.7 資料不足 = 不判斷（R10）
- 當核心資料缺失、延遲或異常，系統必須回到「不判斷/僅觀察」狀態
- 任何人不得以「通靈」補齊缺口

---

## 3. 系統優先序（Priority Order）

從高到低：

1) 風控與合規（Risk/Compliance Veto）
2) 市場狀態（Regime）
3) 策略治理（Governance / Permission Gate）
4) 融合與權重（Fusion / Weighting）
5) 策略訊號（Strategy Signals）
6) 特徵/指標（Features/Indicators）
7) 原始資料（Raw Data）

> 若低層結論與高層衝突，低層必須被覆蓋或降級。

---

## 4. TAITS 的「母體文件」與「實作文件」分界

### 4.1 母體（System Mother）＝你要求的 00–12
母體回答：系統是什麼、怎麼判斷、怎麼治理、怎麼風控、怎麼驗證。

### 4.2 實作（Implementation）＝13+
實作回答：如何接券商 API、如何送單、如何部署、如何監控、如何回放。

> 實作層只能引用母體，不得改寫母體。

---

## 5. TAITS 交付標準（Definition of Done）

系統要稱為「可落地」必須同時滿足：

- 可審計：每次輸出有 evidence bundle
- 可回放：同資料快照可重建同結論
- 可治理：策略有權限與上限（Permission）
- 可否決：Risk Gate 能在工程上真實阻擋
- 可演進：版本化、變更紀錄、回滾機制完整

---

## 6. 版本與變更治理（摘要）

- 任何變更不得覆寫歷史語義
- 必須遵守版本規範與 CHANGELOG
- 沒有 Impact 說明的變更視為不合格

---

## 7. 最終宣告（Locked）

本文件一旦進入 GitHub 主幹（main），視為 TAITS 憲章封板。  
未來如需擴充，一律採用「新增附錄/新增新文件」方式，不得破壞可回放性。
