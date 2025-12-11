# agents/news_agent.py
# ============================================================
# TAITS – NewsAgent（新聞智能體）
# S1 版本預留：未實作實際新聞分析時，一律回中性說明
# ============================================================

from typing import Dict, Any


class NewsAgent:
    """
    新聞智能體（NewsAgent）
    S1 沒有接真實新聞 API，僅作為佔位。
    未來可接：
      - Cnyes / Anue / MoneyDJ / 國外新聞 API
      - LLM 分析新聞標題與內文，給出情緒與事件等級
    """

    def __init__(self):
        self.name = "NewsAgent"

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:

        ticker = context.get("ticker", "N/A")

        return {
            "name": self.name,
            "bias": "NEUTRAL",
            "confidence": 0.3,
            "comment": f"尚未接入 {ticker} 的新聞資料，新聞面暫不影響判斷。"
        }
