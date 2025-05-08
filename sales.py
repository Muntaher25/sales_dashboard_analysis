import pandas as pd
import random

# Load your original CSV (update path if needed)
df = pd.read_csv("sales_data_dashboard.csv")

# Set product-wise price ranges
price_ranges = {
    "Laptop": (900, 1200),
    "Smartphone": (500, 700),
    "Headphones": (80, 120),
    "Monitor": (200, 300),
    "Keyboard": (40, 60),
    "Mouse": (20, 40)
}

# Function to generate random revenue
def generate_revenue(row):
    min_price, max_price = price_ranges[row["product"]]
    price = random.randint(min_price, max_price)
    return row["quantity"] * price

# Apply function to calculate revenue
df["revenue"] = df.apply(generate_revenue, axis=1)

# Save the updated CSV
df.to_csv("sales_data_dashboard_updated.csv", index=False)
print("Revenue column added and file saved as 'sales_data_dashboard_updated.csv'")
