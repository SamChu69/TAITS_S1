# TAITS_全系統架構藍圖（FULL_ARCH）__251218.md

> doc_key：FULL_ARCH  
> 治理等級：A（全系統架構全景藍圖）  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live-Ready）  
> 狀態：ACTIVE（Only-Add｜只能新增不可縮水）  
> 最後更新：2025-12-18（Asia/Taipei）

---

## 0. 文件定位（Architecture Blueprint）

本文件定義 **TAITS（Taiwan Alpha Intelligence Trading System）之「全系統架構藍圖」**，  
其目標是：

- 清楚劃分 **模組邊界（Boundaries）**
- 明確定義 **責任歸屬（Responsibilities）**
- 確保 **策略、風控、執行彼此解耦**
- 為未來擴充（新市場 / 新產品 / 新交易單位）保留空間

📌 本文件回答的是「**系統是怎麼被拆解與組裝的**」，  
而不是「策略細節或參數」。

---

## 1. TAITS 架構總覽（Top-Level View）

TAITS 採用 **多層、可治理、可演進** 的模組化架構，核心層級如下：

[ Governance Layer ]
↓
[ Architecture Layer ]
↓
[ Data Layer ]
↓
[ Strategy Layer ]
↓
[ Risk & Compliance Layer ]
↓
[ Execution Layer ]
↓
[ Ops / UI Layer ]

yaml
複製程式碼

---

## 2. Governance Layer（治理層）

### 2.1 職責
- 文件權威與索引
- 版本與審計
- AI 行為限制
- 開發與部署規則

### 2.2 核心文件
- TAITS_文件索引總表
- MASTER_ARCH
- GitHub 存檔規則
- Beginner Rules

📌 治理層對 **所有下層具有否決權**。

---

## 3. Architecture Layer（架構層）

### 3.1 職責
- 定義模組邊界
- 管理資料與決策流向
- 防止跨層耦合

### 3.2 關鍵原則
- 單一職責（Single Responsibility）
- 明確輸入與輸出
- 不允許策略層侵入 Execution

---

## 4. Data Layer（資料層）

### 4.1 資料來源
- 官方資料優先（TWSE / TPEX / 券商）
- 多層備援（Fallback）

### 4.2 資料型態
- Raw Data（原始）
- Normalized Data（標準化）
- Feature Data（特徵）
- Snapshot / Evidence（回放）

### 4.3 不可違反
- 原始資料不可修改
- 資料處理需可重現
- 所有轉換需留 Log

---

## 5. Strategy Layer（策略層）

### 5.1 定位
- 策略負責「**判斷與建議**」
- 不負責「執行」

### 5.2 特性
- 多策略並存
- 以 Regime 為結構
- 清楚標註交易單位：
  - 零股（Odd Lot）
  - 整股（Round Lot）
  - 混合（Hybrid）

### 5.3 輸出
- 策略訊號
- 置信度
- 前提條件

---

## 6. Risk & Compliance Layer（風控與合規層）

### 6.1 職責
- 交易前審查
- 即時否決
- 事後稽核

### 6.2 核心能力
- Regime 不符否決
- 資金/部位限制
- 市場異常保護
- Kill Switch

📌 本層具有 **最高否決權（Veto Power）**。

---

## 7. Execution Layer（執行層）

### 7.1 定位
- 僅負責「**如何執行**」
- 不決定「是否交易」

### 7.2 來源
- 策略訊號（已通過風控）
- 人類確認（必要時）

### 7.3 限制
- 僅能透過核准 API（富邦 TradeAPI）
- 嚴禁策略或 AI 直接下單

---

## 8. Ops / UI Layer（維運與介面）

### 8.1 Ops（維運）
- 部署
- 監控
- 故障演練
- 回放支援

### 8.2 UI
- 狀態可視化
- 風控提示
- 防呆顯示
- 決策回溯

---

## 9. 環境分級（Execution Context）

TAITS 支援多種執行環境（由治理層控制）：

- Research / Sandbox
- Backtest
- Simulation
- Paper Trading
- Live-Ready（未啟用）

---

## 10. 擴充與演進原則

- 可新增：
  - 新策略
  - 新資料源
  - 新交易單位
- 不可：
  - 破壞層級邏輯
  - 繞過風控
  - 寫死官方規則

---

## 11. 一句話總結

> **TAITS 的強大，  
不是來自某一個策略，  
而是來自清楚、可治理、不可跳層的系統架構。**

---

（End of FULL_ARCH）
