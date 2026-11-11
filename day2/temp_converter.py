def celsius_to_fahrenheit(celsius):
    return round((9 * celsius) / 5 + 32, 1)

def fahrenheit_to_celsius(fahrenheit):
    return round((5 * (fahrenheit - 32)) / 9, 1)
unit = input ("Is the temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9*temp)/5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((5*(temp-32))/9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is not a valid unit of measurement.")