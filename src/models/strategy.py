from abc import ABC, abstractmethod
from typing import Dict
from models.action import Action
from models.candle import Candle

class Strategy(ABC):
    name: str

    @abstractmethod
    def on_candle(self, candle: Candle, context: Dict) -> Action:
        pass
