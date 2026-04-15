from bot.client import client


# MARKET ORDER
def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        return order
    except Exception as e:
        return {"error": str(e)}


# LIMIT ORDER
def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        return order
    except Exception as e:
        return {"error": str(e)}


# STOP-LIMIT ORDER (BONUS)
def place_stop_limit_order(symbol, side, quantity, price, stop_price):
    from bot.client import client

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP_MARKET",   # ✅ FIXED
            quantity=quantity,
            stopPrice=stop_price,
            timeInForce="GTC"
        )
        return order
    except Exception as e:
        return {"error": str(e)}