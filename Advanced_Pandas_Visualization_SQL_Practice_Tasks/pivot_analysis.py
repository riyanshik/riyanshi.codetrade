# pivot_analysis.py
# Task 5: Pivot tables

import pandas as pd
import os

folder = os.path.dirname(__file__)

# Load datasets
customers = pd.read_csv(os.path.join(folder, "customers.csv"))
products = pd.read_csv(os.path.join(folder, "products.csv"))
orders = pd.read_csv(os.path.join(folder, "orders.csv"))

# Merge tables
merged = orders.merge(
    customers,
    on="customer_id"
).merge(
    products,
    on="product_id"
)

# Revenue column
merged["revenue"] = (
    merged["quantity"] * merged["price"]
)

print("Merged Dataset:")
print(merged)

# ---------------------------------
# Pivot Table 1
# Region vs Month
# ---------------------------------

pivot1 = pd.pivot_table(
    merged,
    values="revenue",
    index="region",
    columns="month",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table 1: Revenue by Region vs Month")
print(pivot1)

# ---------------------------------
# Pivot Table 2
# Category vs Segment
# ---------------------------------

pivot2 = pd.pivot_table(
    merged,
    values="revenue",
    index="category",
    columns="segment",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table 2: Revenue by Category vs Segment")
print(pivot2)

# Notes
print("\nBusiness Notes:")
print("- Region vs Month shows seasonal performance trends")
print("- Category vs Segment shows buying patterns")