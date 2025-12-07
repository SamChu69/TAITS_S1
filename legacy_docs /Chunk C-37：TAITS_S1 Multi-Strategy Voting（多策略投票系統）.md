下面這段就是 **TAITS_S1 — C-37：Multi-Strategy Voting（多策略投票系統）最終版**，已經照你說的當成「世界一流 10/10 規格」來寫，可以直接丟給 Cursor / VS Code 當開發藍本。

---

# 📘 C-37 — Multi-Strategy Voting System

**（多策略投票系統／Ensemble Decision Engine）**

> 功能定位：
> **C-35 策略評分 → C-37 多策略投票 → C-36 AI Agent & Orchestrator**
>
> C-37 的職責是：把所有策略的分數、方向、信心整合成
> 「**單一最終方向 + 強度分數**」，給 Agents / Orchestrator 使用。

---

## C-37.1 在整個 TAITS_S1 裡的位置

整體流程（簡化版）：

```text
[Data / Indicators] 
      ↓
[Strategy Engine]  ← 每個策略跑完，產生 raw signals
      ↓
[C-35 Strategy Scoring]  ← 將策略轉成標準化分數 (0–100)
      ↓
★ C-37 Multi-Strategy Voting ★  ← 本章
      ↓
[Agents 層：Technical / Chip / AI ...]
      ↓
[C-36 AI Agent + Orchestrator]
      ↓
[Trade Plan / Paper / Live]
```

C-37 是「**同一群策略之間的整合模組**」，例如：

* 技術策略群（TA）
* 籌碼策略群（Chip）
* K 線型態策略群（Candles）
* AI 策略群（AI-Strategies）

每一群都可以呼叫 C-37 來算出：

> 這一群策略，對某一檔股票、某一 timeframe，**整體是偏多還是偏空？強度多少？**

---

## C-37.2 輸入 / 輸出介面設計

### 📥 輸入：一群策略的標準化結果

每個策略先經過 C-35 → 輸入 C-37 的結構建議如下：

```python
StrategySignal = {
    "symbol": "2330.TW",
    "timeframe": "D",              # D/H1/M15 ...
    "strategy_id": "TA_001_SMA_Breakout",
    "category": "technical",       # technical / chip / candle / ai / ...
    "direction": "BUY",            # BUY / SELL / HOLD / NONE
    "score": 78,                   # 0 ~ 100, 已由 C-35 標準化
    "confidence": 0.82,            # 0.0 ~ 1.0 （策略自身信心）
    "weight_base": 1.0,            # 策略預設權重（可由 config 設定）
    "regime_tags": ["bull", "trend"], 
    "recent_performance": {        # 回測 or 近期實盤資訊（可選）
        "win_rate_30d": 0.63,
        "sharpe_30d": 1.2
    },
    "meta": {
        "reason": "SMA20 breakout with volume",
        "group": "trend_follow"
    }
}
```

C-37 的輸入就是 **一個 list**：

```python
signals: list[StrategySignal]
```

---

### 📤 輸出：整體多空方向與強度

C-37 會輸出「某一群策略」對這檔標的的統一評價：

```python
VotingResult = {
    "symbol": "2330.TW",
    "timeframe": "D",

    "final_direction": "BUY",      # STRONG_BUY/BUY/NEUTRAL/SELL/STRONG_SELL
    "final_score": 68,             # -100 ~ +100 （多空淨分數）

    "buy_strength": 0.71,          # 0 ~ 1
    "sell_strength": 0.21,         # 0 ~ 1
    "hold_strength": 0.08,         # 0 ~ 1

    "num_strategies": 35,
    "num_buy": 22,
    "num_sell": 8,
    "num_hold": 5,

    "agreement_ratio": 0.73,       # 同方向比例
    "conflict_ratio": 0.27,        # 多空對立比例
    "avg_confidence": 0.79,        # 策略平均信心分數

    "regime_adjustment": {         # Kronos / Market Regime 的調整結果
        "regime": "bull",
        "trend_factor": 1.10,
        "volatility_factor": 0.95
    },

    "ai_hint": {                   # 來自 AI Agent 的提示（可選）
        "ai_trend_score": 72,      # 0~100
        "ai_vote": +15             # -50~+50
    },

    "debug": {                     # 非必要，給開發者用
        "raw_buy_power": 23.5,
        "raw_sell_power": 7.1
    }
}
```

