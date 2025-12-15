class OHLCValidator:
    """
    OHLCValidator

    負責驗證 OHLCV 資料結構與基本合理性
    S2.1 階段：只做結構與數值防呆
    """

    def validate(self, bars: list) -> list:
        if not isinstance(bars, list):
            raise ValueError("OHLCV data must be a list")

        validated = []

        for bar in bars:
            self._validate_single_bar(bar)
            validated.append(bar)

        return validated

    def _validate_single_bar(self, bar: dict):
        required_fields = [
            "symbol",
            "date",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ]

        for field in required_fields:
            if field not in bar:
                raise ValueError(f"Missing field in OHLCV data: {field}")

        if bar["high"] < bar["low"]:
            raise ValueError("High price cannot be lower than low price")

        if bar["volume"] < 0:
            raise ValueError("Volume cannot be negative")
