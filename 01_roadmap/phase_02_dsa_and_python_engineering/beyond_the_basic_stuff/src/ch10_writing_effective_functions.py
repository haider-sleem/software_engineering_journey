# ============================================================
# Chapter 10 — Writing Effective Functions
# A small warehouse program that grows through several stages
# ============================================================


# ============================================================
# STAGE 1 — Give Functions Clear Names
# ============================================================

products = {
    "Keyboard": {"price": 25.0, "quantity": 12},
    "Mouse": {"price": 15.0, "quantity": 3},
    "Monitor": {"price": 180.0, "quantity": 7},
}


def show_product(product_name):
    product = products[product_name]
    print(f"{product_name}: ${product['price']}")


show_product("Keyboard")


# ============================================================
# STAGE 2 — Keep Functions Reasonably Small
# ============================================================

# A function should do one clear job.
# Small does not mean "split everything into tiny functions."


def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(25.0, 3)
print("Total:", total)


# ============================================================
# STAGE 3 — Parameters and Arguments
# ============================================================


# name and quantity are PARAMETERS.
def sell_product(name, quantity):
    if name not in products:
        return False

    if quantity <= 0:
        return False

    if products[name]["quantity"] < quantity:
        return False

    products[name]["quantity"] -= quantity
    return True


# "Mouse" and 1 are ARGUMENTS.
sell_product("Mouse", 1)


# ============================================================
# STAGE 4 — Default Arguments
# ============================================================


# Parameters with default values must come after
# parameters without default values.
# Avoid mutable default values such as [] or {}.
def create_product(name, price, quantity=0):
    products[name] = {
        "price": price,
        "quantity": quantity,
    }


# Most new products may start with zero stock.
create_product("Headset", 40.0)

# The default can still be overridden.
create_product("Webcam", 60.0, 5)


# ============================================================
# STAGE 5 — *args
# ============================================================

# *args collects extra positional arguments into a tuple.


def calculate_total_price(*prices):
    total = 0

    for price in prices:
        total += price

    return total


print(
    "Order total:",
    calculate_total_price(25.0, 15.0, 40.0),
)


# ============================================================
# STAGE 6 — **kwargs
# ============================================================

# **kwargs collects extra keyword arguments into a dictionary.
# When both are used, *args must come before **kwargs.


def create_product_with_options(**details):
    name = details["name"]

    products[name] = {
        "price": details.get("price", 0),
        "quantity": details.get("quantity", 0),
    }


create_product_with_options(
    name="Printer",
    price=250.0,
    quantity=2,
)


# ============================================================
# STAGE 7 — Unpacking Arguments
# ============================================================

# * expands an iterable into positional arguments.
# ** expands a mapping into keyword arguments.

prices = [10.0, 20.0, 30.0]

print("Total:", calculate_total_price(*prices))


product_details = {
    "name": "Scanner",
    "price": 150.0,
    "quantity": 3,
}

create_product_with_options(**product_details)


# ============================================================
# STAGE 8 — Wrapper Functions
# ============================================================


# A wrapper function calls another function and can
# forward *args and **kwargs to it unchanged,
# or add behavior before/after the call.
def print_message(*args, **kwargs):
    print(*args, **kwargs)


print_message("Warehouse:", "Main Warehouse")


# ============================================================
# STAGE 9 — Side Effects
# ============================================================

# This function has a side effect because it modifies
# data outside its local scope.
# Modifying a mutable object passed into or referenced
# from a function counts as a side effect.


def restock_product(name, quantity):
    if name not in products:
        return False

    products[name]["quantity"] += quantity
    return True


restock_product("Keyboard", 10)


# ============================================================
# STAGE 10 — Prefer Pure Functions When Practical
# ============================================================

# This function only calculates a value.
# It does not modify external state.
# Python does not enforce purity — it is a design convention.


def calculate_order_total(price, quantity):
    return price * quantity


order_total = calculate_order_total(25.0, 4)
print("Order total:", order_total)


# ============================================================
# STAGE 11 — Deterministic Functions
# ============================================================

# A deterministic function always returns the same result
# for the same inputs.
#
# Non-deterministic examples: random.randint(), time.time()
# Deterministic functions can be cached (space/time tradeoff).


def calculate_discount(price, discount_percent):
    return price * (discount_percent / 100)


# Same inputs → same result.
discount_1 = calculate_discount(100.0, 10)
discount_2 = calculate_discount(100.0, 10)

print(discount_1)
print(discount_2)


# ============================================================
# STAGE 12 — Higher-Order Functions
# ============================================================


def apply_to_price(price, operation):
    return operation(price)


def add_tax(price):
    return price * 1.14


final_price = apply_to_price(100.0, add_tax)

print("Final price:", final_price)


# ============================================================
# STAGE 13 — Lambda Functions
# ============================================================

# A lambda is a small anonymous function whose body is a
# single expression that acts as its return value.
# Use lambda for short one-off functions passed as arguments.
# Use def when a function needs a meaningful name or is reused.


products_by_price = sorted(
    products.items(),
    key=lambda item: item[1]["price"],
)

print("Products sorted by price:")

for name, product in products_by_price:
    print(name, product["price"])


# ============================================================
# STAGE 14 — Mapping with a Comprehension
# ============================================================

# map() and filter() return iterator objects.
# List comprehensions are usually preferred — more readable.

# Mapping: transform each value into a new value.
# Here each name is transformed to uppercase.

product_names = [name.upper() for name in products]

print("Product names:", product_names)


# ============================================================
# STAGE 15 — Filtering with a Comprehension
# ============================================================

available_products = [
    name for name, product in products.items() if product["quantity"] > 0
]

print("Available products:", available_products)


# ============================================================
# STAGE 16 — Avoid Returning Different Types
# ============================================================

# A function should consistently return the same data type.
# Returning 0 here instead of None keeps the return type
# consistent (always an int).


def get_stock(name):
    if name not in products:
        return 0

    return products[name]["quantity"]


# Note: using 0 for "not found" can make it impossible to
# distinguish a missing product from a product with zero stock.
# Exceptions can be a better choice for error conditions.


quantity = get_stock("Keyboard")

print("Keyboard stock:", quantity)


# ============================================================
# STAGE 17 — Use Exceptions for Errors
# ============================================================

# Avoid mixing a normal return value with None as an error
# indicator — callers are forced to handle two different types.
# Use exceptions to signal error conditions instead.
#
# Example: str.find() returns -1 on failure (can silently
# cause bugs). str.index() raises ValueError instead.


def get_product(name):
    if name not in products:
        raise KeyError(f"Product '{name}' does not exist.")

    return products[name]


try:
    product = get_product("Keyboard")
    print("Product:", product)
except KeyError as error:
    print("Error:", error)


# ============================================================
# FINAL — Putting the Ideas Together
# ============================================================


def calculate_sale_total(
    product_name: str,
    quantity: int,
    discount_percent: float = 0,
) -> float:
    """
    Calculate the total price of a sale.

    The function performs a calculation without modifying
    the warehouse inventory.
    """

    product = get_product(product_name)

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if product["quantity"] < quantity:
        raise ValueError("Not enough stock.")

    subtotal = product["price"] * quantity
    discount = subtotal * (discount_percent / 100)

    return subtotal - discount


total = calculate_sale_total(
    "Keyboard",
    2,
    discount_percent=10,
)

print("Sale total:", total)
