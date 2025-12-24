<!--
doc_key: 28_strategy_classification_schema
governance_state: Freeze v1.0
change_policy: Only-Add
engineering_layer: Engineering Translation (Non-Canonical)
source_batch: Batch 4
-->

# 28_strategy_classification_schema__策略分類架構.md

---

## 一、文件定位（Engineering Translation）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）**  
於 **Batch 4（Architecture / Strategy / Data）** 中之：

> **策略分類架構（Strategy Classification Schema）工程定義檔**

本檔目的在於：
- 將 Canonical 中對「策略差異性、策略族群、策略用途」的概念
- 轉譯為 **工程層可引用、可對齊、不可混用** 的分類結構
- 作為後續策略生命週期、特徵索引、風險管理與治理審閱的共同基準

---

## 二、治理前提（不可違反）

- GOVERNANCE_STATE = **Freeze v1.0**
- 僅允許 **Only-Add**
- 不得刪減、覆寫或推翻任何 Canonical 語義
- Risk / Compliance 具最高否決權
- Canonical Flow 固定為 **MASTER_CANON（L1–L11）**

---

## 三、策略分類的治理位階說明

### 3.1 策略分類的治理定位

在 TAITS 中：

> **策略分類**  
> 是對「策略性質」與「策略責任邊界」的治理級結構化標註。

其功能在於：
- 防止不同類型策略被錯誤比較或混用
- 確保風險、合規、評估機制可依策略類型正確套用
- 提供治理與工程層一致的語義基礎

### 3.2 策略分類不是什麼（防誤讀）

策略分類 **不是**：
- 策略績效排名
- 策略優劣評估
- 策略執行優先順序
- 投資建議或操作指引

---

## 四、策略分類之核心分類維度

### 4.1 依策略目標分類（Objective Dimension）

策略可依其主要目標進行分類，例如：
- 趨勢參與型（Trend Participation）
- 區間／均值型（Range / Mean Reversion）
- 事件反應型（Event-Responsive）
- 風險控管／避險型（Risk Mitigation）

> 此分類僅為語義層，不涉及策略邏輯實作。

---

### 4.2 依策略運作頻率分類（Temporal Dimension）

策略可依其運作節奏分類，例如：
- 高頻／極短週期
- 中短期
- 中長期
- 長期／低頻

---

### 4.3 依資料依賴性分類（Data Dependency Dimension）

策略可依其主要資料來源類型分類，例如：
- 價量驅動型
- 基本面驅動型
- 事件／新聞驅動型
- 複合資料型

---

### 4.4 依風險特性分類（Risk Profile Dimension）

策略可依其風險行為特徵分類，例如：
- 波動承受型
- 防禦穩健型
- 槓桿敏感型
- 尾端風險暴露型

---

## 五、策略分類與策略宇宙之關係

- 策略分類 **不得擴張或縮減策略宇宙**
- 所有策略分類：
  - 僅能作用於 #27 定義之策略宇宙內
- 不屬於策略宇宙的標的：
  - 不得因任何分類理由而被納入

---

## 六、工程責任邊界（非常重要）

### 6.1 本檔負責的內容

- 定義策略分類的結構與維度
- 提供一致的分類語義供下游工程檔引用
- 作為治理、風控、審閱時的分類依據

### 6.2 本檔不負責的內容

- 不定義策略生成方式
- 不定義策略邏輯或公式
- 不定義回測或實盤執行細節
- 不進行策略評分或選擇

---

## 七、與下游工程檔的關係

本文件為以下工程檔之 **上游分類基準**：

- `29_strategy_lifecycle_states__策略生命週期狀態.md`
- `30_strategy_feature_index__策略特徵索引.md`
- `31_factor_definition_index__因子定義索引.md`

上述檔案 **必須遵守** 本分類架構，
不得自創衝突或未定義之分類維度。

---

## 八、SOURCE_TAG（Canonical 來源）

- TAITS_策略宇宙全集（STRATEGY_UNIVERSE）
- TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）
- TAITS_系統架構與流程細化說明（ARCH_FLOW）

---

## 九、最終治理聲明

本文件：

- 不新增治理權力
- 不改變 Canonical Flow
- 不構成任何技術實作或投資建議
- 僅作為 **策略分類之工程語義錨定**

---

> **輸出完成。**
>  
> 依工程規範，本檔完成後即停止，不延伸處理下一工程檔。
