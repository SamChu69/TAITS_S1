# 📘 **TAITS_S1 — Chapters 01 to 18（Complete Integrated Edition）**

**TradingAgents AI Trading System — S1 Architecture Documentation**

---

# # **Chapter 01 — 系統理念（System Philosophy）**

TAITS_S1 的核心願景：

> **打造一套「能自己分析、自己決策、自己交易」的台股全自動智慧量化系統。**

與一般散戶程式交易完全不同。
TAITS 是大型、模組化、多層級 AI × 多策略 × 多資料源的 **完整交易平台**。

核心理念包含：

* 多策略（Multi-Strategy）
* 多模型（AI Ensemble）
* 多智能體（TradingAgents）
* 多流程保護（Sandbox → Paper → Live）
* 全自動化（Auto Trading System）
* 高可維護性（Modular Architecture）
* 高可擴充性（Plugin Strategy / Indicator）

---

# # **Chapter 02 — 系統演進（Evolution History）**

| 版本         | 特性                                                             |
| ---------- | -------------------------------------------------------------- |
| **V1**     | 單策略、手動分析、技術面初階                                                 |
| **V2**     | XQ、自動化策略、基礎回測                                                  |
| **V3**     | 雙模組（趨勢+回調）、策略濾網、GMMA 核心模型                                      |
| **S1（現行）** | **TradingAgents + AI 模型 + 多資料源 + 285 策略 + 事件驅動回測 + 富邦 API 實盤** |

S1 超越 V3.1，是正式的企業級架構版本。

---

# # **Chapter 03 — 全域架構（Global Architecture）**

```
TAITS_S1
│
├── Data Layer（資料層）
│     ├── Yahoo / TWSE / FinMind
│     ├── NLP News
│     ├── Fundamental / Chip
│     └── Cache & Validation
│
├── Indicator Layer（指標層）
│     ├── 技術指標 120+
│     ├── 籌碼指標
│     ├── 基本面特徵
│     ├── NLP 分數
│     └── AI 預測特徵
│
├── Strategy Layer（策略層）
│     ├── 285 策略模組
│     ├── Plugin Architecture
│     └── Voting Engine
│
├── TradingAgents Layer
│     ├── Technical Agent
│     ├── Chip Agent
│     ├── Fundamental Agent
│     ├── News Agent
│     ├── Sentiment Agent
│     ├── Macro Agent
│     ├── AI Agent
│     └── Risk Agent
│
├── Orchestrator（主控 AI）
│     ├── 信號整合（加權 / 投票）
│     ├── 決策（Decision Engine）
│     └── Order Plan 生成
│
├── Backtest Engine
│     ├── 事件驅動（Event-driven）
│     ├── Position Manager
│     └── Performance Report
│
├── Trading Layer
│     ├── Sandbox
│     ├── Paper Trading
│     └── Live（富邦 API）
│
└── UI Layer（Streamlit）
       ├── Dashboard
       ├── Strategy Report
       └── AI Signal View
```

---

# # **Chapter 04 — 資料層（Data Layer）**

資料來源分為 3 層 fallback：

### **第一層：Yahoo Finance**

* 最快
* 有外資 ADR、匯率、類股 index
* 但有 SSL error 可能 → 已在 S1 處理

### **第二層：TWSE OpenAPI**

* 官方資料
* 不限頻率
* 台股資料最乾淨

### **第三層：FinMind**

* 籌碼資料
* 融資券
* 財報

### **資料流程**

```
Yahoo → TWSE → FinMind → Cache → Validator → Clean DataFrame
```

---

# # **Chapter 05 — 特徵層（Feature Engineering）**

S1 特徵集包含：

### 技術指標（Trend, Momentum, Volatility…）

120+ 技術指標（EMA、MACD、GMMA、RSI、ATR、BB、KC…）

### 籌碼特徵

外資 / 投信 / 自營
集中度 / 大戶比例 / 融券 / 融資變化

### NLP 特徵

新聞情緒（sentiment）
新聞重要性（impact score）

### 基本面特徵

EPS / YOY / 毛利 / ROE / 市值 / 估值

### AI 預測特徵

Kronos / LSTM / Transformer
→ up_prob, down_prob, side_prob

