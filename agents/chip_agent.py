# agents/chip_agent.py
# ============================================================
# TAITS – ChipAgent（籌碼智能體）
# 觀察法人籌碼（若資料不足，則回傳中性）
# ============================================================

from typing import Dict, Any
import pandas as pd


class ChipAgent:
    """
    籌碼智能體（ChipAgent）
    預期可用欄位：
      - foreign_net : 外資買賣超
      - it_net      : 投信買賣超
      - dealer_net  : 自營商買賣超
    若沒有籌碼欄位，會回傳中性偏低信心的結果。
    """

    def __init__(self, lookback_days: int = 5):
        self.name = "ChipAgent"
        self.lookback_days = lookback_days

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        df: pd.DataFrame = context.get("df")

        if df is None or df.empty:
            return {
                "name": self.name,
                "bias": "NEUTRAL",
                "confidence": 0.3,
                "comment": "沒有價格資料，也沒有籌碼資訊，維持中性。"
            }

        chip_df = df.copy()

        has_chip_col = any(
            col in chip_df.columns for col in ["foreign_net", "it_net", "dealer_net"]
        )

        if not has_chip_col:
            return {
                "name": self.name,
                "bias": "NEUTRAL",
                "confidence": 0.3,
                "comment": "尚未接入法人籌碼資料，暫以中性看待。"
            }

        for col in ["foreign_net", "it_net", "dealer_net"]:
            if col not in chip_df.columns:
                chip_df[col] = 0.0

        recent = chip_df.tail(self.lookback_days)

        foreign_sum = recent["foreign_net"].sum()
        it_sum = recent["it_net"].sum()
        dealer_sum = recent["dealer_net"].sum()

        score = 0.0
        if foreign_sum > 0:
            score += 2.0
        elif foreign_sum < 0:
            score -= 2.0
        if it_sum > 0:
            score += 1.0
        elif it_sum < 0:
            score -= 1.0
        if dealer_sum > 0:
            score += 0.5
        elif dealer_sum < 0:
            score -= 0.5

        if score >= 2.0:
            bias = "BULL"
            confidence = min(1.0, 0.6 + score * 0.1)
            comment = f"最近 {self.lookback_days} 日三大法人整體偏多。"
        elif score <= -2.0:
            bias = "BEAR"
            confidence = min(1.0, 0.6 + abs(score) * 0.1)
            comment = f"最近 {self.lookback_days} 日三大法人整體偏空。"
        else:
            bias = "NEUTRAL"
            confidence = 0.4
            comment = f"最近 {self.lookback_days} 日三大法人買賣超方向不明顯。"

        return {
            "name": self.name,
            "bias": bias,
            "confidence": round(confidence, 2),
            "comment": comment
        }
