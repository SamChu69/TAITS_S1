# strategies/base_strategy.py
# ============================================================
# TAITS – Base Strategy（策略父類別）
# 所有策略必須繼承此類別
# ============================================================

class BaseStrategy:
    """
    所有策略的共同介面
    --------------------------------------------------------
    子類別必須實作：
        - name: 策略名稱
        - run(df) -> dict
    統一輸出格式：
        {
            "name": "...",
            "signal": "BUY/SELL/HOLD",
            "confidence": 0.0~1.0,
            "reason": "中文說明"
        }
    """

    name = "BaseStrategy"

    def run(self, df):
        raise NotImplementedError("子策略必須實作 run() 方法")
