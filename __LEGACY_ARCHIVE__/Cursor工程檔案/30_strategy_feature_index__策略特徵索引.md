<!--
doc_key: 30_strategy_feature_index
governance_state: Freeze v1.0
change_policy: Only-Add
engineering_layer: Engineering Translation (Non-Canonical)
source_batch: Batch 4
-->

# 30_strategy_feature_index__策略特徵索引.md

---

## 一、文件定位（Engineering Translation）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）**  
於 **Batch 4（Architecture / Strategy / Data）** 中之：

> **策略特徵索引（Strategy Feature Index）工程定義檔**

本檔目的在於：
- 將 Canonical 中對「策略差異、策略行為、策略屬性」的隱含描述
- 轉譯為 **可被工程、治理、風控一致引用的「策略特徵索引結構」**
- 作為策略比較、審閱、風險評估與治理判斷的共同語義基準

---

## 二、治理前提（不可違反）

- GOVERNANCE_STATE = **Freeze v1.0**
- 僅允許 **Only-Add**
- 不得刪減、覆寫或偷換任何 Canonical 語義
- Risk / Compliance 具最高否決權
- Canonical Flow 固定為 **MASTER_CANON（L1–L11）**

---

## 三、策略特徵索引的治理位階說明

### 3.1 策略特徵索引的定位

在 TAITS 中：

> **策略特徵索引**  
> 是用於描述「策略在工程與治理層面上具有哪些可辨識特性」的結構化索引。

其核心用途在於：
- 讓不同策略能以 **一致維度** 被理解與比較
- 防止策略因描述不清而產生治理與風控誤判
- 支援策略生命週期、風險控管與治理審閱的判斷基礎

### 3.2 策略特徵索引不是什麼（防誤讀）

策略特徵索引 **不是**：
- 策略績效指標
- 策略優劣評分
- 策略選擇或排序邏輯
- 投資建議或交易指令

---

## 四、策略特徵索引之核心特徵維度

以下特徵維度屬於 **工程語義索引**，  
不代表策略實作內容。

---

### 4.1 結構性特徵（Structural Features）

用於描述策略的基本結構屬性，例如：
- 單一標的 / 多標的
- 單策略 / 組合策略
- 靜態規則 / 動態調整

---

### 4.2 時間特徵（Temporal Features）

用於描述策略在時間上的行為特性，例如：
- 操作頻率區間
- 持倉週期型態
- 訊號更新節奏

---

### 4.3 資料依賴特徵（Data Dependency Features）

用於描述策略所依賴的主要資料型態，例如：
- 價量資料
- 基本面資料
- 事件／新聞資料
- 複合資料來源

---

### 4.4 風險行為特徵（Risk Behavior Features）

用於描述策略風險行為的工程語義，例如：
- 波動暴露傾向
- 槓桿敏感度
- 尾端風險特性
- 回撤容忍假設

---

### 4.5 執行敏感特徵（Execution Sensitivity Features）

用於描述策略對執行條件的敏感性，例如：
- 流動性依賴程度
- 成交滑價敏感性
- 下單時機依賴性

---

## 五、策略特徵索引與其他工程檔之關係

- 本文件：
  - 建立策略「可被描述的共同語言」
- 與 #27（策略宇宙）：
  - 不改變宇宙邊界
- 與 #28（策略分類）：
  - 提供分類後的細部描述維度
- 與 #29（策略生命週期）：
  - 不影響狀態轉換規則

---

## 六、工程責任邊界（非常重要）

### 6.1 本檔負責的內容

- 定義策略特徵的描述維度
- 提供治理、風控、審閱使用的一致索引語義
- 支援策略比較與審計理解

### 6.2 本檔不負責的內容

- 不定義任何特徵計算方式
- 不定義策略邏輯或演算法
- 不產生策略評分或建議
- 不影響策略是否可執行

---

## 七、與下游工程檔之關係

本文件為以下工程檔提供語義支援：

- `31_factor_definition_index__因子定義索引.md`
- 風險評估與治理審閱相關工程檔

下游工程檔 **不得** 以本索引作為實作或計算依據。

---

## 八、SOURCE_TAG（Canonical 來源）

- TAITS_策略特徵與因子索引（STRATEGY_FEATURE_INDEX）
- TAITS_策略宇宙全集（STRATEGY_UNIVERSE）
- TAITS_完整總架構×總流程×全資訊體系（MASTER_CANON）
- TAITS_風險與合規最高否決權（RISK_COMPLIANCE）

---

## 九、最終治理聲明

本文件：

- 不新增治理裁決權
- 不構成策略評估或選擇依據
- 不涉及任何實作或交易行為
- 僅作為 **策略特徵之工程語義索引**

---

> **輸出完成。**  
> 依工程規範，本檔完成後即停止，不延伸處理下一工程檔。
