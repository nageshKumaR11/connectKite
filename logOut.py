from kiteconnect import KiteConnect

# Initialize Kite Connect
api_key = "your_api_key"
kite = KiteConnect(api_key=api_key)

# Set the access token (obtained during login)
access_token = "your_access_token"
kite.set_access_token(access_token)

# Log out
try:
    kite.logout()
    print("Successfully logged out!")
except Exception as e:
    print(f"Error during logout: {e}")
