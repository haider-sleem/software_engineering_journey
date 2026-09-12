# ============================================================
# Chapter 5 - Finding Code Smells
# A small warehouse program that grows through several stages
# ============================================================

import logging

# ============================================================
# Stage 1 - The program works, but duplicate code appears
# ============================================================

products = {
    "Keyboard": 25.0,
    "Mouse": 15.0,
    "Monitor": 180.0,
}

print("Product:", "Keyboard")
print("Price:", products["Keyboard"])

print("Product:", "Mouse")
print("Price:", products["Mouse"])

print("Product:", "Monitor")
print("Price:", products["Monitor"])


# ============================================================
# Stage 2 - Remove duplicate code with a function
# ============================================================


def show_product(name, price):
    print("Product:", name)
    print("Price:", price)


for name, price in products.items():
    show_product(name, price)


# ============================================================
# Stage 3 - Replace magic numbers with constants
# ============================================================

MIN_STOCK = 0
LOW_STOCK_LIMIT = 5
MAX_DISCOUNT_PERCENT = 20

stock = {
    "Keyboard": 12,
    "Mouse": 3,
    "Monitor": 7,
}

for name, quantity in stock.items():
    if quantity < LOW_STOCK_LIMIT and quantity > MIN_STOCK:
        print(f"Low stock: {name}")

discount = 10

if discount > MAX_DISCOUNT_PERCENT:
    print("Discount is too high.")


# ============================================================
# Stage 4 - Avoid commented-out code
# ============================================================

# Old code was removed instead of being kept here.
# Git keeps the history of previous versions.


# ============================================================
# Stage 5 - Remove dead code
# ============================================================
#
# The function below was part of an older version of the
# warehouse program. It is no longer called anywhere.
#
# In a real project, this function should be removed —
# Git keeps the history if we ever need to restore it.


def calculate_total(price, quantity):
    total = price * quantity
    return total


# (No call to calculate_total — it is dead code.)


# ============================================================
# Stage 6 - Stubs are an acceptable exception to dead code
# ============================================================
#
# A stub is a placeholder function that deliberately does
# nothing yet — or raises NotImplementedError — to outline
# future code without failing silently.
#
# This is NOT considered dead code, because it represents
# a planned part of the program.


def export_report():
    """
    Export the inventory report to a file.

    (To be implemented later.)
    """
    raise NotImplementedError("Report export will be added later.")


def import_products():
    """
    Import products from an external source.

    (To be implemented later.)
    """
    pass  # noqa


# ============================================================
# Stage 7 - Use a debugger or logging instead of print debugging
# ============================================================

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename="warehouse.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def sell_product(name, quantity):
    logger.debug("Selling %s units of %s", quantity, name)

    if name not in stock:
        return False

    if stock[name] < quantity:
        logger.debug(
            "Not enough stock for %s. Available: %s",
            name,
            stock[name],
        )
        return False

    stock[name] -= quantity
    logger.debug(
        "Sale completed. Remaining stock for %s: %s",
        name,
        stock[name],
    )
    return True


sell_product("Mouse", 1)


# ============================================================
# Stage 8 - Replace numeric suffixes with a collection
# ============================================================

# Bad pattern:
product1 = "Keyboard"
product2 = "Mouse"
product3 = "Monitor"

# Better pattern:
product_names = ["Keyboard", "Mouse", "Monitor"]

for product_name in product_names:
    print(product_name)


# ============================================================
# Stage 9 - Use a module instead of an unnecessary class
# ============================================================


# Bad pattern:
class ProductPrinter:
    @staticmethod
    def print_product(name, price):
        print(f"{name}: ${price}")


# Better pattern:
def print_product(name, price):
    print(f"{name}: ${price}")


print_product("Keyboard", products["Keyboard"])


# ============================================================
# Stage 10 - Keep list comprehensions readable
# ============================================================

products_with_stock = [
    ("Keyboard", 12),
    ("Mouse", 3),
    ("Monitor", 7),
    ("Headset", 0),
]

warehouse_categories = [
    {
        "name": "Electronics",
        "products": products_with_stock,
    },
    {
        "name": "Accessories",
        "products": [("Cable", 50), ("Charger", 0)],
    },
]

# Bad pattern — multiple for-loops crammed into one comprehension.
# This is technically valid Python, but hard to read at a glance.
all_available = [
    name
    for category in warehouse_categories
    for name, quantity in category["products"]
    if quantity > MIN_STOCK
]

# Better pattern — a plain multi-line for loop.
available_products = []

for category in warehouse_categories:
    for name, quantity in category["products"]:
        if quantity > MIN_STOCK:
            available_products.append(name)

print("Available products:", available_products)


# ============================================================
# Stage 11 - Do not silently ignore exceptions
# ============================================================


def get_product_quantity(product_name):
    try:
        return stock[product_name]
    except KeyError:
        logger.warning("Product not found: %s", product_name)
        return None


quantity = get_product_quantity("Keyboard")

if quantity is not None:
    print("Quantity:", quantity)


# ============================================================
# Stage 12 - Give useful error messages
# ============================================================


def get_quantity(product_name):
    if product_name not in stock:
        print(f"Error: product '{product_name}' does not exist.")
        return None

    return stock[product_name]


quantity = get_quantity("Laptop")

if quantity is not None:
    print("Quantity:", quantity)


# ============================================================
# Stage 13 - Multiple return statements are not automatically bad
# ============================================================


def can_sell(product_name, quantity):
    if product_name not in stock:
        return False

    if quantity <= 0:
        return False

    return stock[product_name] >= quantity


if can_sell("Keyboard", 2):
    print("Sale can be completed.")


# ============================================================
# Stage 14 - Multiple try blocks are not automatically bad
# ============================================================


def process_sale(product_name, quantity):
    try:
        current_stock = stock[product_name]
    except KeyError:
        print(f"Error: product '{product_name}' does not exist.")
        return False

    if current_stock < quantity:
        print(f"Error: only {current_stock} units of '{product_name}' are available.")
        return False

    try:
        stock[product_name] -= quantity
    except (TypeError, ValueError):
        print("Error: invalid quantity.")
        return False

    return True


process_sale("Keyboard", 1)


# ============================================================
# Stage 15 - Flag arguments are sometimes reasonable
# ============================================================


def display_products(include_out_of_stock=False):
    for name, quantity in products_with_stock:
        if include_out_of_stock or quantity > MIN_STOCK:
            print(f"{name}: {quantity}")


display_products()
display_products(include_out_of_stock=True)


# ============================================================
# Stage 16 - Global variables are not automatically bad
# ============================================================

WAREHOUSE_NAME = "Main Warehouse"
DEFAULT_CURRENCY = "USD"


def show_warehouse_info():
    print(f"Warehouse: {WAREHOUSE_NAME}")
    print(f"Currency: {DEFAULT_CURRENCY}")


show_warehouse_info()


# ============================================================
# Stage 17 - Comments are useful when they add information
# ============================================================

# The warehouse uses zero as the minimum valid stock level.
MIN_STOCK = 0


def is_in_stock(product_name):
    return stock.get(product_name, MIN_STOCK) > MIN_STOCK


print(is_in_stock("Keyboard"))
