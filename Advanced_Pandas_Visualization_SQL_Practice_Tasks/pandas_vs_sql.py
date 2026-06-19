# pandas_vs_sql.py
# Task 8: Compare SQL and Pandas approaches

import pandas as pd
import sqlite3
import os

folder = os.path.dirname(__file__)

# Load CSV files
customers = pd.read_csv(
    os.path.join(folder, "customers.csv")
)

products = pd.read_csv(
    os.path.join(folder, "products.csv")
)

orders = pd.read_csv(
    os.path.join(folder, "orders.csv")
)

# Create database connection
conn = sqlite3.connect(
    os.path.join(folder, "sales.db")
)

print("SQL vs Pandas Comparison")
print("-" * 40)

# --------------------------------
# Example 1: Count orders per customer
# --------------------------------

sql_query = """
SELECT
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
"""

sql_result = pd.read_sql(sql_query, conn)

pandas_result = (
    orders.groupby("customer_id")
    ["order_id"]
    .count()
    .reset_index(name="total_orders")
)

print("\nSQL Result:")
print(sql_result)

print("\nPandas Result:")
print(pandas_result)

# --------------------------------
# Example 2: Total quantity per product
# --------------------------------

sql_query2 = """
SELECT
    product_id,
    SUM(quantity) AS total_quantity
FROM orders
GROUP BY product_id
"""

sql_result2 = pd.read_sql(sql_query2, conn)

pandas_result2 = (
    orders.groupby("product_id")
    ["quantity"]
    .sum()
    .reset_index(name="total_quantity")
)

print("\nSQL Product Result:")
print(sql_result2)

print("\nPandas Product Result:")
print(pandas_result2)

print("\nObservations:")
print("- SQL is useful for querying databases")
print("- Pandas is useful for in-memory analysis")
print("- Both can perform filtering, grouping, and joins")
print("- Pandas syntax is Python-based")
print("- SQL syntax is database-oriented")

conn.close()