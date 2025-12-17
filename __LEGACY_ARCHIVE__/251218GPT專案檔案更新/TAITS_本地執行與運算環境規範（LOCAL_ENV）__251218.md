# TAITS_本地執行與運算環境規範（LOCAL_ENV）__251218.md

> doc_key：LOCAL_ENV  
> 治理等級：A（執行環境即風控｜承接 MASTER_ARCH / EXEC_CONTROL）  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live-Ready）  
> 狀態：ACTIVE（Only-Add｜只能新增不可縮水）  
> 最後更新：2025-12-18（Asia/Taipei）

---

## 0. 文件定位（Environment = Governance）

本文件定義 **TAITS 在本地（Local）與半本地（Hybrid）環境下的執行與運算規範**。  
其目標不是效能最大化，而是確保：

- **可重現性（Reproducibility）**
- **可審計性（Auditability）**
- **可控性（Controllability）**
- **風控一致性（Risk Consistency）**

📌 在 TAITS 中：  
**執行環境是風控與治理的一部分，不是工程自由選項。**

---

## 1. 環境分級（Environment Tiers）

TAITS 將運行環境分為四級，**等級越高，限制越嚴**：

### E1｜Research / Sandbox
- 用途：研究、實驗、假設驗證
- 允許快速迭代
- **禁止**連接實盤帳戶

### E2｜Backtest / Simulation
- 用途：策略驗證、壓力測試
- 必須使用可回放資料
- **禁止**即時下單

### E3｜Paper / Dry-Run
- 用途：流程驗證、風控驗證
- 模擬真實交易流程
- 必須完整 Log

### E4｜Live-Ready
- 用途：實盤前最後準備
- 限制最嚴
- **必須人類確認**
- 尚未解鎖

📌 **禁止跳級。**

---

## 2. 作業系統與硬體基準（Baseline）

### 2.1 作業系統

- 支援：
  - Windows
  - Linux
- 建議：
  - 專用使用者帳號
  - 關閉非必要服務

---

### 2.2 硬體資源（最低建議）

- CPU：4 Core 以上
- RAM：16 GB 以上
- Storage：
  - 系統碟
  - 資料碟（必須分離）

📌 **嚴禁同一磁碟同時存放：**
- 原始資料
- 產出資料
- 憑證與金鑰

---

## 3. 使用者實際環境備註（特別標註）

> ⚠️ 本段為 **使用者個人實際環境備註**，  
> 不影響 TAITS 一般性規範，但作為新對話與新 Agent 的「預設上下文」。

- OS：Windows 11 專業版
- RAM：32 GB
- 使用情境：
  - 本地 Research / Backtest
  - 未啟用 Live
- 券商 API：
  - **以富邦證券 TradeAPI 為主**
- 交易重心：
  - **零股交易為核心**
  - 整股 / 其他商品預留未啟用

📌 此段可 **Only-Add**，不可刪除。

---

## 4. Runtime 與語言環境

### 4.1 Python Runtime

- Python 版本：
  - 必須鎖定（例：3.10.x）
- 禁止：
  - 浮動版本
  - 自動升級

---

### 4.2 套件管理

- 必須使用虛擬環境：
  - venv / conda
- 套件清單：
  - 需版本鎖定
- 每次變更：
  - 必須記錄

---

## 5. 憑證與機密管理（Security）

### 5.1 嚴格禁止

- API Key
- Token
- 帳戶資訊

❌ 寫入程式碼  
❌ 上傳 GitHub  
❌ 明文存檔  

---

### 5.2 建議做法

- 環境變數
- 加密設定檔
- OS 層級權限控管

---

## 6. 資料存放與 I/O 規範

### 6.1 資料分類

- Raw Data（只讀）
- Normalized Data
- Feature Data
- Snapshot / Evidence
- Log

---

### 6.2 存放原則

- 原始資料：
  - 不可覆寫
- 產出資料：
  - 必須版本化
- Log：
  - 不可刪除
  - 不可修改

---

## 7. 日誌（Logging）與審計（Audit）

### 7.1 必要日誌類型

- Data Ingestion Log
- Decision Log
- Risk Decision Log
- Execution Log
- System Event Log

---

### 7.2 日誌要求

- 必須包含：
  - 時間戳
  - 來源
  - 環境等級
- 不可後補

---

## 8. 失敗與異常處理

### 8.1 系統異常

- 當機
- 資料中斷
- API 失效

處理原則：
- 停止流程
- 保留狀態
- **不自動重試實盤行為**

---

### 8.2 風控異常

- 立即中止
- 觸發 Kill Switch
- 通知人類

---

## 9. 環境切換規則（Critical）

- E1 → E2：允許
- E2 → E3：需流程確認
- E3 → E4：**必須人類確認**
- 不允許跳級

---

## 10. 與其他文件的關係

- 受制於：
  - MASTER_ARCH
  - EXEC_CONTROL
  - RISK_COMPLIANCE
- 被引用於：
  - DEPLOY_OPS
  - DOCUMENT_INDEX

---

## 11. 演進與擴充原則（Only-Add）

- 可新增：
  - 新工具
  - 新硬體
- 不可：
  - 降低審計要求
  - 放寬憑證管理

---

## 12. 最終環境治理宣告

> **在 TAITS 中，  
> 不是「能不能跑得快」重要，  
> 而是「每一次跑，都能被完整解釋與回放」。**

---

（End of LOCAL_ENV）
