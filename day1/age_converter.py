age = int(input("Enter your age: "))

if  age < 0:
    print("Error: Age cannot be negative.")

elif age < 18:
    print("You are a minor")

elif 18 <= age < 65:
    print("You are an adult and eligible to vote")


else:
    print("You are a senior citizen")