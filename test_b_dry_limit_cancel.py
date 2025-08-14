# test_b_dry_limit_cancel.py
import os
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

client = TradingClient(os.environ["APCA_API_KEY_ID"],
                       os.environ["APCA_API_SECRET_KEY"],
                       paper=True)

# Limit far from market so it won't fill
req = LimitOrderRequest(symbol="SPY", qty=1, side=OrderSide.BUY,
                        time_in_force=TimeInForce.DAY, limit_price="1.00")
o = client.submit_order(req)
print("Placed dry limit (should not fill):", o.id)

client.cancel_order_by_id(o.id)
print("Canceled:", o.id)
