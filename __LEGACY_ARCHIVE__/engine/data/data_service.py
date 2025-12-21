<<<<<<< HEAD:engine/data/data_service.py
from engine.data.connectors.mock_connector import MockDataConnector
from engine.data.validators.ohlcv_validator import OHLCValidator


class DataService:
    """
    DataService
    ===========
    資料服務層，負責：
    1. 向 Connector 取得原始資料
    2. 交給 Validator 驗證資料正確性
    3. 回傳「可用、乾淨」的資料給上層（Orchestrator / Strategy）
    """

    def __init__(self):
        # 目前使用 Mock Connector（未來可替換為真實 API）
        self.connector = MockDataConnector(symbol="2330.TW")

        # 資料驗證器（S2.1 重點）
        self.validator = OHLCValidator()

    def get_ohlcv(self, start_date: str, days: int = 3):
        """
        取得並驗證 OHLCV 資料
        """
        # Step 1：取得原始資料
        raw_bars = self.connector.fetch_ohlcv(
            start_date=start_date,
            days=days
        )

        # Step 2：進行資料驗證（關鍵步驟）
        validated_bars = self.validator.validate(raw_bars)

        # Step 3：回傳驗證後資料
        return validated_bars
=======
from engine.data.connectors.mock_connector import MockDataConnector
from engine.data.validators.ohlcv_validator import OHLCValidator


class DataService:
    """
    DataService
    ===========
    資料服務層，負責：
    1. 向 Connector 取得原始資料
    2. 交給 Validator 驗證資料正確性
    3. 回傳「可用、乾淨」的資料給上層（Orchestrator / Strategy）
    """

    def __init__(self):
        # 目前使用 Mock Connector（未來可替換為真實 API）
        self.connector = MockDataConnector(symbol="2330.TW")

        # 資料驗證器（S2.1 重點）
        self.validator = OHLCValidator()

    def get_ohlcv(self, start_date: str, days: int = 3):
        """
        取得並驗證 OHLCV 資料
        """
        # Step 1：取得原始資料
        raw_bars = self.connector.fetch_ohlcv(
            start_date=start_date,
            days=days
        )

        # Step 2：進行資料驗證（關鍵步驟）
        validated_bars = self.validator.validate(raw_bars)

        # Step 3：回傳驗證後資料
        return validated_bars
>>>>>>> 29da2c159127dfa84e9aea97bea00efd45973e0f:__LEGACY_ARCHIVE__/engine/data/data_service.py
