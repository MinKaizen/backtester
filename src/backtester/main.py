from pprint import pprint
from datetime import datetime
from decimal import Decimal
from models.candle import Candle

def main():
    print("Hello world!")
    candle = Candle(
        timestamp=datetime.utcnow(),
        open=Decimal("101.5"),
        high=Decimal("105.0"),
        low=Decimal("100.0"),
        close=Decimal("103.2"),
        volume=Decimal("1500.75"),
    )
    pprint(candle.model_dump())

if __name__ == "__main__":
    main()
