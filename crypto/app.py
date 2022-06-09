# from market_events.event import MockEvent
# from market_events.event import Event
# import message_delivery.sender
# import market_events.event

from time import sleep


class App():
    def __init__(self, events, time_interval):
        self.events = events
        self.time_interval = time_interval
        print(f"You had the following event: {events} ")
    
    def start(self):
        while True:
            for event in self.events:
                event.check()
            sleep(self.time_inerval)
            

# events = "Test"

# events = MockEvent


        
    