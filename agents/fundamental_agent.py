# agents/fundamental_agent.py
# ============================================================
# TAITS – FundamentalAgent（基本面智能體）
# S1 版本：暫時沒有接財報與評分，用保守中性邏輯
# ============================================================

from typing import Dict, Any


class FundamentalAgent:
    """
    基本面智能體（FundamentalAgent）
    S1 階段尚未接入實際財報 / 評分 API，
    先回傳「保守中性」的判斷，避免亂給方向。
    日後可接：
      - 財報 API
      - 自行維護的評分表
      - LLM 解析財報 / 法說會
    """

    def __init__(self):
        self.name = "FundamentalAgent"

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:

        ticker = context.get("ticker", "N/A")

        return {
            "name": self.name,
            "bias": "NEUTRAL",
            "confidence": 0.3,
            "comment": f"尚未對 {ticker} 接入基本面資料，暫不給方向。"
        }
