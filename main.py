from crypto.message_delivery.sender import Mocksender
from crypto.market_events.event import MockEvent
from crypto.app import App

# For testing
# events_list = ["TestTestTest123"]
# senders_list = ["Kosmas"]

# Getting the message from the sender
mock_senders = [Mocksender()]
# mock_senders.send(events_list[0])

# Getting the event linked to the message
events = [MockEvent(mock_senders)]

# Taking the message from the event and sets the time interval at which it will be updated/published
app = App(events, 5) # ! Since there is no stop condition anywhere, this will loop indefinitely and print the mock message every 5 seconds. Type Ctrl+C repeatedly to make VSCode stop the program.

app.start()


