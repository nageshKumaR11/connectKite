from kiteconnect import KiteConnect
import time

# 1. Initialize Kite Connect
api_key = "your_api_key"  # Replace with your API key
api_secret = "your_api_secret"  # Replace with your API secret
kite = KiteConnect(api_key=api_key)

# Generate session token manually
print("Login URL:", kite.login_url())
request_token = input("Enter the request token from the URL: ")
data = kite.generate_session(request_token, api_secret=api_secret)
access_token = data["access_token"]
kite.set_access_token(access_token)

# 2. Function to fetch live market data
def get_live_price(symbol):
    instruments = kite.ltp(f"NSE:{symbol}")
    return instruments[f"NSE:{symbol}"]["last_price"]

# 3. Function to place a buy/sell order
def place_order(symbol, transaction_type, quantity):
    try:
        order_id = kite.place_order(
            tradingsymbol=symbol,
            exchange="NSE",
            transaction_type=transaction_type,  # "BUY" or "SELL"
            quantity=quantity,
            order_type="MARKET",
            product="MIS"  # MIS for intraday
        )
        print(f"Order placed successfully. Order ID: {order_id}")
    except Exception as e:
        print(f"Order placement failed: {e}")

# 4. Main algorithm logic
def trading_algo():
    symbol = "INFY"  # Example: Infosys
    quantity = 1  # Number of shares to trade
    target_profit = 0.5  # Target profit in percentage
    stop_loss = 0.5  # Stop loss in percentage

    # Fetch initial price
    initial_price = get_live_price(symbol)
    print(f"Monitoring {symbol} at price: {initial_price}")

    while True:
        try:
            current_price = get_live_price(symbol)
            price_change = ((current_price - initial_price) / initial_price) * 100
            print(f"Current Price: {current_price}, Change: {price_change:.2f}%")

            # Buy if price drops by stop-loss %
            if price_change <= -stop_loss:
                print(f"Triggering Buy Order for {symbol} at {current_price}")
                place_order(symbol, "BUY", quantity)
                break

            # Sell if price rises by target-profit %
            elif price_change >= target_profit:
                print(f"Triggering Sell Order for {symbol} at {current_price}")
                place_order(symbol, "SELL", quantity)
                break

            # Sleep to avoid excessive API calls
            time.sleep(10)
        except Exception as e:
            print(f"Error during monitoring: {e}")
            break

# Run the algorithm
if __name__ == "__main__":
    trading_algo()
