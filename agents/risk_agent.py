# agents/risk_agent.py
# ============================================================
# TAITS – RiskAgent（風控智能體）
# 與 engine.risk_engine 不同，這裡是「觀點型」風控 Agent
# ============================================================

from typing import Dict, Any
import pandas as pd
import numpy as np


class RiskAgent:
    """
    風控智能體（RiskAgent）
    與 RiskEngine 的差別：
      - RiskEngine：直接覆寫最終 Bias / Confidence（硬風控）
      - RiskAgent ：提供一個「風險觀點」，交由 FusionEngine 一併考慮

    S1 版本：
      - 用最近 10 日波動判斷風險高低
    """

    def __init__(self, lookback_days: int = 10):
        self.name = "RiskAgent"
        self.lookback_days = lookback_days

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        df: pd.DataFrame = context.get("df")

        if df is None or df.empty or "close" not in df.columns:
            return {
                "name": self.name,
                "bias": "NEUTRAL",
                "confidence": 0.4,
                "comment": "沒有足夠價格資料，風險狀態未知。"
            }

        if len(df) < self.lookback_days + 1:
            return {
                "name": self.name,
                "bias": "NEUTRAL",
                "confidence": 0.4,
                "comment": "資料不足以評估近期波動，暫維持中性。"
            }

        close = df["close"]
        ret = close.pct_change().dropna().tail(self.lookback_days)

        vol = float(np.std(ret))

        if vol > 0.05:
            bias = "BEAR"
            confidence = 0.7
            comment = f"近 {self.lookback_days} 日波動率約 {round(vol,4)}，偏高風險，傾向保守。"
        elif vol < 0.02:
            bias = "BULL"
            confidence = 0.5
            comment = f"近 {self.lookback_days} 日波動率約 {round(vol,4)}，相對平穩，可承擔適度風險。"
        else:
            bias = "NEUTRAL"
            confidence = 0.5
            comment = f"近 {self.lookback_days} 日波動率約 {round(vol,4)}，風險中等。"

        return {
            "name": self.name,
            "bias": bias,
            "confidence": round(confidence, 2),
            "comment": comment
        }
