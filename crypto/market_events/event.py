from abc import abstractmethod, abstractproperty


class Event():
    @abstractmethod
    def event(self):
        pass

    def __init__(self, senders): # * Add event later
        self.senders = senders

    @abstractproperty
    def condition(self):
        pass

    @abstractproperty
    def message(self, alert):
        print(f"This is the alert with the code: {alert}")

# Testing the Event class and event handler

class MockEvent(Event):
    def event(self, message):
        print(f"Mock event happened: {message}")
        
message = "Test"

check = MockEvent()
print(check.event(message))
        
        
        
        