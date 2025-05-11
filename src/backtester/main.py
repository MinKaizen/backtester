from decimal import Decimal
import pandas as pd
from backtester.backtest_runner import BacktestRunner
from models.player import Player
from strategies.random_strategy import RandomStrategy

def main():
    df = pd.read_csv(
        "mock_data.csv",
        dtype={
            "timestamp": str,
            "open": float,
            "high": float,
            "low": float,
            "close": float,
            "volume": float,
        },
    )
    strategy = RandomStrategy()
    player = Player(strategy=strategy, bankroll=Decimal("1000.0"))
    runner = BacktestRunner(df, [player])
    runner.run()

if __name__ == "__main__":
    main()
