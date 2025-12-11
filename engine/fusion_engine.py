# engine/fusion_engine.py
# ============================================================
# TAITS – Fusion Engine（最終決策大腦）
# 整合 Strategy + Agents + Regime → final_bias, confidence
# ============================================================

from typing import List, Dict, Any


class FusionEngine:
    """
    S1 版本 Fusion Engine
    ------------------------------------------------------------
    設計邏輯說明：

    1. Strategy Score（策略層）：
        BUY  → +1
        SELL → -1
        HOLD → 0

    2. Agent Score（Agent 層）：
        BULL    → +1
        BEAR    → -1
        NEUTRAL → 0

    3. Regime 調整：
        BULL     → 加權 * 1.2
        BEAR     → 加權 * 1.2 但方向相反
        SIDEWAYS → 加權 * 0.7（減弱趨勢）

    4. 最終 Bias：
        score > +0.20 → BUY
        score < -0.20 → SELL
        其餘 → HOLD

    5. confidence：
        abs(score) 經正規化（0.0 ~ 1.0）
    """

    # --------------------------------------------------------
    # 主流程
    # --------------------------------------------------------
    def fuse(
        self,
        strategy_results: List[Dict[str, Any]],
        agent_outputs: List[Dict[str, Any]],
        regime: str,
    ) -> Dict[str, Any]:

        # --------------------------------------------------------
        # 1. Strategy Score
        # --------------------------------------------------------
        s_total = 0
        s_count = 0

        for s in strategy_results:
            sig = s.get("signal", "HOLD")

            if sig == "BUY":
                s_total += 1
            elif sig == "SELL":
                s_total -= 1

            s_count += 1

        s_score = s_total / s_count if s_count > 0 else 0

        # --------------------------------------------------------
        # 2. Agent Score
        # --------------------------------------------------------
        a_total = 0
        a_count = 0

        for a in agent_outputs:
            bias = a.get("bias", "NEUTRAL")

            if bias == "BULL":
                a_total += 1
            elif bias == "BEAR":
                a_total -= 1

            a_count += 1

        a_score = a_total / a_count if a_count > 0 else 0

        # --------------------------------------------------------
        # 3. Combine Strategy + Agent
        # --------------------------------------------------------
        combined = (s_score * 0.55) + (a_score * 0.45)

        # --------------------------------------------------------
        # 4. Regime Adjustment
        # --------------------------------------------------------
        if regime == "BULL":
            combined *= 1.2
        elif regime == "BEAR":
            combined *= 1.2
        elif regime == "SIDEWAYS":
            combined *= 0.7

        # --------------------------------------------------------
        # 5. Confidence（0.0 ~ 1.0）
        # --------------------------------------------------------
        conf = min(1.0, abs(combined))

        # --------------------------------------------------------
        # 6. Final Decision
        # --------------------------------------------------------
        if combined > 0.20:
            final_bias = "BUY"
        elif combined < -0.20:
            final_bias = "SELL"
        else:
            final_bias = "HOLD"

        # --------------------------------------------------------
        # 7. 輸出統一格式
        # --------------------------------------------------------
        return {
            "final_bias": final_bias,
            "confidence": round(conf, 2),
            "reason": (
                f"Strategy={round(s_score,2)}, Agent={round(a_score,2)}, "
                f"Regime={regime}, Combined={round(combined,3)}"
            ),
        }
