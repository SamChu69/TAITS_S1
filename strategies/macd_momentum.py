# strategies/macd_momentum.py
# ============================================================
# TAITS – MACD 動能策略
# ============================================================

from strategies.base_strategy import BaseStrategy


class MACDMomentumStrategy(BaseStrategy):

    def __init__(self):
        self.name = "MACD 動能策略"

    def run(self, df):

        if "macd" not in df.columns or "macd_signal" not in df.columns:
            return {
                "name": self.name,
                "signal": "HOLD",
                "confidence": 0.1,
                "reason": "MACD 指標不足，回傳 HOLD"
            }

        macd = df["macd"].iloc[-1]
        sig = df["macd_signal"].iloc[-1]

        if macd > sig:
            return {
                "name": self.name,
                "signal": "BUY",
                "confidence": 0.7,
                "reason": "MACD 上穿訊號線，動能轉強"
            }

        elif macd < sig:
            return {
                "name": self.name,
                "signal": "SELL",
                "confidence": 0.7,
                "reason": "MACD 下穿訊號線，動能轉弱"
            }

        return {
            "name": self.name,
            "signal": "HOLD",
            "confidence": 0.3,
            "reason": "MACD 位於中性區間"
        }
