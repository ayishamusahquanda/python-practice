regions = ["Greater Accra", "Eastern", "Central", "Greater Accra", "Eastern", "Ashanti"]

order_counts = {}

for region in regions:
    if region in order_counts:
        order_counts[region] += 1
    else:
        order_counts[region] = 1

print(order_counts)
