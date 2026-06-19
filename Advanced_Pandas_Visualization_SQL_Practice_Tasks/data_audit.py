# data_audit.py
# Task 1: Data quality audit

import pandas as pd
import os

folder = os.path.dirname(__file__)

customers = pd.read_csv(os.path.join(folder, "customers.csv"))
products = pd.read_csv(os.path.join(folder, "products.csv"))
orders = pd.read_csv(os.path.join(folder, "orders.csv"))


def audit(df, table_name):
    print(f"\n--- {table_name} ---")

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nNull Values:")
    print(df.isnull().sum())

    print("\nDuplicates:")
    print(df.duplicated().sum())

    print("\nUnique Counts:")
    print(df.nunique())


audit(customers, "Customers")
audit(products, "Products")
audit(orders, "Orders")