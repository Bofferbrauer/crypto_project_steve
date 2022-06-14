from abc import abstractmethod
from pydantic import BaseModel, PositiveFloat, ValidationError, root_validator
from typing import List, Dict

# Setting up the values and making sure they're positive float numbers
class OrderBook(BaseModel):
    bid: PositiveFloat
    ask: PositiveFloat
    bid_volume: PositiveFloat
    ask_volume: PositiveFloat

    # Validating the results and throwing an error if an entry is not a positive float
    @root_validator
    def check_price(cls,values):
        bid_x = values.get("bid")
        ask_x = values.get("ask")

        #making sure that the asking price is higher than the bid
        if bid_x <= ask_x:
            return values
        else:
            raise ValueError("The asking price is too high")
            
    def mid(bid, ask) -> List[PositiveFloat]:
        return((bid+ask)/2)

# try:
#     test = OrderBook(bid=2.3, ask=3.6, bid_volume=8, ask_volume=2.3)
#     print(f" The price paid is {test.bid}, the asking price was {test.ask}, wanted to buy {test.bid_volume} and got {test.ask_volume}." )
#     test2 = OrderBook(bid=2.3, ask=1.6, bid_volume=8, ask_volume=2.3)
#     print(f" The price paid is {test2.bid}, the asking price was {test2.ask}, wanted to buy {test2.bid_volume} and got {test2.ask_volume}." )

# except ValueError as e:
#     print(e)

class Pair(BaseModel):
    first: str
    second: str
    def generic_name(first, second):
        print("".join(first) + "_" + "".join(second))

test_pair = Pair.generic_name(first="BTC", second="USDT")
print(test_pair)
        
class DataSource():
    def __init__(self, Pair : Pair):    
        self.pair = Pair

    @abstractmethod
    def get_order_book(self):
        pass