這份結果會交給：

* TechnicalAgent / ChipAgent / … → 做「該面向的總結」
* Orchestrator → 與 AI Agent / 其他 Agents 一起決定最終交易指令

---

## C-37.3 投票邏輯設計（概念）

整體分成 5 個步驟：

1. **清洗 & 過濾策略**
2. **計算每個策略的「實際投票權重」**
3. **累積多空力量（Buy / Sell / Hold Power）**
4. **產生「方向 + 分數 + 一致度」**
5. **考慮 Regime / AI 進行微調（加/減分）**

---

## C-37.4 策略權重計算（核心）

最重要的是：**每個策略的票不一樣重**。

### 基本公式：

```text
effective_weight = weight_base 
                 × confidence_factor
                 × performance_factor
                 × regime_factor
```

### 1️⃣ confidence_factor

依策略自身信心調整：

```python
confidence_factor = 0.5 + 0.5 * confidence  # 0.5 ~ 1.0
```

信心 0 → 0.5 倍
信心 1 → 1.0 倍

---

### 2️⃣ performance_factor

由 C-35 的「績效表」決定：

* 最近 30 天 / 90 天 回測 or 模擬結果
* win rate / Sharpe / max drawdown

舉例：

```python
def calc_performance_factor(win_rate, sharpe):
    base = 1.0
    if win_rate > 0.6:
        base += 0.1
    if sharpe > 1.0:
        base += 0.1
    if win_rate < 0.4:
        base -= 0.1
    if sharpe < 0.5:
        base -= 0.1
    return max(0.5, min(1.3, base))
```

---

### 3️⃣ regime_factor（配合 Kronos 市況）

* 多頭（bull）：順勢做多策略權重 ↑、逆勢放空策略權重 ↓
* 空頭（bear）：放空策略權重 ↑

簡化版：

```python
def calc_regime_factor(regime, direction):
    if regime == "bull" and direction == "BUY":
        return 1.15
    if regime == "bull" and direction == "SELL":
        return 0.85
    if regime == "bear" and direction == "SELL":
        return 1.15
    if regime == "bear" and direction == "BUY":
        return 0.85
    return 1.0
```

---

## C-37.5 投票計算流程（Pseudo-code）

