<!--
doc_key: 31_factor_definition_index
governance_state: Freeze v1.0
change_policy: Only-Add
engineering_layer: Engineering Translation (Non-Canonical)
source_batch: Batch 4
-->

# 31_factor_definition_index__因子定義索引.md

---

## 一、文件定位（Engineering Translation）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）**  
於 **Batch 4（Architecture / Strategy / Data）** 中之：

> **因子定義索引（Factor Definition Index）工程定義檔**

本檔目的在於：
- 將 Canonical 中對「因子（Factor）」之抽象描述
- 轉譯為 **工程層可被一致引用、不可混用的定義索引**
- 作為策略分析、研究、風控與治理審閱時的 **共同語義錨定**

---

## 二、治理前提（不可違反）

- GOVERNANCE_STATE = **Freeze v1.0**
- 僅允許 **Only-Add**
- 不得刪減、覆寫或偷換任何 Canonical 語義
- Risk / Compliance 具最高否決權
- Canonical Flow 固定為 **MASTER_CANON（L1–L11）**

---

## 三、因子在 TAITS 中的治理位階

### 3.1 因子的治理定位

在 TAITS 中：

> **因子（Factor）**  
> 是對「市場、標的或狀態特徵」的結構化描述單元，  
> 用於支持分析、比較與研究，但 **本身不具任何決策權力**。

因子的存在目的在於：
- 提供策略研究的分析材料
- 支援風險與特徵理解
- 作為策略構成元素之一

### 3.2 因子不是什麼（防誤讀）

因子 **不是**：
- 策略
- 交易訊號
- 下單條件
- 投資建議或預測模型

---

## 四、因子定義索引的核心結構

因子定義索引用於描述：

- 因子「是什麼」
- 因子「描述什麼性質」
- 因子「屬於哪一類語義」

而 **不描述** 因子的計算方式或使用方法。

---

## 五、因子分類之工程語義維度

以下分類屬於 **工程語義分類**，  
不代表實作層或數學模型。

---

### 5.1 價格相關因子（Price-related Factors）

- 描述價格行為或價格結構特性
- 例如趨勢、波動、區間性質

---

### 5.2 成交量相關因子（Volume-related Factors）

- 描述市場參與程度或流動性狀態
- 不代表交易活躍度判斷

---

### 5.3 基本面相關因子（Fundamental-related Factors）

- 描述企業或標的的財務與基本狀態特性
- 不構成估值或投資判斷

---

### 5.4 事件與狀態相關因子（Event / State Factors）

- 描述外部事件或內部狀態之存在性
- 不代表事件反應策略

---

### 5.5 複合型因子（Composite Factors）

- 由多種因子語義組合而成
- 組合本身不構成決策邏輯

---

## 六、因子索引與策略特徵之關係

- 因子：
  - 是策略可引用的分析元素
- 策略特徵（#30）：
  - 描述策略行為與性質
- 兩者關係：
  - **因子支援策略**
  - **不主導策略**

---

## 七、工程責任邊界（非常重要）

### 7.1 本檔負責的內容

- 定義因子的語義定位
- 建立因子分類與命名的一致性
- 提供策略研究與審閱的共同索引

### 7.2 本檔不負責的內容

- 不定義因子計算公式
- 不定義資料來源或頻率
- 不定義因子使用方式
- 不產生任何交易或執行指令

---

## 八、與下游工程檔之關係

本文件為以下工程檔之語義基礎：

- `32_data_source_catalog__資料來源目錄.md`
- `33_data_source_usage_constraints__資料來源使用限制.md`
- `34_data_quality_validation_rules__資料品質與驗證規則.md`

下游工程檔 **不得** 推翻或擴張本檔之因子定義語義。

---

## 九、SOURCE_TAG（Canonical 來源）

- TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）
- TAITS_策略宇宙全集（STRATEGY_UNIVERSE）
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）
- TAITS_系統架構與流程細化說明（ARCH_FLOW）

---

## 十、最終治理聲明

本文件：

- 不新增任何治理裁決權
- 不構成策略或投資建議
- 不涉及任何實作或交易行為
- 僅作為 **因子定義之工程語義索引**

---

> **輸出完成。**  
> 依工程規範，本檔完成後即停止，不延伸處理下一工程檔。
