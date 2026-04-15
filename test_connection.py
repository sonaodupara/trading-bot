from bot.orders import place_market_order, place_limit_order

print(" MARKET ORDER TEST ")
market_result = place_market_order("BTCUSDT", "BUY", 0.001)
print(market_result)

print("\n LIMIT ORDER TEST ")
limit_result = place_limit_order("BTCUSDT", "BUY", 0.001, 60000)
print(limit_result)