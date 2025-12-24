<!--
doc_key: 27_strategy_universe_definition
governance_state: Freeze v1.0
change_policy: Only-Add
engineering_layer: Engineering Translation (Non-Canonical)
source_batch: Batch 4
-->

# 27_strategy_universe_definition__策略宇宙定義.md

## 一、文件定位（工程層）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）**  
於 **Batch 4（Architecture / Strategy / Data）** 中之：

> **策略宇宙（Strategy Universe）工程定義檔**

本檔屬於 **工程轉譯層（Engineering Translation）**，  
其目的在於將上游 Canonical 中「策略適用範圍」與「標的集合」概念，  
轉譯為 **可被系統、策略模組與風控模組一致引用的結構化定義**。

---

## 二、治理前提（不可違反）

- GOVERNANCE_STATE = **Freeze v1.0**
- 僅允許 **Only-Add**
- 不得修改、重寫或推翻任何 Canonical 語義
- Risk / Compliance 具最高否決權
- Canonical Flow 固定為 **MASTER_CANON（L1–L11）**

---

## 三、策略宇宙之治理位階說明

### 3.1 策略宇宙的治理定位

「策略宇宙」在 TAITS 中的定位為：

> **策略可作用之標的集合與市場範圍的治理級定義**

其用途在於：

- 明確界定「哪些標的 *可以* 被策略考慮」
- 防止策略模組越權使用未授權市場或標的
- 作為風險、合規、資料品質的共同交集基礎

### 3.2 明確不是什麼（防誤讀）

策略宇宙 **不是**：

- 個別策略的選股結果  
- 即時交易清單  
- 策略績效優化工具  
- 下單或倉位配置邏輯  

---

## 四、策略宇宙的結構性定義

### 4.1 核心構成元素

策略宇宙由以下結構元素組成：

1. **市場層級（Market Scope）**
   - 例如：TWSE、TPEX、期貨、選擇權等
2. **資產類型（Asset Class）**
   - 股票、ETF、期貨、衍生性商品等
3. **標的集合條件（Universe Eligibility）**
   - 上市狀態
   - 交易可得性
   - 合規可交易性
4. **排除條件（Exclusion Rules）**
   - 停牌
   - 合規禁止
   - 資料不可用或品質不足

---

## 五、策略宇宙與 Canonical Flow 的關係

### 5.1 與 L3–L4 的關係

- 策略宇宙為 **策略生成（L4）之前的前置治理條件**
- 未通過策略宇宙定義的標的：
  - 不得進入策略評估
  - 不得進入回測、模擬或實盤流程

### 5.2 與 L11（合法性）的關係

- 策略宇宙 **必須符合 L11 合法性前提**
- 若任一標的違反：
  - 市場法規
  - 合規限制
  - Risk / Compliance 否決條件  
  → 該標的自動不屬於策略宇宙範圍

---

## 六、工程責任邊界（非常重要）

### 6.1 本檔負責的內容

- 定義「策略宇宙是什麼」
- 定義其結構、治理位階與使用邊界
- 提供下游工程檔（#28–#31）一致引用的語義基礎

### 6.2 本檔不負責的內容

- 不定義策略邏輯
- 不定義選股演算法
- 不定義因子計算方式
- 不處理即時交易或回測細節

---

## 七、與下游工程檔的關係

本文件為以下工程檔之 **上游語義來源**：

- `28_strategy_classification_schema__策略分類架構.md`
- `29_strategy_lifecycle_states__策略生命週期狀態.md`
- `30_strategy_feature_index__策略特徵索引.md`
- `31_factor_definition_index__因子定義索引.md`

上述檔案 **不得** 推翻或擴張本檔所定義之策略宇宙邊界。

---

## 八、SOURCE_TAG（來源錨定）

本工程轉譯內容來源對齊以下 Canonical 母檔：

- TAITS_策略宇宙全集（STRATEGY_UNIVERSE）
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）
- TAITS_系統架構與流程細化說明（ARCH_FLOW）
- TAITS_文件索引與治理對照表（DOCUMENT_INDEX）

---

## 九、最終治理聲明

本文件：

- 不新增任何治理權力
- 不改變任何既有 Canonical 條文
- 不構成技術實作指引
- 僅作為 **策略宇宙之工程層定義與語義錨定**

---

> **輸出完成。**
>  
> 依工程規範，本檔完成後即停止，不延伸處理下一工程檔。
