from abc import abstractmethod
# from crypto.message_delivery.sender import message

# Setting up an Event handler that will take the message from the Sender and handles it
class Event():
    
    def __init__(self, senders, data_source): # TODO Add senders and data_source later
        self.senders = senders
        self.data_source = data_source
        # pass


    @property
    @abstractmethod # ? this was the supposed way to do it
    # @abstractproperty # ! Depreciated, do not use anymore
    def condition(self) -> None:
        pass
    
    @property
    @abstractmethod
    def message(self) -> None:
        # print(f"This is the alert with the code: {alert}") # ! Not in an abstract method!
        pass
    
    # Checking if the Class is working
    def check(self) -> str:
        if self.condition:
            for senders in self.senders:
                senders.send(self.message)
            for data in self.data_source:
                data.send(self.message)
                
#                print("It works!")

        
                       

# Setting up the Mock Event, which will add a message to to the one from the Sender

class MockEvent(Event):

    @property
    def condition(self) -> bool:
        return True

    # Adding the message the MockEvent will send
    @property    
    def message(self) -> str:
        message = "The BTCUSDT has reached a value of X on Binance"
        return message






        
        
        
        