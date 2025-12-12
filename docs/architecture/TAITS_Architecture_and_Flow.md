# TAITS_Architecture_and_Flow.md
# TAITS — 系統架構 × 運行流程（Architecture & Runtime Flow）

版本：Master / Full  
文件角色：**系統運行流程最高說明文件**  
上位文件：
- TAITS_MASTER_ARCHITECTURE.md
- TAITS_Full_System_Architecture.md

---

## 0. 文件定位（必讀）

本文件專注回答一件事：

> **TAITS 在「不同時間點」是如何被驅動、如何流動、如何做決策的。**

如果前兩份文件回答的是「是什麼」，  
那這一份回答的是「**什麼時候、先做什麼、再做什麼**」。

---

## 1. TAITS 運行模式總覽

TAITS 支援四種互斥運行模式：

| 模式 | 用途 |
|---|---|
| Research | 離線研究、因子製作 |
| Backtest | 歷史回測（事件驅動） |
| Paper | 模擬交易 |
| Live | 實盤交易（券商 API） |

⚠️ 模式之間 **不得混用狀態**

---

## 2. 系統時間軸（Time Axis）

TAITS 的運行被切成三個主要時間段：

```text
Pre-Market   → 開盤前
In-Market    → 盤中
Post-Market  → 收盤後
````

---

## 3. 開盤前流程（Pre-Market）

### 3.1 資料準備

1. 拉取最新歷史資料（TWSE / TAIFEX / Macro）
2. 驗證交易日與資料完整性
3. 更新資料庫與快取

---

### 3.2 指標與結構計算

1. 技術指標
2. 籌碼因子
3. 基本面因子（若有更新）
4. 纏論結構（分型 / 筆 / 中樞）

---

### 3.3 策略與 Agent（盤前）

1. 執行完整策略宇宙（355+）
2. Agents 彙總盤前觀點
3. Market Regime 初判

---

### 3.4 盤前輸出

* 今日市場偏向
* 可交易 Universe
* 風險提示清單

---

## 4. 盤中流程（In-Market）

### 4.1 事件驅動（Event-Driven）

事件來源：

* Tick / Bar
* 新聞 / 公告
* 期貨 / 選擇權異動

---

### 4.2 快速更新路徑（Fast Path）

1. 更新快取
2. 更新必要指標
3. 更新關鍵 Agents
4. 檢查 Regime 是否變化

---

### 4.3 決策路徑（Decision Path）

```text
策略子集
 → Agents
 → Regime
 → Fusion
 → Risk
```

⚠️ 任一環節 BLOCK → **不允許新倉**

---

### 4.4 執行

依模式：

* Backtest → 撮合引擎
* Paper → 模擬撮合
* Live → 券商 API

---

## 5. 收盤後流程（Post-Market）

1. 寫入所有交易與決策 Log
2. 更新績效與風險指標
3. 產生日報（Markdown）
4. 更新策略統計資料
5. 準備次交易日資料

---

## 6. Orchestrator 調度規則

Orchestrator 負責：

* 流程順序
* 事件觸發
* 模式隔離
* 失敗降級

任何模組 **不得自行啟動流程**。

---

## 7. 風控與熔斷流程（重要）

### 7.1 即時風控

* 曝險過高
* 流動性不足
* 異常波動

---

### 7.2 系統熔斷

觸發條件：

* 指數急殺
* 連續虧損
* API 失效
* 資料延遲

結果：

> **只允許平倉，不允許新倉**

---

## 8. 錯誤與異常處理

* 模組失效 → 隔離
* 資料中斷 → 啟用 fallback
* 風控異常 → 全系統 BLOCK

---

## 9. 稽核與可重建性

任何一天、任何一筆交易，必須能：

* 重建當時資料
* 重建策略輸出
* 重建 Agent 判斷
* 重建最終決策

---

## 10. 與其他文件的關係

* 本文件實作化 `TAITS_Full_System_Architecture.md`
* 本文件受制於 `TAITS_Risk_and_Compliance.md`
* 本文件不定義策略、不定義資料源

---

## 11. 一句話總結

> **如果你要寫 Orchestrator、排程、回測流程，
> 這一份就是你的施工圖。**

---

