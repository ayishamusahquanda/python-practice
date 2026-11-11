## Structure
- `day1/` — variables, data types, input/output, operators, conditionals
- `day2/` — loops, lists, tuples, dictionaries, functions
- `day3/` — file I/O, `csv` module, error handling, modules/pip
- `project/` — `api_to_csv.py` (World Bank API → CSV) and its output


## Day 1 — Basics
**What I learned:** Variables, data types, input/output, operators, and if/elif/else. I also learned how to handle edge cases like division by zero and invalid user input.

**What was difficult:** Getting the order of the `if/else` logic right (like in the BMI and currency converter) so it checks for errors before doing the math.


## Day 2 — Loops, lists, dicts, functions
**What I learned:** How to use for and while loops, store data in lists and dictionaries, and write reusable functions with parameters and return values. I also learned how to handle infinite loops and scope (variables inside vs outside functions).

**What was difficult:** The logic for the sum of digits and finding min/max without built-in functions was difficult to comprehend. Remembering to return values in the correct order was quite tricky.


## Day 3 — Files, errors, modules
**What I learned:** How to read CSV files using the `csv` module, handle file errors with `try/except`, and process real data into dictionaries to calculate totals and sort results.
**What was difficult:** Remembering that CSV files read numbers as strings, so I had to convert `Quantity` to `int` and `UnitPrice_GHS` to `float` before doing the math. Overall, this part was confusing.

## Day 4 / Project — JSON & APIs
**What I learned:** How to use the `requests` library to fetch live JSON data from a public API (World Bank), parse nested JSON structures, and save formatted data to a CSV using `csv.DictWriter`. I also learned how to organize code into separate functions (`fetch_data`, `transform`, `save_to_csv`).
**What was difficult:**  Understanding the structure of the JSON response (the actual data was inside `data[1]`), and dealing with the Python environment path issues between Anaconda and the base Python installation.

## Project — API to CSV
**Description:** A Python script that fetches Ghana's population data from the World Bank API, extracts the year and population values, and saves the results to `output/ghana_population.csv`. It handles errors like missing internet or bad responses and prints a short summary of the data.



## Exercises index
     Day 1
* `calculator.py` - Simple calculator with error handling
* `grade_checker.py` - Grade evaluator with validation
* `currency_converter.py` - GHS to USD converter
* `even_odd.py` - Even/odd number checker
* `age_checker.py` - Age eligibility checker
* `bmi_calculator.py` - BMI calculator with category

    Day 2
* `multiplication_table.py` - Loop practice
* `fizzbuzz.py` - Classic logic test
* `area_function.py` - Basic function
* `total_sales.py` - Summing a list
* `orders_per_region.py` - Dictionary counting
* `min_max_custom.py` - Finding min/max without built-ins
* `reverse_string.py` - String slicing
* `count_vowels.py` - String iteration
* `remove_duplicates.py` - List deduplication
* `factorial_loop.py` - Math with loops
* `prime_checker.py` - Prime number logic
* `temp_converter.py` - Function-based math
* `sum_of_digits.py` - While loop math
* `word_frequency.py` - Dictionary counting words
* `shopping_cart.py` - While loop with lists

    Day 3
* `csv_report.py` - Reading a CSV file and calculating total revenue, revenue by region, and top products.

    Project
* `project/api_to_csv.py` - Fetches World Bank data and exports it to a CSV file.