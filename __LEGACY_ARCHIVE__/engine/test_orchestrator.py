<<<<<<< HEAD:engine/test_orchestrator.py
from engine.orchestrator import Orchestrator


def main():
    orch = Orchestrator()
    bars = orch.get_market_data(symbol="2330.TW", days=3)

    for b in bars:
        print(b)


if __name__ == "__main__":
    main()
=======
from engine.orchestrator import Orchestrator


def main():
    orch = Orchestrator()
    bars = orch.get_market_data(symbol="2330.TW", days=3)

    for b in bars:
        print(b)


if __name__ == "__main__":
    main()
>>>>>>> 29da2c159127dfa84e9aea97bea00efd45973e0f:__LEGACY_ARCHIVE__/engine/test_orchestrator.py
