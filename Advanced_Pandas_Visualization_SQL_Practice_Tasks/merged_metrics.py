# merged_metrics.py
# Task 4: Merge tables and calculate metrics

import pandas as pd
import os

folder = os.path.dirname(__file__)

# Load datasets
customers = pd.read_csv(os.path.join(folder, "customers.csv"))
products = pd.read_csv(os.path.join(folder, "products.csv"))
orders = pd.read_csv(os.path.join(folder, "orders.csv"))

# Merge all tables
merged = orders.merge(
    customers,
    on="customer_id"
).merge(
    products,
    on="product_id"
)

# Create revenue column
merged["revenue"] = merged["quantity"] * merged["price"]

print("Merged Analysis Table:")
print(merged)

# -----------------------------
# Total Revenue
# -----------------------------

total_revenue = merged["revenue"].sum()

print("\nTotal Revenue:")
print(f"₹{total_revenue:,.2f}")

# -----------------------------
# Average Order Value
# -----------------------------

avg_order_value = merged["revenue"].mean()

print("\nAverage Order Value:")
print(f"₹{avg_order_value:,.2f}")

# -----------------------------
# Top Selling Products
# -----------------------------

top_products = (
    merged.groupby("product_name")
    ["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Selling Products:")
print(top_products)

# -----------------------------
# Top 3 Products by Revenue
# -----------------------------

top_revenue_products = (
    merged.groupby("product_name")
    ["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print("\nTop 3 Products by Revenue:")
print(top_revenue_products)

# Business notes
print("\nBusiness Notes:")
print("- Total revenue measures overall business performance")
print("- Average order value estimates customer spending")
print("- Top-selling products identify demand")