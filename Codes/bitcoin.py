import json
import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  
        data = response.json()
        price = data["bpi"]["USD"]["rate_float"]
        total_cost = bitcoins * price
        print(f"${total_cost:,.4f}")   
    except requests.RequestException:
        sys.exit("Failed to retrieve Bitcoin price")
if __name__ == "__main__":
    main()