---

# # **Chapter 06 — 指標層（Indicator System）**

S1 的 Indicator Manager：

* 自動發現 indicators/ 內所有 .py
* 每個指標為 class，可 plugin
* 輸出為統一 DataFrame

指標分類：

1. 趨勢（Trend）
2. 動能（Momentum）
3. 波動（Volatility）
4. 成交量（Volume）
5. K 線形態（Candle）
6. 籌碼（Chip）
7. AI 特徵（ML-based）

---

# # **Chapter 07 — 策略層（Strategy Layer, 285 Strategies）**

策略分為 10 類：

1. 趨勢（Trend）
2. 突破（Breakout）
3. 回調（Pullback）
4. 反轉（Reversal）
5. 均值回歸（Mean Reversion）
6. K 線（Candle）
7. 成交量（Volume）
8. 籌碼策略（Chip）
9. 纏論模組（Chan Theory）
10. AI 策略（ML-based）

所有策略輸出：

```
signal = BUY / SELL / HOLD
confidence = 0~1
reason = "MACD 金叉 + GMMA trend"
```

---

# # **Chapter 08 — 多智能體（TradingAgents Layer）**

8 大 Agents：

* Technical Agent（技術面）
* Chip Agent（籌碼面）
* Fundamental Agent（基本面）
* News Agent（新聞）
* Sentiment Agent（情緒）
* Macro Agent（宏觀）
* AI Agent（AI 預測）
* Risk Agent（風控）

每個 Agent 輸出：

```
{
    "signal": BUY/SELL/HOLD,
    "confidence": 0.0~1.0,
    "factors": [...]
}
```

---

# # **Chapter 09 — Orchestrator（主控 AI）**

Orchestrator 負責：

1. 整合資料
2. 呼叫 Indicators
3. 執行所有策略
4. 執行所有 Agents
5. 加權投票
6. 決策（Decision Engine）

### Decision Output

```
decision = {
    "final_signal": BUY,
    "confidence": 0.82,
    "reason": [...],
    "order_plan": {...}
}
```

---

# # **Chapter 10 — 回測（Backtest Engine）**

事件驅動模型：

```
on_data → indicators → strategy → agents → decision → position update
```

回測輸出：

* 年化報酬
* Max Drawdown
* Sharpe
* Win Rate
* Average Hold
* Strategy Attribution

---

# # **Chapter 11 — Sandbox（封存模式）**

Sandbox 用於：

* 測試策略是否穩定
* 21 天穩定度要求
* 防止未成熟策略進入實盤

---

# # **Chapter 12 — Paper Trading（模擬交易）**

模擬：

* 成交回報
* 撮合
* 滑價模型
* 手續費 / 稅
* 部位更新

---

# # **Chapter 13 — Live Trading（富邦 API）**

支援：

* 自動下單
* 自動停損 / 停利
* 部位追蹤
* 斷線保護
* 錯單處理
* 手續費與稅預估

---

# # **Chapter 14 — UI（Streamlit）**

包含：

* Dashboard
* AI Signals
* Multi-Agent View
* Backtest Report
* 持倉管理
* 自動交易開關

---

# # **Chapter 15 — 系統安全性（Safety Layer）**

* 風控 Agent
* 最大虧損控制
* 單日最大損益
* 自動停交易（Kill Switch）
* 手續費/稅前估算
* 資金權重分配

---

# # **Chapter 16 — 系統延展性（Extensibility）**

你可以：

* 增加策略（Plug & Play）
* 增加指標（自動註冊）
* 增加 Agent
* 改變決策模型（ML、加權、投票）
* 增加資料源

---

# # **Chapter 17 — 系統維護性（Maintainability）**

* 模組化
* 分層架構
* 清晰資料流
* 乾淨分離 Concern（Agents / Strategy / Indicators）
* 使用型別標註、Docstring

---

# # **Chapter 18 — 未來規劃（Roadmap）**

未來可加入：

* Reinforcement Learning
* Portfolio Agent（投組管理）
* Options Module（選擇權）
* Multi-market（美股 / 加密貨幣）
* Auto-ML Strategy Search
* 模型風險評估（Model Risk）

---
