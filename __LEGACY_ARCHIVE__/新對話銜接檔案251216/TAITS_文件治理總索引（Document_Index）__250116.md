# TAITS_文件治理總索引（Document_Index）__250116.md

> doc_key：DOCUMENT_INDEX  
> 治理等級：A（治理中樞｜僅次於 MASTER_ARCH）  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live）  
> 版本狀態：ACTIVE  

---

## 0. 文件定位（治理中樞）

本文件為 **TAITS（Taiwan Alpha Intelligence Trading System）之文件治理中樞（Single Source of Truth）**。

其職責不是「列文件清單」，而是：

- 定義 **哪些文件具有治理效力**
- 定義 **文件之間的裁決順序**
- 定義 **AI 與系統必須服從的制度範圍**
- 作為 **制度索引強制載入機制** 的實體依據

📌 **任何未列入本 Index 的文件，在治理上視為不存在。**

---

## 1. 本文件的法律地位

### 1.1 治理效力

- 本文件具有 **系統治理效力**
- 僅次於：
  - `MASTER_ARCH｜TAITS_母體總憲法與核心鐵律`
- 高於：
  - 所有架構說明
  - 所有策略文件
  - 所有流程與操作文件

### 1.2 裁決角色

當文件、流程、策略、AI 推論之間出現衝突時：

> **本文件負責「指出誰有資格裁決」，  
而不是親自裁決內容。**

實際內容裁決，依治理等級執行。

---

## 2. 治理等級定義（A–G）

TAITS 將所有文件分為七個治理等級，  
**等級越高，否決權越強。**

### A 級｜母體與治理憲法
- 系統存在的根本理由
- 永久鐵律
- 不得被演化突破

### B 級｜系統總架構與 Canonical Flow
- 定義系統「怎麼運作」
- 不得跳步、合併或倒置

### C 級｜資料、證據與決策前置條件
- 定義「什麼資料可以開始思考」
- 資料不足即必須降級行為

### D 級｜策略、研究與方法論
- 允許演進
- 但永遠不可直連下單

### E 級｜風控、合規與否決權
- 對任何層級具備最高否決力
- 不因績效而退讓

### F 級｜操作、部署與版本治理
- 保證系統可維運、可回溯
- 防止混亂與技術債

### G 級｜介面、教學與人機邊界
- 規範「如何使用系統」
- 不影響核心裁決邏輯

---

## 3. 文件裁決順序（Conflict Resolution）

當多份文件內容發生衝突時，裁決順序如下：

1. **A 級 >**
2. **B 級 >**
3. **C 級 >**
4. **E 級 >**
5. **D 級 >**
6. **F 級 >**
7. **G 級**

📌 注意：  
- **E 級（Risk / Compliance）具有跨級否決權**
- 即使面對 A–D 級，也可否決執行行為

---

## 4. 制度索引強制載入原則（與 Prompt 對齊）

本文件列出的所有制度文件：

- **不屬於參考資料**
- **不依賴 AI 記憶**
- 視同在每一次回覆前已完整載入

若 AI 行為違反本 Index 所列任一文件：

> 視為 **制度違反行為**，  
必須立即停止並修正。

---

## 5. TAITS 正式制度文件索引（唯一權威）

以下清單為 **TAITS 唯一正式制度索引**。

---

### 🅰 A 級｜系統母體與治理中樞

- `MASTER_ARCH`  
  → **TAITS_母體總憲法與核心鐵律**

- `DOCUMENT_INDEX`  
  → **TAITS_文件治理總索引（本文件）**

---

### 🅱 B 級｜系統總架構與 Canonical Flow

- `MASTER_CANON`  
  → **TAITS_完整總架構×總流程×全資訊體系（MASTER）**

- `ARCH_FLOW`  
  → **TAITS_系統架構與流程細化說明**

- `FULL_ARCH`  
  → **TAITS_全系統架構總覽**

---

### 🅲 C 級｜資料、證據與決策前置制度

- `DATA_UNIVERSE`  
  → **TAITS_資料來源全集（DataSources_Universe）**

- `DATA_COMPLETENESS`  
  → **TAITS_資料提供完整度前置檢查**

- `DATA_TRACEABILITY`  
  → **TAITS_資料完整紀錄與推論透明度規則**

---

### 🅳 D 級｜策略、研究與方法論

- `STRATEGY_UNIVERSE`  
  → **TAITS_策略宇宙全集（Strategy_Universe）**

- `STRATEGY_FEATURE_INDEX`  
  → **TAITS_策略特徵與因子索引**

- `RESEARCH_RULES`  
  → **TAITS_研究 / 回測 / 模擬行為規範**

---

### 🅴 E 級｜風控、合規與最高否決權

- `RISK_COMPLIANCE`  
  → **TAITS_風險控管與合規最高否決權**

- `EXECUTION_CONTROL`  
  → **TAITS_交易執行與控制規範**

- `TWSE_RULES`  
  → **TAITS_TWSE 交易規則參考彙編**

---

### 🅵 F 級｜操作、部署與版本治理

- `DEPLOYMENT_OPS`  
  → **TAITS_部署與營運流程規範**

- `VERSION_AUDIT`  
  → **TAITS_版本控管與稽核紀錄規範**

- `GITHUB_RULES`  
  → **TAITS_GitHub 儲存與版本保存規則**

- `LOCAL_ENV`  
  → **TAITS_本地執行與運算環境規範**

---

### 🅶 G 級｜介面、教學與使用行為

- `UI_SPEC`  
  → **TAITS_UI 介面與互動規格書**

- `TEACHING_RULES`  
  → **TAITS_新手與教學使用規範**

---

## 6. 檔名與版本一致性原則（索引層宣告）

- 正式文件必須：
  - 使用中文正式檔名
  - 採用時間標註（`__YYMMDD`）
- 檔名變更 **不影響 doc_key**
- doc_key 為治理唯一識別

---

## 7. Index 的變更規則

- 本文件可演進，但具備高度約束力
- 新增文件：
  - 必須先更新本 Index
  - 再產生對應制度文件
- 刪除文件：
  - 必須標註為 Deprecated
  - 不得直接消失

---

## 8. 終極治理宣告

> **在 TAITS 中，  
不是「你寫了什麼文件」重要，  
而是「哪一份文件有資格被服從」。**

---

（End of DOCUMENT_INDEX）
