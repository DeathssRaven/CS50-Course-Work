import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    value = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")


try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=39b82621d2f2b97fc57ad18353424f639c52e8eb65d3ae306ac3f6e45bb3d43a")
    price = float(response.json()['data']['priceUsd'])
    result = value * price
    print(f"${result:,.4f}")

except requests.RequestException:
    pass
