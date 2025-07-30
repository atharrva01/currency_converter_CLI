import requests
import argparse

parser = argparse.ArgumentParser(description="This is a currency converter CLI")

parser.add_argument("--currency" , required= True , help = "Add the currency from which you want your amount to get converted.")
parser.add_argument("--to" , required= True , help = "Add the currency to which you want your amount to get converted.")
parser.add_argument("--amount" , required= True , help = "Add the amount which you want to get converted.")

args = parser.parse_args()

api = "9220***************46520f"

currency = (args.currency).upper()

convert_currency = (args.to).upper()

amount = float((args.amount))

url = f"https://v6.exchangerate-api.com/v6/{api}/latest/{currency}"

data = requests.get(url).json()

try: 

    convert_currency_val = data["conversion_rates"][convert_currency]

    result = amount * convert_currency_val

    print(f"The amount converted from {currency} to {convert_currency}, the converted amount is {round(result ,2)}")
    
except Exception as e:
    print(f"{e}, Enter correct Currency code.")
    exit()
