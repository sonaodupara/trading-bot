def validate_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    # Symbol check
    if not symbol:
        raise ValueError("Symbol is required")

    # Side check
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    # Order type check
    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP")

    # Quantity check
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    # LIMIT order validation (KEEP THIS)
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if price <= 0:
            raise ValueError("Price must be greater than 0")

    # STOP order validation (FIXED)
    if order_type == "STOP":
        if stop_price is None:
            raise ValueError("STOP order requires stop_price")
        if stop_price <= 0:
            raise ValueError("stop_price must be greater than 0")