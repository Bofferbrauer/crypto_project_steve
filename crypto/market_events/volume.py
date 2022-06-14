from event import Event

class VolumeEvent(Event):
    def __init__(self, data_source, senders, pair, volume):
        super().__init__(senders, data_source)
        