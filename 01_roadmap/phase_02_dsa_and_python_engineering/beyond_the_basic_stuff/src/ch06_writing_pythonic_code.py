# ============================================================
# CHAPTER 6 — WRITING PYTHONIC CODE
# ============================================================
#
# Story:
# Haider is improving the warehouse system.
# The system already works, but some parts are written in
# unnecessarily complicated Python.
#
# The goal is not to make the code shorter at any cost.
# The goal is to use Python's idioms when they make the code
# clearer and easier to maintain.
# ============================================================

import copy
from collections import defaultdict

# ============================================================
# STAGE 1 — ENUMERATE INSTEAD OF range(len())
# ============================================================

products = [
    "Keyboard",
    "Mouse",
    "Monitor",
    "Headset",
]

print("\n========== PRODUCT LIST ==========")

for index, product in enumerate(products, start=1):
    print(f"{index}. {product}")


# ============================================================
# STAGE 2 — USE with FOR FILES
# ============================================================

print("\n========== WRITE INVENTORY REPORT ==========")

report = """Warehouse Inventory Report
--------------------------
Keyboard: 12
Mouse: 25
Monitor: 8
Headset: 15
"""

with open("inventory_report.txt", "w") as file:
    file.write(report)

print("Report saved.")


# ============================================================
# STAGE 3 — USE is WHEN COMPARING WITH None
# ============================================================

print("\n========== PRODUCT SEARCH ==========")


def find_product(products, name):
    for product in products:
        if product["name"] == name:
            return product

    return None


inventory = [
    {"name": "Keyboard", "quantity": 12},
    {"name": "Mouse", "quantity": 25},
    {"name": "Monitor", "quantity": 8},
]

product = find_product(inventory, "Printer")

if product is None:
    print("Product not found.")
else:
    print(product)


# ============================================================
# STAGE 4 — BOOLEAN CHECKS WITH TRUTHINESS
# ============================================================
#
# Avoid comparing against True or False explicitly.
# Use the value directly — Pythonic and more readable.

print("\n========== AVAILABILITY CHECK ==========")

in_stock = True

# Non-Pythonic:
# if in_stock == True:
#     ...

if in_stock:
    print("Product is available.")

if not in_stock:
    print("Product is not available.")


# ============================================================
# STAGE 5 — RAW STRINGS FOR PATHS
# ============================================================

print("\n========== FILE PATH ==========")

report_path = r"C:\warehouse\reports\inventory.txt"

print("Report path:", report_path)


# ============================================================
# STAGE 6 — FORMAT STRINGS WITH F-STRINGS
# ============================================================

print("\n========== PRODUCT DETAILS ==========")

product_name = "Keyboard"
quantity = 12
price = 750

print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price: {price} EGP")
print(f"Inventory value: {quantity * price} EGP")


# ============================================================
# STAGE 7 — SHALLOW COPY
# ============================================================

print("\n========== BACKUP INVENTORY ==========")

current_inventory = [
    {"name": "Keyboard", "quantity": 12},
    {"name": "Mouse", "quantity": 25},
]

backup_inventory = copy.copy(current_inventory)

current_inventory.append({"name": "Monitor", "quantity": 8})

print("After adding a new item:")
print("Current inventory:", current_inventory)
print("Backup inventory:", backup_inventory)

# A shallow copy copies the outer list,
# but nested objects are still shared.

current_inventory[0]["quantity"] = 20

print("\nAfter modifying an item in the original:")
print("Current inventory:", current_inventory)
print("Backup inventory:", backup_inventory)


# ============================================================
# STAGE 8 — DICTIONARY get()
# ============================================================

print("\n========== LOOK UP OPTIONAL DATA ==========")

stock = {
    "Keyboard": 12,
    "Mouse": 25,
}

monitor_quantity = stock.get("Monitor", 0)

print("Monitor quantity:", monitor_quantity)


# ============================================================
# STAGE 9 — DICTIONARY setdefault()
# ============================================================

print("\n========== ADD TO A PRODUCT COUNT ==========")

sold_units = {
    "Keyboard": 4,
}

sold_units.setdefault("Mouse", 0)
sold_units["Mouse"] += 3

print("Sold units:", sold_units)


# ============================================================
# STAGE 10 — defaultdict FOR REPEATED DEFAULT VALUES
# ============================================================

print("\n========== SALES BY CASHIER ==========")

sales_by_cashier = defaultdict(list)

