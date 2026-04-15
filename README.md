# Trading Bot CLI

A Python-based CLI tool to place MARKET and LIMIT orders using Binance Futures API.

---

## 🚀 Features

- Place MARKET orders
- Place LIMIT orders
- Input validation before execution
- Logging of request and response
- CLI-based interaction

---

## 🛠️ Setup

Clone the repository:

git clone https://github.com/sonaodupara/trading-bot.git
cd trading-bot

Install dependencies:

pip install -r requirements.txt

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

API_KEY=your_api_key
API_SECRET=your_api_secret

---

## ▶️ Usage

### Market Order

python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order

python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000

---

## 📁 Project Structure

bot/
├── cli.py
├── client.py
├── orders.py
├── validators.py
├── logging_config.py
├── __init__.py

main.py  
test_connection.py  
requirements.txt  
README.md  

---

## ⚠️ Notes

- Make sure your system time is synced (important for Binance API)
- Do not share your API keys publicly
- Use testnet for testing whenever possible

---

## Logs

Logs are stored in `bot.log` and include:
- Market order execution
- Limit order execution
- API request & response details

---

## 🔮 Future Improvements

- Add stop-loss and take-profit
- Add automated trading strategies
- Add unit tests

---

## 📄 License

This project is for educational purposes.