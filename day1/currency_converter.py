exchange_rate = 0.085
amount_ghs = float(input("Enter the amount in GHS: "))
converted_amount = amount_ghs * exchange_rate


if amount_ghs < 0:
    print("Error: Amount cannot be negative.")
else:
    print(f"{amount_ghs} GHS is equal to {converted_amount:.2f} USD.")


