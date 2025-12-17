# TAITS – Taiwan Alpha Intelligence Trading System

> **文件優先｜風控至上｜Regime 為核心｜AI 輔助但不可越權**

---

## 0. 專案定位（Project Positioning）

**TAITS（Taiwan Alpha Intelligence Trading System）**  
是一套為 **台灣市場（TWSE / TPEX）** 設計的：

- 文件先行（Docs-First）
- 可長期演進
- 可回放、可審計
- 以 **Regime（市場狀態）與 Risk / Compliance** 為最高優先權

的 **完整量化交易系統母體架構**。

📌 TAITS 不是 Demo、不是教學範例、不是單一策略，  
而是一套 **可實際落地、但嚴格受控的交易系統藍圖**。

---

## 1. TAITS 不解決的事（先說清楚）

TAITS **刻意不做**以下事情：

- ❌ 不追求單一神策略
- ❌ 不追求高頻或極速下單
- ❌ 不允許 AI 自主交易
- ❌ 不允許黑箱決策
- ❌ 不允許無法回放的交易

TAITS 的核心價值不是「快」，  
而是 **「每一次行為都能被解釋、被否決、被重現」**。

---

## 2. 核心設計哲學（不可動搖）

### 2.1 五大鐵律

1. **策略 ≠ 下單**
2. **Agent ≠ 策略**
3. **AI ≠ 唯一真理**
4. **Regime 高於任何訊號**
5. **Risk / Compliance 可否決一切**

---

### 2.2 Docs-First 原則

在 TAITS 中：

- 文件 > 程式碼
- Canon 文件 > 對話
- DOCUMENT_INDEX > 任何個別說法

📌 **如果文件沒有寫清楚，就視為「尚未允許」**。

---

## 3. 目前支援範圍（Current Scope）

### 3.1 市場與商品

- 市場：
  - 台灣股票（TWSE / TPEX）
- 商品：
  - 股票（Stock）

📌 其他商品（期貨、選擇權、海外市場）  
**架構已預留，但尚未啟用**。

---

### 3.2 交易單位（重要）

- 核心支援：
  - **零股（Odd Lot）**
- 預留支援：
  - 整股
  - 混合策略

📌 因零股在制度、流動性、成交行為上與整股本質不同，  
TAITS **明確將零股視為獨立治理對象**。

---

### 3.3 券商 API

- 主要執行 API：
  - **富邦證券 TradeAPI**
- 原則：
  - 僅使用官方已存在能力
  - 不假設、不模擬不存在功能

---

## 4. 系統整體結構概覽（High-Level）

Governance / Canon Documents
↓
Architecture & Flow
↓
Data & Feature System
↓
Regime Identification
↓
Strategy Universe
↓
Risk & Compliance (Veto Power)
↓
Execution Control (Authorized Only)
↓
Logging / Audit / Replay
↓
UI / Ops / Human-in-the-Loop

yaml
複製程式碼

📌 **任何一層都可以否決下游行為**。

---

## 5. Canon 文件體系（非常重要）

TAITS 的一切定義，**只存在於 Canon 文件中**。

### 5.1 Canon 文件入口

👉 **唯一權威索引：**
docs/TAITS_文件索引總表（DOCUMENT_INDEX）__251218.md

yaml
複製程式碼

- 所有有效文件
- 所有治理等級
- 所有優先順序  
**全部以該索引為準**。

---

### 5.2 為什麼這麼多文件？

因為 TAITS 要解決的不是：

>「怎麼下單？」

而是：

>「在什麼情況下，  
> 為什麼可以下、  
> 為什麼不可以下？」

---

## 6. 新對話 / 新 AI / 新 Agent 使用方式

### 6.1 新對話啟動規則

任何新對話開始，AI 必須：

1. 讀取 DOCUMENT_INDEX
2. 載入所有 Canon 文件
3. 宣告依 Canon 行事

📌 **不需要重新說明專案內容**，  
文件即專案本身。

---

### 6.2 使用者角色定位

- 使用者（你）：
  - 架構決策者
  - 最終控制權持有人
- AI：
  - 嚴格受控的輔助系統
  - 不可越權
  - 不可偷工減料

---

## 7. 版本策略與未來演進

### 7.1 Only-Add 原則

- 允許：
  - 新文件
  - 新版本
- 不允許：
  - 覆寫
  - 縮水
  - 偷刪內容

---

### 7.2 未來擴充方向（尚未啟用）

- 整股專用策略宇宙
- 其他商品（期貨 / 選擇權）
- 多市場（非台股）
- Live Trading（需獨立解鎖）

---

## 8. 重要提醒（給未來的你）

> 如果某一天你覺得  
> 「這套系統怎麼這麼麻煩？」

那代表你正在站在一個：

- 很容易犯錯
- 很容易失控
- 很容易被市場教育

的時間點。

📌 **TAITS 的存在，就是為了在那一刻，把你拉住。**

---

## 9. 最終宣告

> **TAITS 不是為了「今天賺多少」，  
> 而是為了「五年後，你還知道自己為什麼能活著」。**

---

（End of README）
