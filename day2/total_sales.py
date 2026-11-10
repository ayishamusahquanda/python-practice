sales = [100.50, 200.75, 300.25, 250.90, 290.05]


def calculate_total(sales):
    total = 0
    for s in sales:
        total += s
    return total

total_sales = calculate_total(sales)
print(f"The total sales amount is: ${total_sales:.2f}")