sales_by_cashier["Ali"].append("Keyboard")
sales_by_cashier["Ali"].append("Mouse")
sales_by_cashier["Omar"].append("Monitor")

print("Ali:", sales_by_cashier["Ali"])
print("Omar:", sales_by_cashier["Omar"])
print("Adam:", sales_by_cashier["Adam"])


# ============================================================
# STAGE 11 — DICTIONARY AS A VALUE LOOKUP
# ============================================================

print("\n========== PRODUCT STATUS ==========")

status = "low_stock"

status_messages = {
    "available": "Product is available.",
    "low_stock": "Product needs replenishment.",
    "out_of_stock": "Product is out of stock.",
}

message = status_messages.get(
    status,
    "Unknown product status.",
)

print(message)


# ============================================================
# STAGE 12 — DICTIONARY AS A FUNCTION DISPATCH
# ============================================================
#
# Replace long if-elif chains with a dictionary that maps
# command names to functions.

print("\n========== WAREHOUSE COMMANDS ==========")


def show_inventory():
    print("Inventory: Keyboard, Mouse, Monitor")


def show_sales():
    print("Today's sales: 5 items")


def show_reports():
    print("Reports: monthly summary")


commands = {
    "inventory": show_inventory,
    "sales": show_sales,
    "reports": show_reports,
}

user_command = "sales"

if user_command in commands:
    commands[user_command]()
else:
    print("Unknown command.")


# ============================================================
# STAGE 13 — CONDITIONAL EXPRESSION
# ============================================================

print("\n========== SALE STATUS ==========")

quantity = 5

sale_status = "Available" if quantity > 0 else "Out of stock"

print(sale_status)


# ============================================================
# STAGE 14 — CHAIN COMPARISON OPERATORS
# ============================================================

print("\n========== STOCK VALIDATION ==========")

quantity = 35

if 1 <= quantity <= 100:
    print("Quantity is within the valid range.")


# ============================================================
# STAGE 15 — MULTIPLE ASSIGNMENT
# ============================================================

print("\n========== PRODUCT DATA ==========")

name, price, quantity = "Keyboard", 750, 12

print(f"{name}: {quantity} units × {price} EGP")


# ============================================================
# STAGE 16 — CHAINED ASSIGNMENT
# ============================================================
#
# Chain assignment when multiple variables should share
# the SAME initial value. This is different from multiple
# assignment (tuple unpacking), which assigns DIFFERENT values.

print("\n========== INITIALIZE COUNTERS ==========")

keyboard_sold = mouse_sold = monitor_sold = 0

print("Keyboard sold:", keyboard_sold)
print("Mouse sold:", mouse_sold)
print("Monitor sold:", monitor_sold)


# ============================================================
# STAGE 17 — CHECK WHETHER A VALUE IS ONE OF MANY
# ============================================================

print("\n========== USER ROLE ==========")

role = "cashier"

if role in ("admin", "storekeeper", "cashier"):
    print("Recognized role.")
else:
    print("Unknown role.")


# ============================================================
# STAGE 18 — DIRECT ITERATION
# ============================================================

print("\n========== TRAVERSE INVENTORY ==========")

for item in inventory:
    print(f"{item['name']}: {item['quantity']} units")


# ============================================================
# STAGE 19 — PYTHONIC INVENTORY REPORT
# ============================================================

print("\n========== FINAL INVENTORY REPORT ==========")

inventory = [
    {"name": "Keyboard", "price": 750, "quantity": 12},
    {"name": "Mouse", "price": 300, "quantity": 25},
    {"name": "Monitor", "price": 5000, "quantity": 8},
    {"name": "Headset", "price": 1200, "quantity": 0},
]

for index, item in enumerate(inventory, start=1):
    status = "Available" if item["quantity"] > 0 else "Out of stock"

    value = item["price"] * item["quantity"]

    print(
        f"{index}. {item['name']} | "
        f"Qty: {item['quantity']} | "
        f"Value: {value} EGP | "
        f"{status}"
    )


# ============================================================
# STAGE 20 — PUTTING THE PYTHONIC STYLE TOGETHER
# ============================================================

print("\n========== RESTOCK CHECK ==========")

minimum_stock = 10

for item in inventory:
    if item["quantity"] < minimum_stock:
        print(f"Restock needed: {item['name']} (current quantity: {item['quantity']})")


# ============================================================
# CHAPTER 6 COMPLETE
# ============================================================

print("\n========== CHAPTER 6 COMPLETE ==========")
