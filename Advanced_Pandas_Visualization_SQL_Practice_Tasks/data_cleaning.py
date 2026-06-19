# data_cleaning.py
# Task 2: Data cleaning and standardization

import pandas as pd
import os

folder = os.path.dirname(__file__)

# Load data
customers = pd.read_csv(os.path.join(folder, "customers.csv"))
products = pd.read_csv(os.path.join(folder, "products.csv"))
orders = pd.read_csv(os.path.join(folder, "orders.csv"))

# ---------------------------
# Standardize column names
# ---------------------------

customers.columns = customers.columns.str.lower().str.strip()
products.columns = products.columns.str.lower().str.strip()
orders.columns = orders.columns.str.lower().str.strip()

print("Column names standardized\n")

# ---------------------------
# Fix data types
# ---------------------------

products["price"] = products["price"].astype(float)

orders["customer_id"] = orders["customer_id"].astype(int)
orders["product_id"] = orders["product_id"].astype(int)
orders["quantity"] = orders["quantity"].astype(int)

print("Data types fixed\n")

# ---------------------------
# Handle missing values
# ---------------------------

print("Missing values before cleaning:\n")

print("Customers")
print(customers.isnull().sum())

print("\nProducts")
print(products.isnull().sum())

print("\nOrders")
print(orders.isnull().sum())

# Fill text columns if missing
customers = customers.fillna("Unknown")

# Fill numeric columns if missing
products["price"] = products["price"].fillna(
    products["price"].mean()
)

orders["quantity"] = orders["quantity"].fillna(
    orders["quantity"].median()
)

print("\nMissing values after cleaning:\n")

print("Customers")
print(customers.isnull().sum())

print("\nProducts")
print(products.isnull().sum())

print("\nOrders")
print(orders.isnull().sum())

print("\nCleaning Notes:")
print("- Column names converted to lowercase")
print("- Numeric columns converted to proper types")
print("- Missing text values -> 'Unknown'")
print("- Missing prices -> mean value")
print("- Missing quantity -> median value")