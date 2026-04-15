import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    client._timestamp_offset = 1000

    # IMPORTANT: connect to testnet
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client