import requests
import time

URL = "https://abhishek-ftx-btc.herokuapp.com/welcome"

while True:
    r = requests.get(url = URL)
    time.sleep(25)
