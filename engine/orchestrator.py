# engine/orchestrator.py
# ============================================================
# TAITS – 主流程 Orchestrator（完整正式版）
# ============================================================

from pathlib import Path
from typing import Dict, Any

from data_sources.fallback_manager import FallbackManager
from engine.data_validator import DataValidator
from engine.indicator_manager import IndicatorManager
from engine.strategy_manager import StrategyManager
from engine.agent_manager import AgentManager
from engine.market_regime_engine import MarketRegimeEngine
from engine.fusion_engine import FusionEngine
from engine.risk_engine import RiskEngine
from engine.report_formatter import ReportFormatter
from engine.report_md_formatter import MarkdownReportFormatter


class Orchestrator:
    """
    TAITS 主流程引擎
    -----------------------------------------------------------
    Data → Indicators → Strategies → Agents → Regime 
         → Fusion → Risk → Reports
    -----------------------------------------------------------
    """

    def __init__(self) -> None:
        self.data_loader = FallbackManager()
        self.validator = DataValidator()
        self.indicator_manager = IndicatorManager()
        self.strategy_manager = StrategyManager()
        self.agent_manager = AgentManager()
        self.regime_engine = MarketRegimeEngine()
        self.fusion_engine = FusionEngine()
        self.risk_engine = RiskEngine()
        self.report_formatter = ReportFormatter()
        self.md_formatter = MarkdownReportFormatter()

    # ============================================================
    # 主流程
    # ============================================================
    def run(self, ticker: str, start: str, end: str) -> Dict[str, Any]:

        print("\n================= TAITS START =================")
        print(f"[Orchestrator] Ticker={ticker}  Period={start} → {end}")

        # --------------------------------------------------------
        # Step 1：取得資料
        # --------------------------------------------------------
        df = self.data_loader.get(ticker, start, end)

        if df is None or df.empty:
            print("[Orchestrator] ERROR：無法取得資料")
            return {}

        print(f"[Orchestrator] 資料取得成功，共 {len(df)} 筆")

        # --------------------------------------------------------
        # Step 2：資料格式檢查
        # --------------------------------------------------------
        ok, msg = self.validator.validate(df)
        if not ok:
            print(f"[Orchestrator] 資料不合法：{msg}")
            return {}

        print("[Orchestrator] 資料檢查成功")

        # --------------------------------------------------------
        # Step 3：計算指標
        # --------------------------------------------------------
        df = self.indicator_manager.compute(df)
        print("[Orchestrator] 指標計算完成")

        # --------------------------------------------------------
        # Step 4：策略執行
        # --------------------------------------------------------
        strategy_results = self.strategy_manager.run(df)
        print(f"[StrategyManager] 執行完成，共 {len(strategy_results)} 策略")

        # --------------------------------------------------------
        # Step 5：建立 Agents context
        # --------------------------------------------------------
        context = {
            "ticker": ticker,
            "df": df,
            "strategies": strategy_results,
        }

        # --------------------------------------------------------
        # Step 6：Agents 執行
        # --------------------------------------------------------
        print("[AgentManager] 開始執行 Agents...")
        agent_outputs = self.agent_manager.run(context)
        print(f"[AgentManager] 完成，共 {len(agent_outputs)} Agents")

        # --------------------------------------------------------
        # Step 7：市場 Regime 判斷
        # --------------------------------------------------------
        regime = self.regime_engine.classify(df)
        print(f"[RegimeEngine] 市場狀態：{regime}")

        # --------------------------------------------------------
        # Step 8：Fusion Engine（策略 + Agents + Regime）
        # --------------------------------------------------------
        final_signal = self.fusion_engine.fuse(
            strategy_results, agent_outputs, regime
        )

        print("[FusionEngine] 最終 Bias：", final_signal.get("final_bias"))
        print("[FusionEngine] 信心：", final_signal.get("confidence"))

        # --------------------------------------------------------
        # Step 9：風險引擎（Risk Engine Override）
        # --------------------------------------------------------
        final_signal = self.risk_engine.apply(final_signal)
        print("[RiskEngine] 風控後 Bias：", final_signal.get("final_bias"))

        # --------------------------------------------------------
        # Step 10：整合 Final Result
        # --------------------------------------------------------
        result = {
            "ticker": ticker,
            "regime": regime,
            "strategies": strategy_results,
            "agents": agent_outputs,
            "final_signal": final_signal,
            "price_data": df.tail(5),
        }

        # --------------------------------------------------------
        # Step 11：產出報告（TXT / JSON / Markdown）
        # --------------------------------------------------------
        root = Path(__file__).resolve().parents[1]
        output_dir = root / "output"

        self.report_formatter.save_files(result, str(output_dir))
        self.md_formatter.save_markdown(result, str(output_dir))

        print("\n================= TAITS END =================\n")
        return result
