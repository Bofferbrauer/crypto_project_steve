from crypto.data.source import DataSource, OrderBook, Pair # ? Can't find it and throws an error if tested
import requests
import json

class Binance(DataSource):

    # Testing the link:
    # req = requests.get("https://api.binance.com/api/v3/depth")
    # print(req)

    def get_order_book(self, pair : Pair) -> OrderBook:
        pair = self.pair
        api_address = "https://api.binance.com"
        api_endpoint = "api/v3/depth"


        