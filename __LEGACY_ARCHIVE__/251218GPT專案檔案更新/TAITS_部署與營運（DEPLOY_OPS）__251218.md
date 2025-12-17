# TAITS_部署與營運（DEPLOY_OPS）__251218.md

> doc_key：DEPLOY_OPS  
> 治理等級：A（部署與營運治理｜承接 EXEC_CONTROL / RISK_COMPLIANCE）  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live-Ready）  
> 狀態：ACTIVE（Only-Add｜只能新增不可縮水）  
> 最後更新：2025-12-18（Asia/Taipei）

---

## 0. 文件定位（Deployment Is Governance）

本文件定義 **TAITS 的部署、營運與日常運作治理規範**。  
在 TAITS 中：

> **部署不是把系統「跑起來」，  
而是把系統「放在正確、可控、可審計的位置」。**

📌 本文件承接：
- `EXEC_CONTROL`（執行邊界）
- `RISK_COMPLIANCE`（最高否決權）
- `LOCAL_ENV`（執行環境）

---

## 1. 環境分級與部署對應（Environment × Deployment）

TAITS 的部署必須明確標示所屬環境層級：

| 環境等級 | 用途 | 可部署內容 |
|---|---|---|
| Research | 研究實驗 | 資料、策略原型 |
| Backtest | 回測 | 回測引擎、歷史資料 |
| Simulation | 模擬 | 全流程模擬 |
| Paper | 模擬實單 | 執行流程驗證 |
| Live-Ready | 實盤前 | 僅在治理解鎖後 |

📌 **環境不同，部署權限不同，不可混用。**

---

## 2. 部署前必要檢查（Pre-Deployment Checklist）

部署前 **必須全部通過**：

1. 文件版本一致（Document Index）
2. 架構文件無衝突
3. 策略狀態明確（非 Draft）
4. 風控規則完整
5. API 權限確認
6. 日誌與回放機制存在

📌 **任一項不通過 → 禁止部署。**

---

## 3. 部署行為的嚴格限制

### 3.1 禁止事項

- 不得：
  - 在未知環境部署
  - 在未標示環境等級下運行
  - 在未記錄版本下啟動系統

---

### 3.2 部署必留資訊

每一次部署必須記錄：

- 部署時間
- 環境等級
- 文件版本組合
- 系統配置摘要

---

## 4. 營運監控（Operational Monitoring）

### 4.1 必要監控項目

- 系統狀態
- API 連線狀態
- 資料流是否中斷
- Execution 是否被觸發

---

### 4.2 異常處理原則

- 偵測異常：
  - 立即告警
- 不自動恢復實盤行為
- 需人類確認後才能繼續

---

## 5. 日誌、證據與回放（Ops Layer）

### 5.1 必留日誌

- 系統啟動 / 停止
- 部署 / 回滾
- 環境切換
- 異常事件

---

### 5.2 回放要求

- 可重建：
  - 當時系統狀態
  - 使用的文件版本
  - 生效的風控規則

---

## 6. 版本與變更管理（Change Management）

### 6.1 變更類型

- 文件變更
- 策略變更
- 環境設定變更

---

### 6.2 變更原則

- Only-Add：
  - 不可覆寫
- 重大變更：
  - 必須記錄
  - 必須可回滾

---

## 7. Live-Ready 特別規範（尚未啟用）

📌 目前 TAITS **未進入 Live 狀態**。

當未來準備啟用 Live：

- 需：
  - 完整審查
  - 人類核准
  - 獨立文件解鎖

---

## 8. 與其他文件的關係

- 受制於：
  - RISK_COMPLIANCE
  - EXEC_CONTROL
  - LOCAL_ENV
- 被引用於：
  - DOCUMENT_INDEX

---

## 9. 演進與擴充原則（Only-Add）

- 可新增：
  - 新環境層級
  - 新部署工具
- 不可：
  - 降低監控要求
  - 跳過治理流程

---

## 10. 一句話總結

> **在 TAITS 中，  
> 能不能部署，  
> 和能不能交易一樣重要。**

---

（End of DEPLOY_OPS）
