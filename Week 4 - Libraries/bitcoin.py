import requests
from sys import argv

def main():
    bitcoin = is_float()

    try:
        page = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        USD_rate_str = page["bpi"]["USD"]["rate"].replace("," , "")
        USD_rate = float(USD_rate_str)
        price = bitcoin * USD_rate
        print(f"${price:,.4f}")
    except requests.RequestException:
         print("Error Fetching Data")


def is_float():
        try:
            return float(argv[1])
        except ValueError:
                print("Command-line argument is not a number")
        except IndexError:
            print("Missing command-line argument")


main()

