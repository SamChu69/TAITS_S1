# strategies/gmma_trend.py
# ============================================================
# TAITS – GMMA 多均線趨勢策略
# ============================================================

from strategies.base_strategy import BaseStrategy


class GMMAtrendStrategy(BaseStrategy):

    def __init__(self):
        self.name = "GMMA 多均線趨勢策略"

    def run(self, df):

        required_cols = ["gmma_short_3", "gmma_long_30"]

        for col in required_cols:
            if col not in df.columns:
                return {
                    "name": self.name,
                    "signal": "HOLD",
                    "confidence": 0.1,
                    "reason": "GMMA 指標不足"
                }

        s = df["gmma_short_3"].iloc[-1]
        l = df["gmma_long_30"].iloc[-1]

        if s > l:
            return {
                "name": self.name,
                "signal": "BUY",
                "confidence": 0.7,
                "reason": "短期 GMMA 高於長期 GMMA，趨勢多頭"
            }

        elif s < l:
            return {
                "name": self.name,
                "signal": "SELL",
                "confidence": 0.7,
                "reason": "短期 GMMA 低於長期 GMMA，趨勢空頭"
            }

        return {
            "name": self.name,
            "signal": "HOLD",
            "confidence": 0.3,
            "reason": "GMMA 無明確趨勢"
        }
