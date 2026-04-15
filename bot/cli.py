import argparse
import logging
from bot.validators import validate_order
from bot.orders import place_market_order, place_limit_order
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    order_type = args.type.upper()
    side = args.side.upper()

    try:
        validate_order(args.symbol, side, order_type, args.quantity, args.price)
        logging.info(f"Request: {args}")
    except Exception as e:
        print("Validation Error:", e)
        logging.error(f"Validation Error: {e}")
        return

    if order_type == "MARKET":
        result = place_market_order(args.symbol, side, args.quantity)

    elif order_type == "LIMIT":
        result = place_limit_order(args.symbol, side, args.quantity, args.price)

    else:
        print("Invalid order type")
        logging.error("Invalid order type")
        return

    # OUTPUT
    print("\n===== ORDER SUMMARY =====")
    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {side}")
    print(f"Type     : {order_type}")
    print(f"Quantity : {args.quantity}")
    if order_type == "LIMIT":
        print(f"Price    : {args.price}")

    print("\n===== ORDER RESPONSE =====")
    print(f"Order ID     : {result.get('orderId')}")
    print(f"Status       : {result.get('status')}")
    print(f"Executed Qty : {result.get('executedQty')}")
    print(f"Avg Price    : {result.get('avgPrice')}")

    if "orderId" in result:
        print("\n✅ Status: SUCCESS")
    else:
        print("\n❌ Status: FAILED")

    logging.info(f"Response: {result}")


if __name__ == "__main__":
    main()