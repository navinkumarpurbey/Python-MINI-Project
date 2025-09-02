# Simple Currency Converter (USD to NPR, INR, EUR)

def currency_converter(amount, currency):
    rates = {
        "NPR": 133.5,   # Example rate for Nepalese Rupee
        "INR": 83.2,    # Example rate for Indian Rupee
        "EUR": 0.92     # Example rate for Euro
    }

    if currency in rates:
        converted = amount * rates[currency]
        print(f"{amount} USD = {converted:.2f} {currency}")
    else:
        print("❌ Currency not supported!")

# Example usage
usd = float(input("Enter amount in USD: "))
currency = input("Enter currency (NPR/INR/EUR): ").upper()

currency_converter(usd, currency)
