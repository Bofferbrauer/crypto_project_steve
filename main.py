from crypto.message_delivery.sender import Mocksender
from crypto.market_events.event import MockEvent
from crypto.app import App

# For testing
# events_list = ["TestTestTest123"]
# senders_list = ["Kosmas"]

mock_senders = [Mocksender()]
# mock_senders.send(events_list[0])
events = [MockEvent(mock_senders)]

# Taking the message from the event and sets the time interval at which it will be updated/published
app = App(events, 5)

app.start()


