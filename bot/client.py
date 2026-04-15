from binance.client import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Validate keys
if not API_KEY or not API_SECRET:
    raise ValueError("API_KEY and API_SECRET must be set in .env file")

# Create Binance client
client = Client(API_KEY, API_SECRET)

# Set Futures Testnet URL (IMPORTANT)
client.FUTURES_URL = "https://testnet.binancefuture.com"