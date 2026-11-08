operator = input("Enter an operator (+, -, *, /): ")
first_number = float(input("Enter the 1st number: "))
second_number = float(input("Enter the 2nd number: "))

if operator == "+":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result:.2f}")

elif operator == "-":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result:.2f}")

elif operator == "*":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result:.2f}")

elif operator == "/":
    if second_number != 0:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.2f}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")