```python
class StrategyVotingEngine:

    def vote(self, signals, regime=None, ai_hint=None) -> dict:
        """
        signals: List[StrategySignal]
        regime:  來自 Kronos 的市場狀態，例如 {"regime": "bull"}
        ai_hint: 來自 AI Agent 的結果，例如 {"ai_vote": +15}
        """

        # 1. 過濾無效訊號
        valid = [s for s in signals if s["direction"] in ("BUY", "SELL", "HOLD")]

        if not valid:
            return self._empty_result()

        total_buy_power = 0.0
        total_sell_power = 0.0
        total_hold_power = 0.0
        total_weight = 0.0

        for s in valid:
            # 2. 策略權重
            win_rate = s["recent_performance"].get("win_rate_30d", 0.5)
            sharpe = s["recent_performance"].get("sharpe_30d", 0.5)

            confidence_factor = 0.5 + 0.5 * s["confidence"]
            perf_factor = calc_performance_factor(win_rate, sharpe)
            regime_factor = calc_regime_factor(
                regime.get("regime") if regime else None,
                s["direction"]
            )

            w = s["weight_base"] * confidence_factor * perf_factor * regime_factor

            # 3. 多空力量（score 0~100 → -1~+1）
            norm_score = (s["score"] - 50) / 50.0   # -1 ~ +1

            if s["direction"] == "BUY":
                total_buy_power += w * max(norm_score, 0)
            elif s["direction"] == "SELL":
                total_sell_power += w * max(-norm_score, 0)
            else:  # HOLD
                total_hold_power += w * (1 - abs(norm_score))

            total_weight += w

        # 4. 正規化多空力量
        if total_weight == 0:
            return self._empty_result()

        buy_strength = total_buy_power / total_weight
        sell_strength = total_sell_power / total_weight
        hold_strength = total_hold_power / total_weight

        # 5. 淨多空分數
        net_score = buy_strength - sell_strength  # -1 ~ +1

        # 6. AI 微調（可選，用 ai_vote -50~+50）
        if ai_hint and "ai_vote" in ai_hint:
            ai_adjust = ai_hint["ai_vote"] / 100.0  # -0.5~+0.5
            net_score = max(-1.0, min(1.0, net_score + ai_adjust * 0.2))

        final_score = int(net_score * 100)  # -100 ~ +100

        # 7. 方向分類
        if final_score >= 60:
            final_dir = "STRONG_BUY"
        elif final_score >= 20:
            final_dir = "BUY"
        elif final_score <= -60:
            final_dir = "STRONG_SELL"
        elif final_score <= -20:
            final_dir = "SELL"
        else:
            final_dir = "NEUTRAL"

        agreement_ratio = max(buy_strength, sell_strength, hold_strength)

        return {
            "final_direction": final_dir,
            "final_score": final_score,
            "buy_strength": round(buy_strength, 3),
            "sell_strength": round(sell_strength, 3),
            "hold_strength": round(hold_strength, 3),
            "num_strategies": len(valid),
            "num_buy": sum(1 for s in valid if s["direction"] == "BUY"),
            "num_sell": sum(1 for s in valid if s["direction"] == "SELL"),
            "num_hold": sum(1 for s in valid if s["direction"] == "HOLD"),
            "agreement_ratio": round(agreement_ratio, 3),
            "conflict_ratio": round(1 - agreement_ratio, 3),
        }
```

---

## C-37.6 對 Orchestrator / Agents 的使用方式

### 1️⃣ TechnicalAgent 裡的使用流程

```python
class TechnicalAgent:

    def __init__(self, strategies, voting_engine):
        self.strategies = strategies
        self.voting_engine = voting_engine

    def analyze(self, market, regime, ai_hint=None):
        # 1. 跑所有技術策略
        signals = []
        for s in self.strategies:
            raw = s.run(market)             # 回傳 raw signal
            scored = score_strategy(raw)    # C-35
            signals.append(scored)

        # 2. 呼叫 C-37 投票
        vote = self.voting_engine.vote(signals, regime, ai_hint)

        # 3. 封裝成 Agent 輸出
        return {
            "agent": "technical",
            "symbol": market.symbol,
            "timeframe": market.timeframe,
            "direction": vote["final_direction"],
            "score": vote["final_score"],
            "details": vote
        }
```

其他 Agents（Chip / Fundamental / News / AI）都可以用同樣模式套用。

---

## C-37.7 設計重點總結（給未來維護用）

1. **C-37 不做「預測」，只做「投票與加權」**
2. 所有策略必須先標準化成 **0–100 分** 才送進來（由 C-35 負責）。
3. Regime（Kronos）與 AI Agent 給的是「**偏好與微調**」，不是「直接強迫方向」。
4. 可以做到：

   * 例如 50 個技術策略 → 一個清楚結論：**BUY 68 / SELL 12 / HOLD 20**
   * 或是 20 個籌碼策略 → 「SELL 強烈集中」 → 交給 Orchestrator 再評估。
5. 未來若要新增：

   * 新策略 → 只要能輸出 StrategySignal 結構即可
   * 不需改 C-37 核心程式 → 高擴充性。

---

## ✅ C-37 完成情況（你關心的幾件事）

* ✅ 可以直接丟給 Cursor / VSCode，讓它「生成 ai_voting.py」等檔案
* ✅ 結構與前面 C-30 ~ C-36 完全相容
* ✅ 已包含：

  * 資料結構
  * 投票公式
  * 權重設計
  * Regime / AI 整合方式
  * Python 風格 pseudo-code

---
