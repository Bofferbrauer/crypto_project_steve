from market_events.event import MockEvent
from market_events.event import Event
import message_delivery.sender

class App():
    def __init__(self, events):
        self.events = events
        print(f"You had the following event: {events} ")

# events = "Test"

events = MockEvent("Small test")
print(events.check)

start = App()
print(start.events(events))
        
    