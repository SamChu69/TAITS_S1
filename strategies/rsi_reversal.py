# strategies/rsi_reversal.py
# ============================================================
# TAITS – RSI 反轉策略
# ============================================================

from strategies.base_strategy import BaseStrategy


class RSIReversalStrategy(BaseStrategy):

    def __init__(self):
        self.name = "RSI 反轉策略"

    def run(self, df):

        if "rsi" not in df.columns:
            return {
                "name": self.name,
                "signal": "HOLD",
                "confidence": 0.1,
                "reason": "RSI 指標不存在，回傳 HOLD"
            }

        rsi = df["rsi"].iloc[-1]

        if rsi < 30:
            return {
                "name": self.name,
                "signal": "BUY",
                "confidence": 0.6,
                "reason": "RSI < 30，超賣反彈訊號"
            }

        elif rsi > 70:
            return {
                "name": self.name,
                "signal": "SELL",
                "confidence": 0.6,
                "reason": "RSI > 70，超買回落訊號"
            }

        return {
            "name": self.name,
            "signal": "HOLD",
            "confidence": 0.3,
            "reason": "RSI 位於中性區間"
        }
