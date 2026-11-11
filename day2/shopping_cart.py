cart = []

print("Welcome to the shopping cart!")
print("Type 'done' when you are finished.\n")

while True:
    item = input("Enter an item: ")
    
    if item.lower() == "done":
        break
        
    cart.append(item)
    print(f"{item} added to cart.")

print("\n--- Your Cart ---")
print(cart)
print(f"Total items: {len(cart)}")