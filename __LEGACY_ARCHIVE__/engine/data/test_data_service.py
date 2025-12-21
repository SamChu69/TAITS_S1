<<<<<<< HEAD:engine/data/test_data_service.py
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
=======
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
>>>>>>> 29da2c159127dfa84e9aea97bea00efd45973e0f:__LEGACY_ARCHIVE__/engine/data/test_data_service.py
