# agents/macro_agent.py
# ============================================================
# TAITS – MacroAgent（宏觀環境智能體）
# 以近期報酬率與波動，粗略推估大盤 / 標的所處環境
# ============================================================

from typing import Dict, Any
import pandas as pd
import numpy as np


class MacroAgent:
    """
    宏觀智能體（MacroAgent）
    S1 版本採用標的自身 30 日報酬 + 波動作為簡易代理。
    未來可：
      - 接 SOX / 匯率 / VIX / 大盤指數
      - 接期貨 / ETF 作為領先指標
    """

    def __init__(self, lookback_days: int = 30):
        self.name = "MacroAgent"
        self.lookback_days = lookback_days

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        df: pd.DataFrame = context.get("df")

        if df is None or df.empty or "close" not in df.columns:
            return {
                "name": self.name,
                "bias": "NEUTRAL",
                "confidence": 0.3,
                "comment": "缺乏價格資料，無法推估宏觀環境，暫中性。"
            }

        if len(df) < self.lookback_days + 1:
            return {
                "name": self.name,
                "bias": "NEUTRAL",
                "confidence": 0.3,
                "comment": "資料長度不足，宏觀環境判斷可信度有限。"
            }

        close = df["close"]
        ret = (close.iloc[-1] / close.iloc[-self.lookback_days - 1]) - 1
        vol = np.std(close.pct_change().dropna())

        score = 0.0
        reasons = []

        if ret > 0.05:
            score += 1.0
            reasons.append(f"{self.lookback_days} 日累積報酬 > 5%，偏多頭環境。")
        elif ret < -0.05:
            score -= 1.0
            reasons.append(f"{self.lookback_days} 日累積報酬 < -5%，偏空頭環境。")

        if vol > 0.03:
            score -= 0.5
            reasons.append("近期期待波動偏高，風險較大。")

        if score > 0.5:
            bias = "BULL"
        elif score < -0.5:
            bias = "BEAR"
        else:
            bias = "NEUTRAL"

        confidence = min(1.0, 0.3 + abs(score) * 0.2)

        return {
            "name": self.name,
            "bias": bias,
            "confidence": round(confidence, 2),
            "comment": "；".join(reasons) if reasons else "宏觀指標訊號有限，暫中性。"
        }
