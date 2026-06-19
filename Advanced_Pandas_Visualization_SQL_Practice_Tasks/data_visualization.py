# data_visualization.py
# Task 6: Data visualization

import pandas as pd
import matplotlib.pyplot as plt
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
merged["revenue"] = merged["quantity"] * merged["price"]

# -------------------------
# Bar Chart
# Revenue by Region
# -------------------------

region_sales = merged.groupby("region")["revenue"].sum()

plt.figure()
region_sales.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.savefig(
    os.path.join(folder, "revenue_by_region.png")
)

# -------------------------
# Line Chart
# Revenue by Month
# -------------------------

monthly_sales = merged.groupby("month")["revenue"].sum()

plt.figure()
monthly_sales.plot(kind="line")
plt.title("Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.savefig(
    os.path.join(folder, "revenue_by_month.png")
)

# -------------------------
# Pie Chart
# Product Category Distribution
# -------------------------

category_sales = merged.groupby("category")["revenue"].sum()

plt.figure()
category_sales.plot(kind="pie", autopct="%1.1f%%")

plt.ylabel("")

plt.title("Revenue Share by Category")

plt.savefig(
    os.path.join(folder, "category_distribution.png")
)

print("Charts created successfully:")
print("1. revenue_by_region.png")
print("2. revenue_by_month.png")
print("3. category_distribution.png")