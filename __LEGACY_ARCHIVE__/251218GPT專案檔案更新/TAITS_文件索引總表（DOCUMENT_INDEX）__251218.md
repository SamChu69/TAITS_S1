# TAITS_文件索引總表（DOCUMENT_INDEX）__251218.md

> doc_key：DOCUMENT_INDEX  
> 治理等級：A+（全 Repo Canon 索引｜最高一致性來源）  
> 適用範圍：TAITS 全系統文件  
> 狀態：ACTIVE（Only-Add｜只能新增不可縮水）  
> 最後更新：2025-12-18（Asia/Taipei）

---

## 0. 文件定位（Single Source of Truth）

本文件是 **TAITS 全 Repo 的「唯一文件權威索引」**。  
其目的在於：

- 定義 **哪些文件存在**
- 定義 **每份文件的治理等級與用途**
- 定義 **跨文件的優先順序**
- 防止：
  - 文件漂移
  - 新對話誤讀
  - AI / 人類引用錯誤

📌 **任何不在本索引中的文件，不具 Canon 身分。**

---

## 1. 文件治理總原則（不可違反）

### 1.1 索引即權威

- 文件是否有效：
  - 以是否列於本索引為準
- 文件是否衝突：
  - 依治理等級裁決

---

### 1.2 Only-Add 原則

- 可新增文件
- 不可：
  - 刪除既有文件
  - 變更既有文件定位
  - 降低既有文件治理等級

---

### 1.3 命名與版本規範（強制）

- 檔名必須包含：
  - 文件用途
  -（如適用）產品 / 市場
  - 日期版本（YYMMDD）
- 例：
  - `TAITS_策略宇宙全集（STRATEGY_UNIVERSE）_股票Stock__251218.md`

---

## 2. 全域優先順序（Conflict Resolution Order）

發生任何衝突時，依以下順序裁決（由高到低）：

1. **RISK_COMPLIANCE**
2. **OFFICIAL_REF**
3. **MASTER_VERSION / MASTER_ARCH**
4. **ARCH_FLOW**
5. **EXEC_CONTROL**
6. **STRATEGY_UNIVERSE**
7. **FEATURE_INDEX**
8. **UI_SPEC**
9. **DEPLOY_OPS**
10. **LOCAL_ENV**
11. 其他輔助文件

---

## 3. Canon 文件總覽（最新完整）

### 3.1 架構與總覽（Architecture / Master）

| 編號 | doc_key | 檔案 |
|---|---|---|
| 01 | README | `README.md` |
| 02 | AI_RULES | `docs/TAITS_AI規則全集（AI_RULES）__251218.md` |
| 03 | CHECKLIST | `docs/TAITS_一致性與審查清單（CHECKLIST）__251218.md` |
| 04 | MASTER_ARCH | `docs/architecture/TAITS_主架構總覽（MASTER_ARCH）__251218.md` |
| 05 | ARCH_FLOW | `docs/architecture/TAITS_架構與流程總覽（ARCH_FLOW）__251218.md` |
| 06 | MASTER_VERSION | `docs/architecture/TAITS_完整總架構與全資訊體系（MASTER_VERSION）__251218.md` |

---

### 3.2 資料與策略（Data / Strategy）

| 編號 | doc_key | 檔案 |
|---|---|---|
| 07 | DATASOURCE_UNIVERSE | `docs/datasources/TAITS_資料來源宇宙（DATASOURCE_UNIVERSE）__251218.md` |
| 08 | STRATEGY_UNIVERSE | `docs/strategies/TAITS_策略宇宙全集（STRATEGY_UNIVERSE）_股票Stock__251218.md` |
| 09 | FEATURE_INDEX | `docs/strategies/TAITS_策略特徵索引（FEATURE_INDEX）_股票Stock__251218.md` |

---

### 3.3 風控、執行與制度（Risk / Execution）

| 編號 | doc_key | 檔案 |
|---|---|---|
| 10 | RISK_COMPLIANCE | `docs/risk/TAITS_風控與合規（RISK_COMPLIANCE）__251218.md` |
| 11 | OFFICIAL_REF | `docs/risk/TAITS_TWSE交易規則參考彙編（OFFICIAL_REF）__251218.md` |
| 12 | EXEC_CONTROL | `docs/execution/TAITS_執行與控制（EXEC_CONTROL）_股票Stock__251218.md` |

---

### 3.4 環境、部署與介面（Ops / UI）

| 編號 | doc_key | 檔案 |
|---|---|---|
| 13 | DEPLOY_OPS | `docs/deployment/TAITS_部署與營運（DEPLOY_OPS）__251218.md` |
| 14 | UI_SPEC | `docs/ui/TAITS_UI規範與互動設計（UI_SPEC）__251218.md` |
| 15 | LOCAL_ENV | `docs/ops/TAITS_本地執行與運算環境規範（LOCAL_ENV）__251218.md` |

---

## 4. Repo 行為規範（對人類與 AI）

### 4.1 新對話 / 新 Agent 必須先做的事

1. 讀取 `DOCUMENT_INDEX`
2. 確認 Canon 文件清單
3. 僅能依 Canon 行事

---

### 4.2 禁止行為

- 引用未列於索引的文件
- 擅自簡化 Canon 內容
- 以對話假設取代文件

---

## 5. 變更流程（文件治理）

### 5.1 新增文件（Only-Add）

- 新文件：
  - 必須加入本索引
  - 必須標示 doc_key
  - 必須定義治理等級

---

### 5.2 重大變更

- 不得覆寫舊版
- 必須新增新版本檔
- 以日期區分

---

## 6. 與工具的關係（Cursor / GPT）

- Cursor / AI：
  - 只讀 Canon
  - 忽略 Legacy
- 本索引：
  - 是 AI 行為邊界的依據

---

## 7. 最終宣告

> **如果不在 DOCUMENT_INDEX 裡，  
> 它就不是 TAITS 的一部分。**

---

（End of DOCUMENT_INDEX）
