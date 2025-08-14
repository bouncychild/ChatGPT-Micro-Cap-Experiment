# test_c_tiny_trade.py
import os
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

client = TradingClient(os.environ["APCA_API_KEY_ID"],
                       os.environ["APCA_API_SECRET_KEY"],
                       paper=True)

def buy_small():
    # Try fractional $5 on SPY
    try:
        req = MarketOrderRequest(symbol="SPY", notional=5,
                                 side=OrderSide.BUY, time_in_force=TimeInForce.DAY)
        o = client.submit_order(req)
        print("Fractional SPY $5 order id:", o.id)
        return "SPY", None  # notional order
    except Exception as e:
        print("Fractional failed -> buying 1 cheap share:", e)
        cheap = "SIRI"   # typically a few dollars
        req = MarketOrderRequest(symbol=cheap, qty=1,
                                 side=OrderSide.BUY, time_in_force=TimeInForce.DAY)
        o = client.submit_order(req)
        print(f"Bought 1 share of {cheap}: id={o.id}")
        return cheap, 1

def sell_if_held(symbol):
    # Sell whatever we hold for this symbol (qty can be fractional; use string)
    for p in client.get_all_positions():
        if p.symbol == symbol:
            req = MarketOrderRequest(symbol=symbol, qty=p.qty,
                                     side=OrderSide.SELL, time_in_force=TimeInForce.DAY)
            o = client.submit_order(req)
            print(f"SOLD {symbol} qty={p.qty}: id={o.id}")
            return

sym, _ = buy_small()

# Optional: comment out the next line if you want to leave the position open
sell_if_held(sym)
