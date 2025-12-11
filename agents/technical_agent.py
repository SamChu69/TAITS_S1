# agents/technical_agent.py
# ============================================================
# TAITS – TechnicalAgent（技術面智能體）
# 依據技術指標綜合判斷：MA / RSI / MACD / GMMA
# ============================================================

from typing import Dict, Any
import pandas as pd


class TechnicalAgent:
    """
    技術面智能體（TechnicalAgent）
    使用 df 中的技術指標欄位，給出多空偏向。
    需要的欄位（若不存在則自動降級為中性判斷）：
      - ma_short, ma_long
      - rsi
      - macd, macd_signal
      - gmma_short_3, gmma_long_30
    """

    def __init__(self):
        self.name = "TechnicalAgent"

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        df: pd.DataFrame = context.get("df")

        if df is None or df.empty:
            return {
                "name": self.name,
                "bias": "NEUTRAL",
                "confidence": 0.3,
                "comment": "沒有有效價格資料，技術面維持中性。"
            }

        row = df.iloc[-1]

        score = 0.0
        reasons = []

        # MA 趨勢
        if "ma_short" in df.columns and "ma_long" in df.columns:
            ma_short = row["ma_short"]
            ma_long = row["ma_long"]
            if ma_short > ma_long:
                score += 1.0
                reasons.append("短均線在長均線之上（多頭排列）。")
            elif ma_short < ma_long:
                score -= 1.0
                reasons.append("短均線在長均線之下（空頭排列）。")

        # RSI
        if "rsi" in df.columns:
            rsi = row["rsi"]
            if rsi < 30:
                score += 0.7
                reasons.append("RSI < 30，技術面超賣。")
            elif rsi > 70:
                score -= 0.7
                reasons.append("RSI > 70，技術面超買。")

        # MACD
        if "macd" in df.columns and "macd_signal" in df.columns:
            macd = row["macd"]
            sig = row["macd_signal"]
            if macd > sig:
                score += 0.8
                reasons.append("MACD > 訊號線，動能偏多。")
            elif macd < sig:
                score -= 0.8
                reasons.append("MACD < 訊號線，動能偏空。")

        # GMMA
        if "gmma_short_3" in df.columns and "gmma_long_30" in df.columns:
            gs = row["gmma_short_3"]
            gl = row["gmma_long_30"]
            if gs > gl:
                score += 1.0
                reasons.append("短期 GMMA 高於長期 GMMA，趨勢偏多。")
            elif gs < gl:
                score -= 1.0
                reasons.append("短期 GMMA 低於長期 GMMA，趨勢偏空。")

        # 綜合判斷
        if score > 0.5:
            bias = "BULL"
        elif score < -0.5:
            bias = "BEAR"
        else:
            bias = "NEUTRAL"

        confidence = min(1.0, 0.3 + abs(score) * 0.2)

        comment = "；".join(reasons) if reasons else "技術指標訊號有限，維持中性。"

        return {
            "name": self.name,
            "bias": bias,
            "confidence": round(confidence, 2),
            "comment": comment
        }
