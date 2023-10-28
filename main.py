from utils import binance_utils, discord_utils
from strategies import simple_strategy

# TODO: 定义交易对和其他变量
symbol = 'BTCUSDT'

# 获取当前价格
price = binance_utils.get_current_price(symbol)

# 根据策略决定买卖
if simple_strategy.should_buy(symbol, price):
    order = binance_utils.place_order(symbol, 'BUY', quantity)
    discord_utils.send_message(f'Bought {symbol} at {order["price"]}')
elif simple_strategy.should_sell(symbol, price):
    order = binance_utils.place_order(symbol, 'SELL', quantity)
    discord_utils.send_message(f'Sold {symbol} at {order["price"]}')

# 运行Discord客户端
discord_utils.client.run(discord_config.TOKEN)
