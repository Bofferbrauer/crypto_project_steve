from crypto.data.api.exchange import Binance
from crypto.data.source import OrderBook, Pair
from crypto.market_events.volume import VolumeEvent
from crypto.message_delivery.sender import Mocksender
from crypto.market_events.event import MockEvent
from crypto.app import App

# For testing
# events_list = ["TestTestTest123"]
# senders_list = ["Kosmas"]

# Getting the message from the sender
mock_senders = [Mocksender()]
# mock_senders.send(events_list[0])

# Connecting to the source API
binance = Binance()

pair = Pair(first="BTC", second="USDT")


vol_threshold = 0.5

# Getting the event linked to the message
events = [VolumeEvent(binance, mock_senders, pair, vol_threshold)]


# Testing the import branches
# # Getting the float numbers from the orders
# book_orders = OrderBook()

# # Getting the amount of Event orders
# event_volumes = VolumeEvent()

# Taking the message from the event and sets the time interval at which it will be updated/published
app = App(events, 5) # ! Since there is no stop condition anywhere, this will loop indefinitely and print the mock message every 5 seconds. Type Ctrl+C repeatedly to make VSCode stop the program.

app.start()


