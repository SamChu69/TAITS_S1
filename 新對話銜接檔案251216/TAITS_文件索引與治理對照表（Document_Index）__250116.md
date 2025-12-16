# TAITS_文件索引與治理對照表（Document_Index）__250116.md

> doc_key：DOCUMENT_INDEX  
> 治理等級：A（全文件索引母表｜最高權威之一）  
> 適用範圍：TAITS 全系統  
> 版本狀態：LOCKED（僅可由人類主權覆寫）

---

## 0. 文件定位（Index as Law）

本文件為 **TAITS 全專案的「文件索引母表」**，  
其法律地位等同於「憲法附表」。

在 TAITS 中：

> **文件是否存在、是否有效、是否具治理效力，  
一律以本 Index 為準。**

📌 若某文件 **未被列入本 Index**：
- 視為「非正式文件」
- **不得被系統、Agent、治理流程引用**

---

## 1. Document_Index 的核心職責（不可替代）

Document_Index 同時承擔四個角色：

1. **唯一文件白名單**
2. **doc_key ↔ 中文檔名 對照表**
3. **治理等級與效力來源**
4. **版本有效性裁決依據**

📌 本文件高於：
- 單一文件內容
- 檔名與路徑
- 工具或 AI 的假設

---

## 2. 文件識別規則（doc_key 為唯一識別）

### 2.1 doc_key 定義

- doc_key 為：
  - 全大寫
  - 底線分隔
- **全系統唯一**
- 一經發布：
  - 不得重用
  - 不得變更語意

📌 **文件之間的引用，只能使用 doc_key。**

---

### 2.2 檔名與 doc_key 的關係

- 檔名：
  - 給人閱讀
  - 可調整、可版本化
- doc_key：
  - 給治理、索引、Prompt 使用
  - **不可隨意變更**

---

## 3. 治理等級定義（Authority Levels）

| 等級 | 說明 | 覆寫權限 |
|-----|-----|---------|
| A | 母體 / 索引 | 人類主權 |
| B | Canonical / 架構 | 人類主權 |
| C | 營運 / 治理 | 嚴格審查 |
| D | 策略 / 特徵 | Only-Add |
| E | 風控 / 合規 | 人類主權 |
| F | 教學 / 操作 | 彈性 |

📌 **低等級文件不得影響高等級裁決。**

---

## 4. 正式文件清單（Authoritative List）

### 4.1 A 級（最高）

| doc_key | 中文檔名（最新版本） |
|-------|------------------|
| MASTER_ARCH | TAITS_MASTER_ARCHITECTURE |
| DOCUMENT_INDEX | TAITS_文件索引與治理對照表 |

---

### 4.2 B 級（Canonical / 架構）

| doc_key | 中文檔名 |
|-------|---------|
| MASTER_CANON | TAITS_完整總架構×總流程×全資訊體系 |
| ARCH_FLOW | TAITS_系統架構與流程細化說明 |
| FULL_ARCH | TAITS_全系統架構總覽 |

---

### 4.3 C 級（營運 / 治理）

| doc_key | 中文檔名 |
|-------|---------|
| DATA_UNIVERSE | TAITS_資料來源全集 |
| UI_SPEC | TAITS_使用者介面與人機決策規範 |
| DEPLOY_OPS | TAITS_部署、營運與日常運作規範 |
| VERSION_AUDIT | TAITS_版本控管、稽核與可追溯治理規範 |

---

### 4.4 D 級（策略 / 分析）

| doc_key | 中文檔名 |
|-------|---------|
| STRATEGY_UNIVERSE | TAITS_策略宇宙全集 |
| STRATEGY_FEATURE_INDEX | TAITS_策略特徵與因子索引 |

---

### 4.5 E 級（風控 / 合規）

| doc_key | 中文檔名 |
|-------|---------|
| RISK_COMPLIANCE | TAITS_風險控管與合規最高否決權 |
| TWSE_RULES | TAITS_TWSE交易規則參考彙編 |
| EXECUTION_CONTROL | TAITS_交易執行與控制規範 |

---

### 4.6 F 級（操作 / 環境）

| doc_key | 中文檔名 |
|-------|---------|
| LOCAL_ENV | TAITS_本地執行與運算環境規範 |

---

## 5. 版本有效性裁決規則（Critical）

- 同一 doc_key：
  - 僅能有 **一個「最新有效版本」**
- 舊版本：
  - 自動降為「歷史參考」
  - 不得被引用於 Live 決策

📌 有衝突時：
- 以本 Index 標註為準

---

## 6. Index 更新規則（唯一入口）

- 任何新增 / 更新文件：
  - **必須同步更新本 Index**
- 未更新 Index 的文件：
  - 視為未生效

📌 **Index 未更新 = 文件不存在**

---

## 7. 與 Prompt 與 AI 的關係

- AI 行為：
  - 必須以本 Index 為文件真實來源
- AI 不得：
  - 自行假設文件存在
  - 引用未列入 Index 的內容

---

## 8. 人類主權與 Index

- 僅人類：
  - 可新增 / 移除 doc_key
  - 可調整治理等級
- 所有變更：
  - 必須產生新版本
  - 必須可追溯

---

## 9. 最終索引宣告

> **在 TAITS 中，  
文件不是因為被寫下來而存在，  
而是因為被列入 Index 才具有治理效力。**

---

（End of DOCUMENT_INDEX）
