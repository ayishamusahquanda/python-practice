values = [4, 8, 15, 16, 23, 42]

def find_min_max(numbers):

    highest = numbers[0]
    lowest = numbers[0]

    for num in numbers:
        if num > highest:
            highest = num

        if num < lowest:
            lowest = num

    return highest, lowest

high, low = find_min_max(values)
print(f"Highest: {high}, Lowest {low}")
    
