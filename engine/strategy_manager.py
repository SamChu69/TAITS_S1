# engine/strategy_manager.py
# ============================================================
# TAITS – Strategy Manager（策略管理器）
# 統一管理所有策略，回傳多空訊號供 Fusion Engine 使用
# ============================================================

import pandas as pd

from strategies.macd_momentum import MACDMomentumStrategy
from strategies.rsi_reversal import RSIReversalStrategy
from strategies.ma_trend import MATrendStrategy
from strategies.gmma_trend import GMMAtrendStrategy


class StrategyManager:
    """
    策略管理器
    --------------------------------------------------------
    功能：
    1. 管理並執行所有策略
    2. 每個策略需繼承 BaseStrategy
    3. 每個策略回傳統一格式：
        {
            "name": "...",
            "signal": "BUY/SELL/HOLD",
            "confidence": 0.0 ~ 1.0,
            "reason": "中文說明"
        }
    """

    def __init__(self):
        # 登記需要啟動的策略
        # 未來新增 285 策略時，只需加進這裡
        self.strategies = [
            MACDMomentumStrategy(),
            RSIReversalStrategy(),
            MATrendStrategy(),
            GMMAtrendStrategy(),
        ]

    # --------------------------------------------------------
    # 主函數：執行所有策略
    # --------------------------------------------------------
    def run(self, df: pd.DataFrame):
        """
        執行所有策略並回傳結果陣列。
        """
        results = []

        if df is None or df.empty:
            print("[StrategyManager] WARNING: 無有效資料，跳過策略運算")
            return results

        for strategy in self.strategies:
            try:
                result = strategy.run(df)
                results.append(result)
            except Exception as e:
                print(f"[StrategyManager] 策略 {strategy.name} 執行錯誤：{e}")

        return results
