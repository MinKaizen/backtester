from time import time
from decimal import Decimal
from typing import Dict
from models.action import Action
from models.candle import Candle
from models.strategy import Strategy

class RandomStrategy(Strategy):
    name: str = "Random Strategy"

    def on_candle(self, candle: Candle, context: Dict) -> Action:
        now = round(time()*1000)

        if now % 3 == 0:
            return Action(amount = Decimal(100))
        elif now % 3 == 1:
            return Action(amount = Decimal(-100))

        return Action()
