from engine.data.data_service import DataService


class Orchestrator:
    def __init__(self):
        self.data_service = DataService()

    def get_market_data(self, symbol: str, days: int = 3):
        # 先固定日期，之後會做成自動
        return self.data_service.get_ohlcv(
            start_date="2024-01-02",
            days=days
        )
