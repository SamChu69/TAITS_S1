# agents/sentiment_agent.py
# ============================================================
# TAITS – SentimentAgent（市場情緒智能體）
# S1 版本以保守設計，預留未來接入社群 / 籌碼情緒指標
# ============================================================

from typing import Dict, Any


class SentimentAgent:
    """
    市場情緒智能體（SentimentAgent）
    context 可以在未來加入：
      - sentiment_score: -1.0 ~ +1.0
    S1 若沒有任何情緒數據，直接回傳中性。
    """

    def __init__(self):
        self.name = "SentimentAgent"

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:

        sentiment_score = context.get("sentiment_score", 0.0)

        if sentiment_score > 0.2:
            bias = "BULL"
        elif sentiment_score < -0.2:
            bias = "BEAR"
        else:
            bias = "NEUTRAL"

        confidence = min(1.0, 0.3 + abs(sentiment_score))

        return {
            "name": self.name,
            "bias": bias,
            "confidence": round(confidence, 2),
            "comment": f"情緒分數={round(sentiment_score, 3)}（S1 簡化版，尚未接實際社群/期權情緒資料）。"
        }
