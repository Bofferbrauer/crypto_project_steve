# from market_events.event import MockEvent
# from market_events.event import Event
# import message_delivery.sender
# import market_events.event

from time import sleep

# Taking the content from the Event and sets up an interval to publish the message to the terminal
class App():
    def __init__(self, events: str, time_interval: int):
        self.events = events
        self.time_interval = time_interval
        print(f"You had the following event: {events} ")

    def start(self) ->None:
        for event in self.events:
            event.check()
            
    
    def start(self) -> int:
        while True:
            for event in self.events:
                event.check()
            sleep(self.time_interval)
            



        
    