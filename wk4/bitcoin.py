import json
import sys
import requests


def main():

    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    else:
        try:
            usd = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        else:
            rate_float = 0
            try:
                request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                response = request.json()
                rate_float = response["bpi"]["USD"]["rate_float"]
            except requests.RequestException:
                sys.exit("Error during request")
            else:
                amount = usd * rate_float
                print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
