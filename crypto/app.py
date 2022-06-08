from asyncio import events
import market_events.event
import message_delivery.sender

class App():
    def __init__(self, events):
        self.events = events
        print(f"You had the following event: {events} ")

events = "Test"

start = App()
print(start.events(events))
        
    