from abc import abstractmethod


class Sender():
    @abstractmethod
    def send(self, message):
        pass

class Mocksender(Sender):
    def send(self, message):
        print(f"Sent using the Mock sender: {message}")


# Testing the Mocksender and abstract Sender classes
message = "Test"

mock_sender = Mocksender()
mock_sender.send(message)
        
        