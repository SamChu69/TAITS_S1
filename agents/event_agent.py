# agents/event_agent.py
# ============================================================
# TAITS – EventAgent（事件 / 特殊狀況智能體）
# 用來處理除權息、重大公告、法說會等事件（S1 先佔位）
# ============================================================

from typing import Dict, Any


class EventAgent:
    """
    事件型智能體（EventAgent）
    未來可接：
      - 除權息日 / 股利政策
      - 重大訊息公告
      - 法說會日期與內容
    S1 版僅做為佔位，回傳中性。
    """

    def __init__(self):
        self.name = "EventAgent"

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:

        ticker = context.get("ticker", "N/A")

        return {
            "name": self.name,
            "bias": "NEUTRAL",
            "confidence": 0.3,
            "comment": f"{ticker} 尚未載入事件資料（除權息 / 法說會等），事件面暫不影響判斷。"
        }
