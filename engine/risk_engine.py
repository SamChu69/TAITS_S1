# engine/risk_engine.py
# ============================================================
# TAITS – Risk Engine（風險控管核心）
# 在 Fusion Engine 的最終決策後進行覆核，必要時強制調整 Bias
# ============================================================

from typing import Dict, Any
import numpy as np


class RiskEngine:
    """
    TAITS S1 風控引擎（Risk Engine）
    ------------------------------------------------------------
    功能：
    1. 根據價格波動檢查是否進入高風險狀態
    2. 若波動過高，自動降低 confidence
    3. 若波動極端，強制 override 為 HOLD（停止交易）
    4. 未來可擴充台股 TWSE 熔斷、零股特規、漲跌幅、防呆等
    """

    def __init__(self,
                 high_vol_threshold: float = 0.03,
                 extreme_vol_threshold: float = 0.07):
        """
        :param high_vol_threshold: 高波動門檻（預設 3%）
        :param extreme_vol_threshold: 極端波動（預設 7%）
        """
        self.high_vol_threshold = high_vol_threshold
        self.extreme_vol_threshold = extreme_vol_threshold

    # --------------------------------------------------------
    # 主流程：覆核最終決策
    # --------------------------------------------------------
    def apply(self, final_signal: Dict[str, Any]) -> Dict[str, Any]:
        """
        final_signal 格式：
        {
            "final_bias": "BUY/SELL/HOLD",
            "confidence": 0.0~1.0,
            "reason": "...",
            "price_data": df.tail(5)
        }
        """

        if "price_data" not in final_signal:
            return final_signal

        df = final_signal["price_data"]

        if df is None or df.empty or "close" not in df.columns:
            return final_signal

        # 計算最近 5 根 K 線的波動幅度
        close = df["close"]
        ret = close.pct_change().dropna()

        if ret.empty:
            return final_signal

        vol = np.std(ret)

        # --------------------------------------------------------
        # 極端波動 → 強制停止（HOLD）
        # --------------------------------------------------------
        if vol >= self.extreme_vol_threshold:
            final_signal["final_bias"] = "HOLD"
            final_signal["confidence"] = 0.0
            final_signal["reason"] += f" | RiskEngine: 極端波動 {round(vol,4)} → 強制 HOLD"
            return final_signal

        # --------------------------------------------------------
        # 高波動 → 降低信心
        # --------------------------------------------------------
        if vol >= self.high_vol_threshold:
            old_conf = final_signal["confidence"]
            new_conf = max(0.0, old_conf * 0.5)

            final_signal["confidence"] = new_conf
            final_signal["reason"] += f" | RiskEngine: 高波動 {round(vol,4)} → 降低信心至 {new_conf}"

        return final_signal
