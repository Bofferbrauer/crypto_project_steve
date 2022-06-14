from crypto.data.source import DataSource # ? Can't find it and throws an error if tested
import requests
import json

class Binance(DataSource):
    req = requests.get("https://api.binance.com/api/v3/depth")
    print(req)