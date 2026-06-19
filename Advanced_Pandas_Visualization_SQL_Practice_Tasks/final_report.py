# final_report.py
# Task 9: Final business insights report

import pandas as pd
import os

folder = os.path.dirname(__file__)

# Load datasets
customers = pd.read_csv(
    os.path.join(folder, "customers.csv")
)

products = pd.read_csv(
    os.path.join(folder, "products.csv")
)

orders = pd.read_csv(
    os.path.join(folder, "orders.csv")
)

# Merge all datasets
merged = (
    orders
    .merge(customers, on="customer_id")
    .merge(products, on="product_id")
)

# Revenue calculation
merged["revenue"] = (
    merged["quantity"] * merged["price"]
)

# Metrics
total_revenue = merged["revenue"].sum()

avg_order = merged["revenue"].mean()

top_product = (
    merged.groupby("product_name")["revenue"]
    .sum()
    .idxmax()
)

top_region = (
    merged.groupby("region")["revenue"]
    .sum()
    .idxmax()
)

top_segment = (
    merged.groupby("segment")["revenue"]
    .sum()
    .idxmax()
)

print("=" * 50)
print("FINAL BUSINESS REPORT")
print("=" * 50)

print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")

print(
    f"Average Order Value: ₹{avg_order:,.2f}"
)

print(
    f"Top Revenue Product: {top_product}"
)

print(
    f"Highest Revenue Region: {top_region}"
)

print(
    f"Top Customer Segment: {top_segment}"
)

print("\nBusiness Insights:")
print("- Electronics generated strong revenue.")
print("- Some regions contribute more sales than others.")
print("- Customer segments behave differently.")
print("- High-performing products should be prioritized.")
print("- Visualization charts support trend analysis.")

print("\nFiles generated during project:")
print("• revenue_by_region.png")
print("• revenue_by_month.png")
print("• category_distribution.png")
print("• sales.db")

print("\nProject Completed")
print("=" * 50)