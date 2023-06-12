def currency_converter(brl_amount):
    usd_rate = 5.47
    euro_rate = 6.55
    yuan_rate = 0.86
    usd_amount = brl_amount / usd_rate
    euro_amount = brl_amount / euro_rate
    yuan_amount = brl_amount / yuan_rate
    return (usd_amount, euro_amount, yuan_amount)

brl_amount = float(input("Enter the amount in BRL: "))
usd_amount, euro_amount, yuan_amount = currency_converter(brl_amount)
print("Amount in USD: ", usd_amount)
print("Amount in EUR: ", euro_amount)
print("Amount in CNY: ", yuan_amount)