<<<<<<< HEAD:engine/data/test_mock_connector.py
from engine.data.connectors.mock_connector import MockDataConnector

def main():
    connector = MockDataConnector(symbol="2330.TW")
    bars = connector.fetch_ohlcv(start_date="2024-01-02", days=3)

    for b in bars:
        print(b)

if __name__ == "__main__":
    main()
=======
from engine.data.connectors.mock_connector import MockDataConnector

def main():
    connector = MockDataConnector(symbol="2330.TW")
    bars = connector.fetch_ohlcv(start_date="2024-01-02", days=3)

    for b in bars:
        print(b)

if __name__ == "__main__":
    main()
>>>>>>> 29da2c159127dfa84e9aea97bea00efd45973e0f:__LEGACY_ARCHIVE__/engine/data/test_mock_connector.py
