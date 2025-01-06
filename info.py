from kiteconnect import KiteConnect

# 1. Initialize Kite Connect
api_key = "your_api_key"  # Replace with your API key   visit    https://developers.kite.trade/create for getting keys
api_secret = "your_api_secret"  # Replace with your API secret
kite = KiteConnect(api_key=api_key)

# Generate session token manually
print("Login URL:", kite.login_url())
request_token = input("Enter the request token from the URL: ")
data = kite.generate_session(request_token, api_secret=api_secret)
access_token = data["access_token"]
kite.set_access_token(access_token)

# 2. Fetch Live Price
def fetch_live_price(symbol):
    try:
        instruments = kite.ltp(f"NSE:{symbol}")
        last_price = instruments[f"NSE:{symbol}"]["last_price"]
        print(f"Live price for {symbol}: {last_price}")
    except Exception as e:
        print(f"Error fetching live price: {e}")

# 3. Fetch Market Depth (Order Book)
def fetch_market_depth(symbol):
    try:
        depth = kite.quote(f"NSE:{symbol}")
        buy_orders = depth[f"NSE:{symbol}"]["depth"]["buy"]
        sell_orders = depth[f"NSE:{symbol}"]["depth"]["sell"]

        print(f"Market Depth for {symbol}:")
        print("Buy Orders:")
        for order in buy_orders:
            print(order)

        print("\nSell Orders:")
        for order in sell_orders:
            print(order)
    except Exception as e:
        print(f"Error fetching market depth: {e}")

# 4. Fetch Historical Data
def fetch_historical_data(symbol, interval, start_date, end_date):
    try:
        historical_data = kite.historical_data(
            instrument_token=kite.ltp(f"NSE:{symbol}")[f"NSE:{symbol}"]["instrument_token"],
            from_date=start_date,
            to_date=end_date,
            interval=interval
        )
        print(f"Historical Data for {symbol}:")
        for data in historical_data:
            print(data)
    except Exception as e:
        print(f"Error fetching historical data: {e}")

# Run the functions
if __name__ == "__main__":
    stock_symbol = "INFY"  # Replace with the desired stock symbol
    # fetch_live_price(stock_symbol)
    # fetch_market_depth(stock_symbol)

    # Historical data example
    fetch_historical_data(stock_symbol, "day", "2023-12-01", "2023-12-31")
