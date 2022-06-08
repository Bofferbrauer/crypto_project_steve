
from market_events.event import Event
from message_delivery.sender import Sender
from market_events.event import MockEvent


class App():
    def __init__(self, events, sender):
        self.events = events
        self.sender = sender
        
        print(f"{sender}, you had the following event: {events} ")

events = Event()
sender = Sender()

start = App()
print(start.events(events))
        
    