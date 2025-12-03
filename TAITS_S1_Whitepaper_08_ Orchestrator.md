📘 **CHAPTER 8 — STRATEGY CATALOG PART I
**TAITS S1 OFFICIAL WHITEPAPER — CHAPTER 8**
# 🌐 **CHAPTER 8 前言**

從這章開始，你將看到：

### ✔ **285 策略完整逐一展開（全內容）**

### ✔ 每一個策略都有固定 6 大欄位：

1. **策略編號 Strategy ID**
2. **策略名稱 Strategy Name（EN + TW）**
3. **策略類別 Category**
4. **進場邏輯 Entry Logic**
5. **出場邏輯 Exit Logic**
6. **Pseudo-code（TAITS S1 格式）**

這些策略都會完全對應：

* 指標層（Indicators）
* Agents（Technical Agent）
* Orchestrator（Voting + Weighting）
* Backtest（Fitness Score）

---

# 🔥 **本章內容：策略 1–20（Trend / MA / EMA / GMMA / MACD / Pullback）**

這 20 個策略屬於「技術分析核心基礎」，是 TAITS S1 整套策略系統的底座。

---

# ———— 🎯 **STRATEGY 1–20 開始** ————

---

# **1. SMA 突破策略（SMA Breakout Strategy）**

**分類：** 趨勢（Trend Following）
**適用市場：** 緩升、多頭、轉強

### 📈 **進場條件**

* 收盤價 **突破 SMA20**
* 同時 **量能 > 5 日均量**

### 📉 **出場條件**

* 收盤價跌破 SMA20

### 🧠 **Pseudo-code**

```python
if close > sma20 and volume > vol_ma5:
    signal = 1
elif close < sma20:
    signal = -1
```

---

# **2. EMA 趨勢策略（EMA Trend Model）**

**分類：** 趨勢
**適用市場：** 單邊趨勢盤

### 進場

* EMA20 > EMA60
* 收盤價 > EMA20

### 出場

* EMA20 < EMA60

```python
if ema20 > ema60 and close > ema20:
    signal = 1
elif ema20 < ema60:
    signal = -1
```

---

# **3. EMA20 回踩買進（EMA20 Pullback Buy）**

**分類：** 回調（Pullback）

### 進場

* 趨勢向上（EMA20 > EMA60）
* 今日最低價觸碰 EMA20

### 出場

* 收盤價跌破 EMA20

```python
if ema20 > ema60 and low <= ema20:
    signal = 1
if close < ema20:
    signal = -1
```

---

# **4. EMA60 大波段策略（EMA60 Trend Ride）**

**分類：** 長線趨勢

### 進場

* EMA20 > EMA60 > EMA120

### 出場

* 收盤價跌破 EMA60

```python
if ema20 > ema60 > ema120:
    signal = 1
if close < ema60:
    signal = -1
```

---

# **5. WMA 趨勢策略（Weighted MA Crossover）**

**分類：** 趨勢

```python
if wma20 > wma50:
    signal = 1
elif wma20 < wma50:
    signal = -1
```

---

# **6. HMA 趨勢零滯後（HMA Zero-Lag Trend）**

**分類：** 快速趨勢追蹤

```python
if close > hma20 and hma20 rising:
    signal = 1
elif close < hma20:
    signal = -1
```

---

# **7. T3 平滑突破（T3 Trend Break）**

```python
if t3_fast > t3_slow:
    signal = 1
elif t3_fast < t3_slow:
    signal = -1
```

---

# **8. DEMA 雙均線加速（DEMA Acceleration）**

```python
if dema20 > dema50:
    signal = 1
elif dema20 < dema50:
    signal = -1
```

---

# **9. ZLEMA 去滯後（ZLEMA Anti-Lag Trend）**

```python
if zlema20 > zlema50:
    signal = 1
elif zlema20 < zlema50:
    signal = -1
```

---

# **10. GMMA 快慢雙層共振（GMMA Fast-Slow Confluence）**

### 進場

* GMMA 快線群平均 > 慢線群平均
* 收盤價 > 快線群平均

```python
if gmma_fast_avg > gmma_slow_avg and close > gmma_fast_avg:
    signal = 1
```

---

# **11. GMMA 趨勢突破（GMMA Slow Breakout）**

```python
if close > gmma_slow_high:
    signal = 1
elif close < gmma_slow_low:
    signal = -1
```

---

# **12. GMMA 回調買點（GMMA Pullback Buy）**

```python
if trend_up and low <= gmma_fast_low:
    signal = 1
```

---

# **13. GMMA 趨勢反轉（GMMA Fast Cross Slow）**

```python
if gmma_fast_cross_up_slow:
    signal = 1
elif gmma_fast_cross_down_slow:
    signal = -1
```

---

# **14. MA20 回測買進（MA20 Retest Buy）**

```python
if low <= ma20:
    signal = 1
elif close < ma20:
    signal = -1
```

---

# **15. MA 龍回頭（Dragon Tail Buy）**

```python
if big_green and next_day_low <= ma10:
    signal = 1
```

---

# **16. MACD 金叉（MACD Golden Cross）**

```python
if dif_cross_up_dea:
    signal = 1
elif dif_cross_down_dea:
    signal = -1
```

---

# **17. MACD 背離（MACD Divergence）**

```python
if price_new_low and hist_higher_low:
    signal = 1
```

---

# **18. MACD 零軸突破（MACD Zero Line Break）**

```python
if hist > 0 and hist_prev <= 0:
    signal = 1
elif hist < 0:
    signal = -1
```

---

# **19. MACD 死叉（MACD Dead Cross）**

```python
if dif_cross_down_dea:
    signal = -1
```

---

# **20. MACD 快速反轉（MACD Histogram Reversal）**

```python
if hist shrinking 3 days:
    signal = 1
```

---
