# sql_analysis.py
# Task 7: Store data in SQLite and query it

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

# Create database
db_path = os.path.join(folder, "sales.db")

conn = sqlite3.connect(db_path)

# Store tables in SQLite
customers.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

products.to_sql(
    "products",
    conn,
    if_exists="replace",
    index=False
)

orders.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully")

# -----------------------------
# Query 1
# Total orders by customer
# -----------------------------

query1 = """
SELECT
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
"""

result1 = pd.read_sql(query1, conn)

print("\nTotal Orders by Customer:")
print(result1)

# -----------------------------
# Query 2
# Product sales quantity
# -----------------------------

query2 = """
SELECT
    product_id,
    SUM(quantity) AS total_quantity
FROM orders
GROUP BY product_id
ORDER BY total_quantity DESC
"""

result2 = pd.read_sql(query2, conn)

print("\nProduct Sales Quantity:")
print(result2)

# -----------------------------
# Query 3
# Customer + product join
# -----------------------------

query3 = """
SELECT
    c.name,
    p.product_name,
    o.quantity
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN products p
ON o.product_id = p.product_id
"""

result3 = pd.read_sql(query3, conn)

print("\nJoined Analysis:")
print(result3)

conn.close()