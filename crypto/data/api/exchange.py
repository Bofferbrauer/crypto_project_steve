from crypto.data.source import DataSource, OrderBook, Pair
# ? Can't find it and throws an error if tested, but needed to be called in the main
import requests
import json

class Binance(DataSource):

    # Testing the link:
    # req = requests.get("https://api.binance.com/api/v3/depth")
    # print(req)

    def get_order_book(self, pair : Pair) -> OrderBook:

        # getting the base path of the API and it's extension
        api_base = "https://api.binance.com/api/v3/"
        api_endpoint = "depth"
        api_address = api_base + api_endpoint
        
        # Setting the query parameters 
        req_params = {
            "limit": 1,
            "symbol": pair.first + pair.second}

        #requesting the data from the API and turning it into a .json
        boo = requests.get(Binance.api_address, params=req_params)
        OrderBook = boo.json()

        # The data is transformed into the data for the OrderBook
        return OrderBook(
            bid = float(boo["bids"][0][0]),
            ask = float(boo["asks"][0][0]),
            bid_volume = float(boo["bids"][0][1]),
            ask_volume = float(boo["asks"][0][1])
        )

        