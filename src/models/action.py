from decimal import Decimal
from enum import Enum
from pydantic import BaseModel

class ActionType(str, Enum):
    sell = 'sell'
    buy = 'buy'
    hold = 'hold'

class Action(BaseModel):
    amount: Decimal = Decimal()
    stop_loss: Decimal | None = None

    class Config:
        from_attributes = True

    def getType(self) -> ActionType:
        match(self.amount):
            case x if x > Decimal("0"):
                action = ActionType.buy
            case x if x < Decimal("0"):
                action = ActionType.sell
            case x if x == Decimal("0"):
                action = ActionType.hold
            case _:
                raise RuntimeError("Trying to getType of amount but it is neither positive, negative or 0")
        return action
