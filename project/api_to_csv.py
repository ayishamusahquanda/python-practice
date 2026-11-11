import csv
import os
import requests

URL = "https://api.worldbank.org/v2/country/GH/indicator/SP.POP.TOTL?format=json&per_page=100"

def fetch_data(url):
    print("Fetching data from World Bank API...")
    try:
        response = requests.get(url, timeout=10)
        # This checks if the status code is 200 (OK)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def transform(data):
    """Extracts year and population from the raw API JSON."""
    if not data or len(data) < 2:
        print("Error: Unexpected data format from API.")
        return []

    rows = []
    for entry in data[1]:
        year = entry.get("date")
        population = entry.get("value")
        
        if population is not None:
            rows.append({"year": int(year), "population": population})
    
    rows.sort(key=lambda x: x["year"])
    return rows

def save_to_csv(rows, filepath):
    """Saves the transformed data to a CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    try:
        with open(filepath, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["year", "population"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Successfully saved {len(rows)} rows to {filepath}")
    except OSError as e:
        print(f"Error saving file: {e}")

def main():
    """Main function to run the script."""
    data = fetch_data(URL)
    
    if data:
        rows = transform(data)
        if rows:
            filepath = "project/output/ghana_population.csv"
            save_to_csv(rows, filepath)
            
            print("\n--- Summary ---")
            print(f"Total rows saved: {len(rows)}")
            print(f"Earliest year: {rows[0]['year']}")
            print(f"Latest year: {rows[-1]['year']}")
            
            highest = max(rows, key=lambda x: x["population"])
            print(f"Highest population: {highest['population']:,} (in {highest['year']})")

if __name__ == "__main__":
    main()