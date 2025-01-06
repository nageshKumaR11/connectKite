# Zerodha Kite Connect API Integration

This project demonstrates how to use the Zerodha Kite Connect API to fetch market data and perform various operations such as fetching live stock prices, market depth, and historical data.

## Features

### Login
- Authenticates using the **API key**, **API secret**, and manually generated session token.
- Generates an access token for subsequent API requests.

### Live Price
- Fetches the latest stock price for a given symbol (e.g., "INFY" for Infosys).

### Market Depth
- Retrieves the order book (buy and sell orders with price and quantity details).

### Historical Data
- Fetches historical price data for a stock in the specified date range and interval (e.g., "day," "minute").

---

## Key Functions

### `fetch_live_price(symbol)`
Fetches and prints the current market price for a given symbol.

### `fetch_market_depth(symbol)`
Retrieves and displays the top buy and sell orders for the given symbol.

### `fetch_historical_data(symbol, interval, start_date, end_date)`
Fetches OHLC (Open, High, Low, Close) and volume data for a stock in the specified date range and interval.

---

## How to Obtain the Request Token

1. **Generate Login URL**:
   After initializing the Kite Connect object, generate a login URL:
   ```python
   print("Login URL:", kite.login_url())
   ```
   
   Visit this URL to log in to Zerodha. After successful login, you'll be redirected to the redirect URL specified in your Kite Connect app configuration.

2. **Extract the Request Token**:
   The redirect URL will contain the request token as a query parameter, for example:
   ```
   https://your_redirect_url.com/?request_token=abcdef123456&status=success
   ```
   Extract the value of the `request_token` parameter (e.g., `abcdef123456`).

3. **Generate Access Token**:
   Use the request token to generate the access token:
   ```python
   data = kite.generate_session(request_token="abcdef123456", api_secret="your_api_secret")
   access_token = data["access_token"]
   ```
   The `access_token` is what you'll use for all subsequent API requests.

---

## Important Notes

### Token Usage and Validity
- **Single Use**: The request token is valid for a single use and must be exchanged for an access token within a few minutes.
- **Access Token Duration**: The access token is valid for one trading day, after which you'll need to repeat the process to generate a new one.

### Zerodha API Rate Limits
- **Retail Plan**: 3 requests per second.
- **Premium Plan**: 10 requests per second.

---

## Automating the Process
For production systems, you may need to:
- Automate request token retrieval (requires manual intervention due to Zerodha's security policies).
- Use tools like OAuth token refreshers to streamline token generation.

---

## Example Code
### Fetch Live Price
```python
fetch_live_price("INFY")
```

### Fetch Market Depth
```python
fetch_market_depth("INFY")
```

### Fetch Historical Data
```python
fetch_historical_data("INFY", "day", "2023-12-01", "2023-12-31")
