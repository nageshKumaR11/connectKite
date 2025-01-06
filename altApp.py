# Install the Kite Connect library: pip install kiteconnect
from kiteconnect import KiteConnect
import requests
import hashlib
import hmac
import base64

#Initialize KiteConnect with API Key
# Replace with your API key
api_key = "your_api_key"
kite = KiteConnect(api_key=api_key)

# Get the login URL
login_url = kite.login_url()
print(f"Login URL: {login_url}")

#Step 3: Redirect User to Kite Login
#Direct the user to the login_url generated above. 
# This step is typically done in a web application.
# After successful login, 
# the user will be redirected to the redirect URL with the request token as a query parameter.

# example uel = https://your_redirect_url.com/?status=success&request_token=abcdef123456

#Extract the request_token from the redirect URL.
request_token="abcdef123456"

#Step 4: Generate Access Token
# Exchange Request Token for Access Token
# Send a POST request to the Kite Connect API to exchange the request_token for an access_token.

# API secret from Kite Connect dashboard
api_secret = "your_api_secret"

# Generate the hash signature for verification
token_signature = hmac.new(
    api_secret.encode(),
    (api_key + request_token).encode(),
    hashlib.sha256
).hexdigest()

# Get the access_token using the KiteConnect SDK
try:
    data = kite.generate_session(request_token=request_token, api_secret=api_secret)
    access_token = data["access_token"]
    print(f"Access Token: {access_token}")
    print(f"User Data: {data['user_id']}")
except Exception as e:
    print(f"Error: {e}")

# Store Access Token for Subsequent Requests
# The access_token is required for all API calls. 
# Store it securely for the current session or day.

# Set the access token for subsequent API calls
kite.set_access_token(access_token)

#  Use Access Token for API Calls
# Now that you have the access_token, you can make API calls to interact with Zerodha's systems.

# Example: Fetching User Profile
try:
    profile = kite.profile()
    print("User Profile:", profile)
except Exception as e:
    print(f"Error: {e}")
