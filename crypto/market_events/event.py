from abc import abstractmethod
# from crypto.message_delivery.sender import message


class Event():
    
    def __init__(self, senders): # * Add senders and event later
        self.senders = senders
        # pass

    @abstractmethod
    def event(self):
        pass

    @property
    @abstractmethod # ? this was the supposed way to do it
    # @abstractproperty # ! Depreciated, do not use anymore
    def condition(self):
        pass
    
    @property
    @abstractmethod
    def message(self, alert):
        # print(f"This is the alert with the code: {alert}") # ! Not in an abstract method!
        pass
    
    def check(self, senders):
        if self.condition():
            for senders in self.senders:
                senders.send(self.message)
                print("It works!")
                
            
# check = Event("Mark")
# print(check.event(message))        

# Testing the Event class and event handler

class MockEvent(Event):
    @property
    def condition(self):
        return True

    @property    
    def event(self, message):         
        print(f"Mock event happened: {message}")




message = "he BTCUSDT has reached a value of X on Binance"


        
        
        
        