from engine.data.connectors.mock_connector import MockDataConnector

def main():
    connector = MockDataConnector(symbol="2330.TW")
    bars = connector.fetch_ohlcv(start_date="2024-01-02", days=3)

    for b in bars:
        print(b)

if __name__ == "__main__":
    main()
