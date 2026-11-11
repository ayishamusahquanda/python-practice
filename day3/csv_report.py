import csv

def generate_report(filename):
    total_revenue = 0
    revenue_by_region = {}
    product_sales = {}
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                quantity = int(row["Quantity"])
                price = float(row["UnitPrice_GHS"])
                revenue = quantity * price
                total_revenue += revenue
                
                region = row["Region"]
                if region in revenue_by_region:
                    revenue_by_region[region] += revenue
                else:
                    revenue_by_region[region] = revenue
                product = row["Product"]

                if product in product_sales:
                    product_sales[product] += quantity
                else:
                    product_sales[product] = quantity
                    
        print(f"Total Revenue: GHS {total_revenue:,.2f}\n")
        
        print("Revenue by Region:")
        for region, rev in revenue_by_region.items():
            print(f"  - {region}: GHS {rev:,.2f}")
            
        sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
        top_5 = sorted_products[:5]
        
        print("\nTop 5 Products (by quantity sold):")
        for i, (prod, qty) in enumerate(top_5, 1):
            print(f"  {i}. {prod}: {qty} units")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError as e:
        print(f"Error: There is bad data in the CSV file (could not convert to number). Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

generate_report("day3/cleaned_data.csv")