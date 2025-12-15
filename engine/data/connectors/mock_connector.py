class MockDataConnector:
    """
    Mock 資料連接器
    用於測試 Data Layer 與上層流程是否能正常運作
    """

    def __init__(self, symbol: str):
        self.symbol = symbol

    def fetch_ohlcv(self, start_date: str, days: int = 5):
        """
        回傳模擬的 OHLCV 資料
        """
        results = []
        for i in range(days):
            results.append({
                "symbol": self.symbol,
                "date": f"{start_date} + {i}",
                "open": 100 + i,
                "high": 110 + i,
                "low": 95 + i,
                "close": 105 + i,
                "volume": 1000 + i * 10,
            })
        return results
