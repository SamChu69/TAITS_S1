# engine/market_regime_engine.py
# ============================================================
# TAITS – Market Regime Engine（市場狀態分類引擎）
# 負責判斷市場是多頭、空頭或盤整，用於 Fusion Engine 權重調整
# ============================================================

import pandas as pd


class MarketRegimeEngine:
    """
    市場狀態（Regime）分類器
    -------------------------------------------------------
    S1 版本採用簡易但實用的趨勢 + 波動判斷方法：

    1. 取近 20 日報酬率：
       return20 = (close / close.shift(20)) - 1

    2. 若 > +3% → BULL（多頭）
       若 < -3% → BEAR（空頭）
       介於區間 → SIDEWAYS（盤整）

    * 未來 S2 可改成 ML 模型（HMM / KMeans）
    -------------------------------------------------------
    """

    def __init__(self, bull_th=0.03, bear_th=-0.03):
        self.bull_th = bull_th
        self.bear_th = bear_th

    # -------------------------------------------------------
    # 主流程：分類市場狀態
    # -------------------------------------------------------
    def classify(self, df: pd.DataFrame) -> str:

        if df is None or df.empty or "close" not in df.columns:
            return "UNKNOWN"

        if len(df) < 21:
            return "UNKNOWN"

        close = df["close"]
        ret20 = (close.iloc[-1] / close.iloc[-21]) - 1

        if ret20 >= self.bull_th:
            return "BULL"

        elif ret20 <= self.bear_th:
            return "BEAR"

        else:
            return "SIDEWAYS"
