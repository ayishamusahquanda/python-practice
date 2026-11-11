number = int(input("Enter a whole number: "))
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number = number // 10

print(f"The sum of the digits is: {total}")
  
