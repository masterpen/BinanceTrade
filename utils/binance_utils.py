from binance.client import Client
from config import binance_config

client = Client(binance_config.API_KEY, binance_config.SECRET_KEY)

def place_order(symbol, side, quantity, price=None):
    """Place an order on Binance."""
    if price:
        order = client.order_limit(
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=price
        )
    else:
        order = client.order_market(
            symbol=symbol,
            side=side,
            quantity=quantity
        )
    return order
