from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal

class Candle(BaseModel):
    timestamp: datetime = Field(..., description="Start time of the candle")
    open: Decimal = Field(..., description="Opening price")
    high: Decimal = Field(..., description="Highest price")
    low: Decimal = Field(..., description="Lowest price")
    close: Decimal = Field(..., description="Closing price")
    volume: Decimal = Field(..., description="Traded volume during the candle")

    class Config:
        from_attributes = True

