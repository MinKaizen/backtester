from datetime import datetime
from decimal import Decimal
from typing import Dict, List
import pandas as pd

from models.candle import Candle
from models.player import Player

class BacktestRunner:
    result: Dict = {}

    def __init__(self, candles: pd.DataFrame, players: List[Player]):
        self.candles = candles
        self.players = players

    def run(self):
        for idx, row in self.candles.iterrows():
            # Convert row to Candle model
            candle = Candle(
                timestamp=datetime.strptime(str(row['timestamp']), '%Y-%m-%d %H:%M:%S'),
                open=Decimal(str(row['open'])),
                high=Decimal(str(row['high'])),
                low=Decimal(str(row['low'])),
                close=Decimal(str(row['close'])),
                volume=Decimal(str(row['volume']))
            )

            for player in self.players:
                strategy = player.strategy
                context = player.context

                try:
                    action = strategy.on_candle(candle, context)
                    print(f"[{strategy.name}] {candle.timestamp} -> {action}")
                except Exception as e:
                    print(f"Error in strategy '{strategy.name}' at index {idx}: {e}")
