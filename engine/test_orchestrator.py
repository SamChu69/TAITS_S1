from engine.orchestrator import Orchestrator


def main():
    orch = Orchestrator()
    bars = orch.get_market_data(symbol="2330.TW", days=3)

    for b in bars:
        print(b)


if __name__ == "__main__":
    main()
