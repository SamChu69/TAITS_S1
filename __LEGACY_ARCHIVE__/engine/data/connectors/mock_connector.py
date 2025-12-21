# TAITS - Mock Data Connector
# Purpose:
#   Provide deterministic mock market data for research / testing
#   This is the FIRST real data output in TAITS (S2.1)

from datetime import datetime, timedelta
from typing import List, Dict, Any


class MockDataConnector:
    """
    MockDataConnector
    -----------------
    Simulates Taiwan stock OHLCV data.

    Design principles:
    - Deterministic output (no randomness by default)
    - Contract-first (structure > values)
    - Replaceable by real connectors (FinMind / TWSE / Broker API)
    """

    def __init__(self, symbol: str = "2330.TW"):
        self.symbol = symbol

    def fetch_ohlcv(
        self,
        start_date: str,
        days: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Fetch mock OHLCV data.

        Args:
            start_date (str): YYYY-MM-DD
            days (int): number of trading days

        Returns:
            List[Dict]:
                [
                    {
                        "symbol": "2330.TW",
                        "date": "2024-01-02",
                        "open": 600.0,
                        "high": 610.0,
                        "low": 595.0,
                        "close": 605.0,
                        "volume": 25000000
                    },
                    ...
                ]
        """

        base_date = datetime.strptime(start_date, "%Y-%m-%d")
        base_price = 600.0

        data: List[Dict[str, Any]] = []

        for i in range(days):
            current_date = base_date + timedelta(days=i)

            open_price = base_price + i * 2
            high_price = open_price + 10
            low_price = open_price - 5
            close_price = open_price + 5

            bar = {
                "symbol": self.symbol,
                "date": current_date.strftime("%Y-%m-%d"),
                "open": float(open_price),
                "high": float(high_price),
                "low": float(low_price),
                "close": float(close_price),
                "volume": int(20_000_000 + i * 1_000_000),
            }

            data.append(bar)

        return data
