import requests

def currency_converter(amount, from_curr, to_curr):
    # use a free api
    url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
    response = requests.get(url)
    data = response.json()
    
    rate = data['rates'][to_curr]
    converted_amount = amount * rate
    return converted_amount

print("--- Real-time Currency Converter ---")
try:
    amt = float(input("Enter the amount of money: "))
    from_c = input("from which currency? (like: USD): ").upper()
    to_c = input("which currency? (like: BDT): ").upper()

    result = currency_converter(amt, from_c, to_c)
    print(f"{amt} {from_c} = {result:.2f} {to_c}")
except:
    print("Error: enter the right currency code or check internet.") 