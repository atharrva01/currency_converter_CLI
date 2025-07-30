# 💱 Currency Converter CLI Tool

A simple Python CLI app to convert currencies in real time using the ExchangeRate-API.

## 🚀 Features

- Real-time currency conversion
- Command line interface using `argparse`
- Error handling for invalid currency codes
- Case-insensitive currency inputs

## 🧠 How It Works

The script takes in:
- `--currency` : The base currency (e.g. USD)
- `--to` : The target currency (e.g. INR)
- `--amount` : The amount to convert

Then it fetches the latest exchange rates using ExchangeRate-API and calculates the converted amount.

## 🛠️ Usage

python currency_converter.py --currency USD --to INR --amount 100

## 🧪 Example Output

The amount converted from USD to INR, the converted amount is 8293.12

## 🔗 API Used

ExchangeRate API

⚠️ You’ll need to sign up and replace api key with your own for it to work.

## 📌 Author

Atharva — Python Automation & CLI Tools 🔧
