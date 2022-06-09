from abc import abstractmethod, abstractproperty
from email import message


class Event():
    @abstractmethod
    def event(self):
        pass

    def __init__(self, senders): # * Add event later
        self.senders = senders

    @property
    @abstractmethod # ? this was the supposed way to do it
    # @abstractproperty # ! Depreciated, do not use anymore
    def condition(self):
        pass
    @property
    @abstractmethod
    def message(self, alert):
        print(f"This is the alert with the code: {alert}")
    
    def check(self):
        if self.condition():
            for senders in self.senders:
                senders.send(self.message)
                print("It works!")
                
            
        

# Testing the Event class and event handler

class MockEvent(Event):
    def event(self, message):
        print(f"Mock event happened: {message}")
        
message = "Test"

check = MockEvent()
print(check.event(message))
        
        
        
        