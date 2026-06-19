# group_analysis.py
# Task 3: Groupby analysis

import pandas as pd
import os

folder = os.path.dirname(__file__)

# Load datasets
customers = pd.read_csv(os.path.join(folder, "customers.csv"))
products = pd.read_csv(os.path.join(folder, "products.csv"))
orders = pd.read_csv(os.path.join(folder, "orders.csv"))

# Merge datasets
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

# --------------------------------
# Sales by region
# --------------------------------

print("\nSales by Region:")
region_sales = merged.groupby(
    "region"
)["revenue"].sum()

print(region_sales)

# --------------------------------
# Sales by category
# --------------------------------

print("\nSales by Category:")
category_sales = merged.groupby(
    "category"
)["revenue"].sum()

print(category_sales)

# --------------------------------
# Sales by customer segment
# --------------------------------

print("\nSales by Segment:")
segment_sales = merged.groupby(
    "segment"
)["revenue"].sum()

print(segment_sales)

# --------------------------------
# Multi-level Groupby
# Region + Category
# --------------------------------

print("\nMulti-Level Groupby (Region + Category):")

multi_group = merged.groupby(
    ["region", "category"]
)["revenue"].sum()

print(multi_group)

# Business insights
print("\nBusiness Notes:")
print("- Region sales show strongest market areas")
print("- Category sales identify top product groups")
print("- Segment analysis shows customer behavior")
print("- Multi-level grouping combines dimensions")