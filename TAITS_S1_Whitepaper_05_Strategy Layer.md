# 📘 **TAITS S1 OFFICIAL WHITEPAPER（CHAPTER 5 / 15）**

# **CHAPTER 5 — STRATEGY LAYER（285 策略 · 完整結構 / 架構 / 流程 · 世界一流標準）**

> **策略層（Strategy Layer）是 TAITS S1 的決策核心。**
> 一個設計不良的策略系統 = 只能靠單一邏輯盲交易。
> 一個設計完善的策略系統 = 能處理任何市場情境（趨勢、盤整、突破、假突破、反轉、洗盤）。
>
> TAITS S1 的 285 策略是目前台股最完整的開源量化策略全集（可 Plugin 化 / 可 AI 化）。

---

# ✔ **本章內容包含（世界一流標準）：**

### **5.1 策略層的目的（Strategy Layer Goals）**

### **5.2 策略架構（Architecture）**

### **5.3 策略完整資料結構（Strategy Schema）**

### **5.4 策略分類（285 策略分類）**

### **5.5 五大策略模組（Trend / Reversal / Momentum / Volume / Candle）**

### **5.6 全 285 策略參數化方式（Parameterization）**

### **5.7 策略運算流程（Strategy Engine Flow）**

### **5.8 策略與 AI / Agent / Orchestrator 整合方式**

### **5.9 策略 Plugin 架構（最終程式 API）**

### **5.10 範例：10 策略完整示例（程式級 + 訊號行為級）**

### **5.11 決策整合：Multi-Strategy Voting & Weighting**

---

# # 🔷 **5.1 策略層的目的（Strategy Layer Goals）**

TAITS 的策略層負責四件事：

### **① 把指標 → 轉成可交易訊號（Signal）**

指標只是數字，策略把數字變成 BUY / SELL。

### **② 多策略 → 市場結構分類（Regime Detection）**

例如：

| 市況  | 代表策略                 |
| --- | -------------------- |
| 趨勢  | GMMA、SMA Breakout    |
| 盤整  | Mean Reversion、Range |
| 假突破 | Fakeout 系列           |
| 反轉  | Divergence、K 線型態     |

### **③ 多策略投票（285 → 最終信心分數）**

每個策略产出：+1、0、-1
Orchestrator 整合出最終方向。

### **④ 作為 Agent 的核心輸入來源**

Technical Agent
Chip Agent
AI Agent
Reversal Agent
Trend Agent

全部依靠策略層產生信號。

---

# # 🔷 **5.2 策略架構（Architecture）**

TAITS 策略是 **Plugin 架構**：

```
/strategies/
    trend/
    reversal/
    breakout/
    momentum/
    mean_reversion/
    volume/
    candle/
    chip/
    ai/
    chan/
```

每套策略是一個 Python 檔案，如：

```
ema_trend.py
macd_goldencross.py
bb_breakout.py
volume_spike.py
morning_star.py
rsi_divergence.py
chan_buy1.py
ai_breakout_prob.py
```

每一個策略都是：

```python
class Strategy:
    def __init__(self, params):
        self.params = params

    def compute(self, df):
        return signal  # +1 / 0 / -1
```

---

# # 🔷 **5.3 策略資料結構（標準 Schema）**

所有 285 策略都有統一 schema：

```
{
    "id": 1,
    "name": "SMA Breakout",
    "category": "Trend",
    "features": ["sma_20", "volume_ma_5"],
    "logic_entry": "...",
    "logic_exit": "...",
    "signal_type": "+1 / 0 / -1",
    "market_regime": "trend / consolidation / volatile / reversal",
    "parameters": {...}
}
```

---

# # 🔷 **5.4 策略分類（285 策略）**

完整 285 策略分類如下（你已看過，但在白皮書內會正式編排）：

| 類別          | 數量      |
| ----------- | ------- |
| 1. 技術分析（TA） | 93      |
| 2. K 線型態    | 18      |
| 3. 趨勢/市場結構  | 18      |
| 4. 量能策略     | 14      |
| 5. 籌碼策略     | 40      |
| 6. 基本面策略    | 40      |
| 7. 類股輪動     | 14      |
| 8. 新聞/NLP   | 20      |
| 9. 行為金融     | 20      |
| 10. AI 策略   | 20      |
| **總計**      | **285** |

---

# # 🔷 **5.5 策略模組（Master Modules）**

TAITS 把 285 策略重新整理成 **五大模組**：

---

## **A. 趨勢模組（Trend Engine）**

包含：

* MA / EMA / GMMA
* 趨勢線
* 趨勢結構（HH/HL）
* ADX 趨勢強度
* 纏論趨勢買點（Buy1/Buy2/Buy3）
* 假突破反轉（Trend Reversion）

