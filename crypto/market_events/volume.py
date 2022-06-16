from typing import List
from crypto.data.source import DataSource, Pair
from crypto.market_events.event import Event
from crypto.message_delivery.sender import Sender

class VolumeEvent(Event):
    def __init__(self, data_source : DataSource, senders : List[Sender], pair : Pair, threshold : float) -> None:
        super().__init__(senders, data_source)
        self.pair = pair
        self.threshold = threshold

    @property
    def condition(self) -> bool:
        current_ob = self.data_source.get_order_book(self.pair)
        return(current_ob.bid_volume >= self.threshold)
        
    @property
    def message(self) -> str:
        return f"{self.pair.generic_name} best price offering reached {self.volume_threshold} "
        
        