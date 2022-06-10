from abc import abstractmethod

# Setting up a Sender which will send a base message
class Sender():
    @abstractmethod
    def send(self):
        pass

# Creating a Mocksender based on the Sender
class Mocksender(Sender):
    def send(self, message):
        print(f"Sent using the Mock sender: {message}")


# Testing the Mocksender and abstract Sender classes
# message = "Test"

# mock_sender = Mocksender()
# mock_sender.send(message)
        
        