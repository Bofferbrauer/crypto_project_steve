from crypto.market_events.event import Event

class VolumeEvent(Event):
    def __init__(self, data_source : str, senders : str, pair : str, volume_treshold : float):
        super().__init__(senders, data_source, volume_treshold)
    def alert(self):
        pass
        
        