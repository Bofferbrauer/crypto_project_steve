from abc import abstractmethod, abstractproperty


class Event():
    @abstractmethod
    def event(self):
        pass

    def __init__(self): # * Add event and senders later
        pass

    @abstractproperty
    def condition(self):
        pass

    @abstractproperty
    def message(self, alert):
        print(f"This is the alert with the code: {alert}")

# Testing the Event class and event handler
alert = "Test"

check = Event()
check.event(alert)

class MockEvent(Event):
    def event(self, message):
        print(f"Mock event happened: {message}")
        
        
        
        
        