# agents/ai_model_agent.py
# ============================================================
# TAITS – AIModelAgent（AI 模型智能體）
# S1 不實際呼叫外部 LLM，只作佔位與未來擴充點
# ============================================================

from typing import Dict, Any


class AIModelAgent:
    """
    AI 模型智能體（AIModelAgent）
    未來可串接：
      - GPT / DeepSeek / Qwen / Gemini 等
      - 使用策略輸出 + Agents 輸入，產生自然語言分析
    S1 先不實際呼叫外部 API，以中性說明為主。
    """

    def __init__(self):
        self.name = "AIModelAgent"

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:

        ticker = context.get("ticker", "N/A")

        return {
            "name": self.name,
            "bias": "NEUTRAL",
            "confidence": 0.4,
            "comment": f"AI 模型尚未實際串接，僅作為 {ticker} 的未來解釋型智能體入口。"
        }
