items = ["apple", "banana", "apple", "cherry", "banana"]
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items)
