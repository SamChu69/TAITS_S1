from engine.data.data_service import DataService


def main():
    service = DataService()

    bars = service.get_ohlcv(
        start_date="2024-01-02",
        days=3
    )

    print("Validated OHLCV bars:")
    for b in bars:
        print(b)


if __name__ == "__main__":
    main()
