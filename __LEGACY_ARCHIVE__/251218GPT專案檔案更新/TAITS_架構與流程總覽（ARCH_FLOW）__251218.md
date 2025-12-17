# TAITS_架構與流程總覽（ARCH_FLOW）__251218.md

> doc_key：ARCH_FLOW  
> 治理等級：A（架構＋流程的可落地總覽）  
> 適用範圍：TAITS 全系統（Research / Backtest / Simulation / Paper / Live-Ready）  
> 狀態：ACTIVE（Only-Add｜只能新增不可縮水）  
> 最後更新：2025-12-18（Asia/Taipei）

---

## 0. 文件定位（Architecture × Flow）

本文件負責 **把「架構（誰負責什麼）」與「流程（事情怎麼發生）」完整對齊**。  
回答以下問題：

- 資料如何進來、如何被處理？
- 策略如何形成判斷？
- 風控如何否決？
- 執行如何被允許？
- 哪些地方 **不可跳步**？

📌 本文件是 **MASTER_ARCH 與 FULL_ARCH 的流程化落地版本**，  
不是策略細節、也不是參數說明。

---

## 1. 全系統事件驅動總流程（Event-Driven Overview）

TAITS 採用 **事件驅動（Event-Driven）** 的決策與執行流程：

[ Data Event ]
↓
[ Data Validation / Normalization ]
↓
[ Feature Generation ]
↓
[ Regime Identification ]
↓
[ Strategy Evaluation ]
↓
[ Risk & Compliance Check ]
↓
[ Human-in-the-Loop (If Required) ]
↓
[ Execution Authorization ]
↓
[ Order Execution ]
↓
[ Logging / Audit / Evidence ]

yaml
複製程式碼

📌 **任何一步失敗，流程即停止，不允許自動跳過。**

---

## 2. 資料流程（Data Flow）

### 2.1 資料來源進入（Ingestion）

- 官方資料優先：
  - TWSE / TPEX
  - 券商（富邦 TradeAPI）
- 非官方資料：
  - 僅作輔助
  - 必須標註來源與可信度

### 2.2 驗證與標準化

- 檢查：
  - 時間完整性
  - 欄位完整性
  - 異常值
- 標準化：
  - 時區
  - 單位
  - 欄位命名

📌 驗證失敗 → **禁止進入策略層**。

---

## 3. 特徵工程流程（Feature Pipeline）

### 3.1 特徵生成

- 價量特徵
- 波動特徵
- 結構特徵
- 事件標記（公告、除權息等）

### 3.2 特徵治理

- 特徵需：
  - 可重現
  - 可回放
- 不允許：
  - 即時臨時特徵
  - 無法回溯的計算

---

## 4. Regime 辨識流程（Market Regime）

### 4.1 Regime 定位

- Regime 是「市場結構狀態」，非單一指標
- 常見 Regime 類型（示意）：
  - 趨勢
  - 盤整
  - 高波動
  - 事件期

### 4.2 Regime Gate（不可跳）

- 未識別 Regime：
  - **策略不得啟動**
- Regime 不符：
  - **策略輸出自動失效**

📌 Regime 是策略能否成立的「前提條件」。

---

## 5. 策略評估流程（Strategy Evaluation）

### 5.1 策略輸入

- Regime 標籤
- Feature 集
- 策略前提條件

### 5.2 策略輸出

- 訊號方向（Buy / Sell / Hold）
- 信心權重
- 交易單位標註（零股 / 整股 / 混合）
- 風險提示

📌 **策略不產生下單指令**。

---

## 6. 風控與合規流程（Risk & Compliance Gate）

### 6.1 事前風控（Pre-Trade）

- 資金限制
- 部位限制
- 流動性檢查（特別針對零股）
- Regime 相容性

### 6.2 否決邏輯

- 任一條件不符：
  - **立即否決**
  - 不進入 Execution
- 否決結果：
  - 必須記錄原因
  - 不需即時對外解釋

---

## 7. 人類介入節點（Human-in-the-Loop）

### 7.1 介入條件

- 高風險策略
- 新策略初次啟用
- 異常市場狀態
- 由治理層指定的情境

### 7.2 人類權限

- 確認
- 延後
- 否決

📌 人類否決同樣需留下審計紀錄。

---

## 8. 執行授權與下單流程（Execution Authorization）

### 8.1 授權條件（全部必須通過）

- 策略成立
- Regime 符合
- 風控通過
-（必要時）人類確認

### 8.2 下單行為

- 僅能由 Execution Layer 執行
- 僅能使用核准 API（富邦 TradeAPI）
- 不允許：
  - 策略直接下單
  - AI 繞過授權

---

## 9. 事後處理（Post-Trade）

### 9.1 日誌與證據

- 資料輸入 Log
- 決策 Log
- 風控 Log
- 下單 Log

### 9.2 回放與稽核

- 每一筆交易：
  - 必須可回放
  - 必須可解釋

---

## 10. 執行環境對應（Context Binding）

- Research / Sandbox：
  - 不連實盤
- Backtest：
  - 可回放資料
- Simulation / Paper：
  - 流程完整模擬
- Live-Ready：
  - 尚未啟用（治理解鎖後）

---

## 11. 不可接受的流程行為（Anti-Flow Patterns）

- 跳過 Regime
- 跳過風控
- 無 Log 即執行
- AI 自行決定執行

---

## 12. 一句話總結

> **TAITS 的流程不是為了「快」，  
而是為了「每一步都能被否決、被解釋、被回放」。**

---

（End of ARCH_FLOW）