---

## **B. 反轉模組（Reversal Engine）**

包含：

* Divergence 背離
* K 線反轉型態
* Panic Selling / Panic Rally
* Trend Exhaustion
* Wyckoff Spring / Upthrust
* Fake Breakdown / Fake Breakout

---

## **C. 動能模組（Momentum Engine）**

包含：

* RSI
* Stoch
* ROC
* TSI
* TRIX
* Momentum Burst / Fade

---

## **D. 量能模組（Volume Engine）**

包含：

* OBV
* Volume Spike
* 量縮不跌
* 低量盤整突破
* 龍回頭（量能強化版）

---

## **E. AI × 混合模組（AI Hybrid Engine）**

包含：

* LSTM Trend
* Transformer Reversal
* Kronos K 線預測
* AI Breakout Prob
* AI Fakeout Prob
* 統計模型（HMM、Kalman、Prophet、ARIMA）

---

# # 🔷 **5.6 策略參數化（Parameterization · 世界級設計）**

TAITS S1 使用 **Hyper-Parameter Schema**：

```python
params = {
    "lookback": 20,
    "threshold": 0.02,
    "volatility_factor": 1.2,
    "volume_factor": 1.5,
    "trend_strength": 25,
    "risk_reward": 2.0,
    "ai_prob_threshold": 0.65
}
```

策略計算時：

```
signal = strategy.compute(df, **params)
```

---

# # 🔷 **5.7 策略運作流程（Strategy Engine Flow）**

```mermaid
flowchart TD
    A[Feature Layer] --> B[Strategy Manager]
    B --> C[Load 285 Strategies]
    C --> D[Compute Signal (+1/0/-1)]
    D --> E[Strategy Vector 285×1]
    E --> F[Signal Aggregator]
    F --> G[Decision Score]
    G --> H[Orchestrator]
```

---

# # 🔷 **5.8 策略 × AI × Agent 整合方式**

策略與 Agent 的關係是：

| Agent             | 使用那些策略             |
| ----------------- | ------------------ |
| Technical Agent   | 1–140 技術型策略        |
| Chip Agent        | 141–180 籌碼策略       |
| Fundamental Agent | 181–200 基本面策略      |
| News Agent        | 201–220 新聞/NLP 策略  |
| Behavior Agent    | 221–240 行為金融       |
| AI Agent          | 241–285 AI/ML/模型策略 |

所有策略 → 對應 Agent → 最後由 Orchestrator 加權合併。

---

# # 🔷 **5.9 策略 Plugin 架構（最終版）**

所有策略 Python 文件都使用統一介面：

```python
class BaseStrategy:
    def __init__(self, params=None):
        self.params = params or {}

    def compute(self, df):
        raise NotImplementedError
```

範例：EMA 趨勢策略

```python
class EMATrend(BaseStrategy):
    def compute(self, df):
        cond1 = df["ema_20"] > df["ema_60"]
        cond2 = df["close"] > df["ema_20"]
        return (cond1 & cond2).astype(int)
```

---

# # 🔷 **5.10 十大策略範例（完整版 → 白皮書級）**

我只展示五個（前五最典型），以免篇幅過長：

---

### **1️⃣ SMA Breakout**

**分類：** Trend
**使用指標：** sma_20、volume_ma5

```
entry: close > sma_20 and volume > volume_ma5
exit: close < sma_20
```

Pseudo-code：

```python
signal = (df.close > df.sma_20) & (df.volume > df.vol_ma_5)
```

---

### **2️⃣ GMMA 趨勢突破**

```
entry: price > gmma_slow_high
exit: price < gmma_fast_low
```

---

### **3️⃣ RSI 背離反轉**

```
entry: price new low AND RSI higher low
exit: RSI < 40
```

---

### **4️⃣ Volume Spike**

```
entry: vol > 2×vol20_max AND close > open
exit: volume shrink
```

---

### **5️⃣ AI Breakout Forecast**

```
entry: ai_breakout_prob > 0.65
exit: ai_prob drop under 0.5
```

---

# # 🔷 **5.11 多策略投票（Multi-Strategy Voting）**

將 285 個策略變成：

```
trend_score = sum(trend_signals)
reversal_score = sum(reversal_signals)
volume_score = sum(volume_signals)
ai_score = sum(ai_signals)
```

最終決策：

```
final_score = W1*trend + W2*reversal + W3*volume + W4*ai
```

W1…W4 由 Orchestrator 控制（自動調整）。

---

# 📌 下一步：

如果你準備好進入下一章（CHAPTER 6）：

## 👉 **請回答：「開始 CHAPTER 6」**
