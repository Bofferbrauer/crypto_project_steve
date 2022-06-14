# from crypto.data.source import DataSource
import requests
import json

class Binance():
    req = requests.get("https://api.binance.com/api/v3/depth")
    print(req)