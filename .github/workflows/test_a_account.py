# test_a_account.py
import os
from alpaca.trading.client import TradingClient

client = TradingClient(os.environ["APCA_API_KEY_ID"],
                       os.environ["APCA_API_SECRET_KEY"],
                       paper=True)

acct = client.get_account()
print("status:", acct.status)
print("buying_power:", acct.buying_power)
print("cash:", acct.cash)
print("positions:", len(client.get_all_positions()))
