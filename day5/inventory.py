# inventory.py
# This program demonstrates OOP with file I/O using CSV.

import csv


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"{self.name} | Price: ₹{self.price} | "
            f"Quantity: {self.quantity}"
        )


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Adds a product to inventory."""
        self.products.append(product)

    def total_value(self) -> float:
        """Returns total inventory value."""
        return sum(
            product.price * product.quantity
            for product in self.products
        )

    def find_product(self, name: str):
        """Case-insensitive search."""
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def save_to_csv(self, filename):
        """Saves products to CSV."""
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["name", "price", "quantity"])

            for product in self.products:
                writer.writerow(
                    [
                        product.name,
                        product.price,
                        product.quantity
                    ]
                )

    def load_from_csv(self, filename):
        """Loads products from CSV."""
        self.products = []

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                product = Product(
                    row["name"],
                    float(row["price"]),
                    int(row["quantity"])
                )

                self.products.append(product)


# Create inventory
inventory = Inventory()

# Add products
inventory.add_product(Product("Laptop", 55000, 2))
inventory.add_product(Product("Mouse", 500, 5))
inventory.add_product(Product("Keyboard", 1200, 3))

print("Products:")
for product in inventory.products:
    print(product)

print("\nTotal Inventory Value:")
print("₹", inventory.total_value())

print("\nSearch Product:")
found = inventory.find_product("mouse")

if found:
    print(found)
else:
    print("Not found")


# Save to CSV
inventory.save_to_csv("inventory.csv")

print("\nSaved to inventory.csv")

# Load into a new inventory object
new_inventory = Inventory()
new_inventory.load_from_csv("inventory.csv")

print("\nLoaded Products:")
for product in new_inventory.products:
    print(product)


# Explore:
# @staticmethod does not receive self or cls automatically.
# load_from_csv could be a class method if it creates and
# returns an Inventory object.
# A static method is independent, while a class method
# works with the class itself (cls).