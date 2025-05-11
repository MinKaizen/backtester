from typing import Dict
from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from models.strategy import Strategy

class Player(BaseModel):
    strategy: Strategy
    bankroll: Decimal
    context: Dict = {}
    # model_config = ConfigDict(arbitrary_types_allowed=True)

    class Config:
        from_attributes = True
        arbitrary_types_allowed=True
