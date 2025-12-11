# engine/indicator_manager.py
# ============================================================
# TAITS – Indicator Manager（技術指標管理器）
# 負責統一調用 MA / RSI / MACD / GMMA / ChanLun 等指標
# ============================================================

import pandas as pd

from indicators.trend_ma import compute_ma
from indicators.momentum_rsi import compute_rsi
from indicators.momentum_macd import compute_macd
from indicators.trend_gmma import compute_gmma


class IndicatorManager:
    """
    技術指標管理器
    --------------------------------------------------------
    功能：
    1. 統一調用所有指標（MA / RSI / MACD / GMMA / ...）
    2. 將每個指標的輸出合併回 DataFrame
    3. 提供插件式擴充（之後可加入籌碼、K 線形態、纏論等）
    """

    def __init__(self):
        # 指標列表：未來新增指標，只需加入函數即可
        self.indicator_functions = [
            compute_ma,
            compute_rsi,
            compute_macd,
            compute_gmma,
        ]

    # --------------------------------------------------------
    # 主流程：執行所有指標
    # --------------------------------------------------------
    def compute(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        依序執行所有技術指標模組。

        每個指標模組都應為：
            def func(df) -> df
        並回傳 df（不可自行 deepcopy）

        回傳：
            加上所有技術指標欄位的 DataFrame
        """

        if df is None or df.empty:
            print("[IndicatorManager] WARNING: 空資料，跳過指標計算")
            return df

        for func in self.indicator_functions:
            try:
                df = func(df)
            except Exception as e:
                print(f"[IndicatorManager] 指標 {func.__name__} 計算失敗：{e}")

        return df
