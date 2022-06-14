from pydantic import BaseModel, PositiveFloat
from typing import List, Dict

class OrderBook(BaseModel):
    bid: PositiveFloat
    ask: PositiveFloat
    bid_volume: PositiveFloat
    ask_volume: PositiveFloat

def mid(bid, ask_price) -> List[PositiveFloat]:
    return((bid+ask_price)/2)

test = OrderBook(bid=2.3, ask=3.6, bid_volume=8, ask_volume=2.3)

print(f" The price paid is {test.bid}, the asking price was {test.ask}, wanted to buy {test.bid_volume} and got {test.ask_volume}." )


