# strategies/ma_trend.py
# ============================================================
# TAITS – MA 趨勢策略
# ============================================================

from strategies.base_strategy import BaseStrategy


class MATrendStrategy(BaseStrategy):

    def __init__(self):
        self.name = "MA 趨勢策略"

    def run(self, df):

        if "ma_short" not in df.columns or "ma_long" not in df.columns:
            return {
                "name": self.name,
                "signal": "HOLD",
                "confidence": 0.1,
                "reason": "MA 指標不足，回傳 HOLD"
            }

        short = df["ma_short"].iloc[-1]
        long = df["ma_long"].iloc[-1]

        if short > long:
            return {
                "name": self.name,
                "signal": "BUY",
                "confidence": 0.6,
                "reason": "短均線上穿長均線，形成多頭趨勢"
            }

        elif short < long:
            return {
                "name": self.name,
                "signal": "SELL",
                "confidence": 0.6,
                "reason": "短均線下穿長均線，形成空頭趨勢"
            }

        return {
            "name": self.name,
            "signal": "HOLD",
            "confidence": 0.3,
            "reason": "均線沒有明確方向"
        }
