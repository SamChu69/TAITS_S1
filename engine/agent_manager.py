# engine/agent_manager.py
# ============================================================
# TAITS – Agent Manager（多智能體管理核心）
# 統一呼叫各種 Agents：技術、籌碼、基本面、情緒、新聞、宏觀、AI 模型等
# ============================================================

from typing import List, Dict, Any

from agents.technical_agent import TechnicalAgent
from agents.chip_agent import ChipAgent
from agents.fundamental_agent import FundamentalAgent
from agents.sentiment_agent import SentimentAgent
from agents.news_agent import NewsAgent
from agents.macro_agent import MacroAgent
from agents.derivatives_agent import DerivativesAgent
from agents.event_agent import EventAgent
from agents.ai_model_agent import AIModelAgent
from agents.risk_agent import RiskAgent
# 若你有纏論 Agent，可在這裡加入：
# from agents.chan_agent import ChanAgent


class AgentManager:
    """
    多智能體管理器（Multi-Agent Controller）
    -------------------------------------------------------------
    功能：
      1. 建立並管理所有 Agents
      2. 自動執行每個 Agent 的 analyze()
      3. 收集所有 Agents 的 bias / confidence / comment
      4. 提供給 Fusion Engine 進行多腦融合決策
    -------------------------------------------------------------
    Agents 統一輸出格式：
      {
        "name": "TechnicalAgent",
        "bias": "BULL / BEAR / NEUTRAL",
        "confidence": 0.0 ~ 1.0,
        "comment": "中文理由"
      }
    """

    def __init__(self):

        # * 預設啟用的 Agents（可隨你需求擴充）
        self.agents = [
            TechnicalAgent(),
            ChipAgent(),
            FundamentalAgent(),
            SentimentAgent(),
            NewsAgent(),
            MacroAgent(),
            DerivativesAgent(),
            EventAgent(),
            AIModelAgent(),
            RiskAgent(),
            # ChanAgent(),   # 若你未來加入纏論 Agent, 在此啟用
        ]

    # ---------------------------------------------------------
    # 主流程：執行所有 Agents
    # ---------------------------------------------------------
    def run(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        執行所有 Agents 並回傳結果列表。

        context 應包含：
            "ticker"     : 股票代碼
            "df"         : 價格資料
            "strategies" : 策略運算結果
        """

        results = []

        for agent in self.agents:
            try:
                output = agent.analyze(context)
                results.append(output)
            except Exception as e:
                print(f"[AgentManager] Agent {agent.__class__.__name__} 執行錯誤：{e}")

        return results
