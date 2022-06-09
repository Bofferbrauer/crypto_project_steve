# from market_events.event import MockEvent
# from market_events.event import Event
# import message_delivery.sender
# import market_events.event

class App():
    def __init__(self, events):
        self.events = events
        print(f"You had the following event: {events} ")
    
    def start(self):
        for event in self.events:
            event.check()
            

# events = "Test"

# events = MockEvent


        
    