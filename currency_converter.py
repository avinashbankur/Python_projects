import requests

def convert_to_all_no_key(from_currency, amount):
    url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"

    try:
        print(f"Fetching rates for base currency: {from_currency.upper()} ...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("result") != "success" or "rates" not in data:
            print("❌ Failed to get rates. Server response:")
            print(data)
            return

        rates = data["rates"]
        print(f"\n💱 {amount} {from_currency.upper()} — current rates:\n")
        for currency in sorted(rates):
            converted = amount * rates[currency]
            print(f"{currency}: {converted:.2f}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    from_cur = input("Enter source currency (e.g., USD): ").strip()
    try:
        amt = float(input("Enter amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a number.")
        exit(1)

    convert_to_all_no_key(from_cur, amt)
