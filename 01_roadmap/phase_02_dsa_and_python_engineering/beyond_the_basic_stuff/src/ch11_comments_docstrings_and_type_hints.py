"""
Chapter 11 — Comments, Docstrings, and Type Hints
Beyond the Basic Stuff with Python

This module demonstrates comments, docstrings, and type hints.
The examples use a small inventory system to demonstrate
documentation and gradual typing.
"""

from collections.abc import Mapping, Sequence
from typing import Any, Dict, List

# ============================================================
# 1. COMMENTS
# ============================================================

# Comments explain code to human readers.
# Python ignores comments during execution.

price = 100

# Prefer comments that explain WHY something is done,
# rather than simply repeating WHAT the code does.

# Apply a discount because this product is on promotion.
price *= 0.90


# Inline comments can explain a specific expression.
tax_rate = 0.14  # Egyptian VAT rate used by this example.


# Block comments can explain a larger section of code.
#
# The inventory is processed in two stages:
# first we calculate the total value,
# then we display the result.
inventory = {
    "Laptop": 1000,
    "Mouse": 20,
}


# ============================================================
# 2. COMMENTS SHOULD ADD INFORMATION
# ============================================================

# Bad: repeats what the code already says.
price = 100  # Set price to 100


# Better: explains the reason behind the code.
# Store prices in the smallest currency unit to avoid
# floating-point rounding problems.
price_in_cents = 10000


# ============================================================
# 3. SUMMARY COMMENTS
# ============================================================

# Calculate the total inventory value before displaying it.
total_value = sum(inventory.values())

print(total_value)


# ============================================================
# 4. LESSONS-LEARNED COMMENTS
# ============================================================

# Do not modify a collection while iterating over it.
# Build a separate list when items need to be removed.

products = ["Laptop", "Mouse", "Keyboard"]

products_to_remove = []

for product in products:
    if product == "Mouse":
        products_to_remove.append(product)

for product in products_to_remove:
    products.remove(product)


# ============================================================
# 5. TODO / CODETAG COMMENTS
# ============================================================

# TODO: Replace this temporary calculation with the database
# value once persistence is implemented.

inventory_value = 0


# ============================================================
# 6. FUNCTION DOCSTRINGS
# ============================================================


def calculate_total(prices):
    """
    Returns the sum of all product prices.
    """
    return sum(prices)


prices = [100, 250, 500]

print(calculate_total(prices))


# A docstring belongs directly inside the function body.
print(calculate_total.__doc__)


# ============================================================
# 7. CLASS DOCSTRINGS
# ============================================================


class Product:
    """Represents a product in the inventory."""

    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 1000)

print(Product.__doc__)


# ============================================================
# 8. help()
# ============================================================

help(Product)


# ============================================================
# 9. TYPE HINTS
# ============================================================

# Type hints document the expected type.
product_name: str = "Laptop"
quantity: int = 10
price: float = 999.99
is_active: bool = True


# Type hints do NOT enforce the type at runtime.

quantity: int = "ten"

print(quantity)


# ============================================================
# 10. FUNCTION PARAMETERS AND RETURN TYPES
# ============================================================


def calculate_price(price: float, quantity: int) -> float:
    return price * quantity


total = calculate_price(100.0, 3)

print(total)


# ============================================================
# 11. NONE RETURN TYPE
# ============================================================


def display_product(name: str, price: float) -> None:
    print(f"{name}: {price}")


display_product("Mouse", 20.0)


# ============================================================
# 12. GRADUAL TYPING
# ============================================================

# Type hints can be added gradually.
# A program does not need to be fully type-hinted at once.

name: str = "Laptop"


def get_price(product):
    return product["price"]


# Later, the function can become more explicit:


def get_typed_price(product: dict) -> float:
    return product["price"]


# ============================================================
# 13. TYPE INFERENCE
# ============================================================

# Python/type-checking tools can often infer the type
# from the assigned value.

name = "Laptop"  # inferred as str
quantity = 10  # inferred as int
active = True  # inferred as bool


# Explicit annotations can make the intended type clearer.

name: str = "Laptop"
quantity: int = 10


# ============================================================
# 14. CLASSES AS TYPES
# ============================================================


class CatTail:
    def __init__(self, length: int, color: str) -> None:
        self.length = length
        self.color = color


def show_tail(tail: CatTail) -> None:
    print(tail.length)
    print(tail.color)


tail = CatTail(20, "black")

show_tail(tail)


# ============================================================
# 15. MULTIPLE POSSIBLE TYPES
# ============================================================

# A value can sometimes legitimately have more than one type.


def format_product_id(product_id: int | str) -> str:
    return str(product_id)


print(format_product_id(100))
print(format_product_id("P-100"))


# ============================================================
# 16. OPTIONAL VALUES
# ============================================================

# A value may be either a string or None.


def find_product(name: str) -> str | None:
    if name == "Laptop":
        return "Laptop"
    return None


result = find_product("Mouse")

print(result)


# ============================================================
# 17. ANY
# ============================================================

# Any is imported at the top of the module.
#
# Any means the value may be of any type.
# Use it sparingly because it reduces the benefits
# provided by static type checking.


def log_value(value: Any) -> None:
    print(value)


log_value("Laptop")
log_value(100)
log_value([1, 2, 3])


# ============================================================
# 18. CONTAINER TYPE HINTS
# ============================================================

products: list[str] = [
    "Laptop",
    "Mouse",
    "Keyboard",
]

quantities: list[int] = [
    10,
    20,
    15,
]

prices: dict[str, float] = {
    "Laptop": 1000.0,
    "Mouse": 20.0,
}

coordinates: tuple[int, int] = (10, 20)

categories: set[str] = {
    "electronics",
    "office",
}


# ============================================================
# 19. SEQUENCE
# ============================================================

# Sequence is imported at the top of the module.
#
# Sequence describes ordered collection-like objects
# without requiring one specific concrete type.


def display_items(items: Sequence[str]) -> None:
    for item in items:
        print(item)


display_items(["Laptop", "Mouse"])
display_items(("Laptop", "Mouse"))


# ============================================================
# 20. MAPPING
# ============================================================

# Mapping is imported at the top of the module.
#
# Mapping describes dictionary-like objects.


def display_prices(prices: Mapping[str, float]) -> None:
    for name, price in prices.items():
        print(name, price)


display_prices(
    {
        "Laptop": 1000.0,
        "Mouse": 20.0,
    }
)


# ============================================================
# 21. STATIC TYPE CHECKING
# ============================================================

# Python itself does not enforce type hints at runtime.
#
# Static type checkers such as Mypy can inspect the source code
# before execution and report possible type errors.


def add_numbers(a: int, b: int) -> int:
    return a + b


# A static type checker can report this as a type error.
# This line is intentionally commented out because Python
# would raise TypeError at runtime.
#
# result = add_numbers("10", 20)


# ============================================================
# 22. type: ignore
# ============================================================

# A type checker can be instructed to ignore a specific line
# when the programmer knows that the reported issue is safe
# or intentionally handled elsewhere.
#
# Important: # type: ignore only tells the STATIC type checker
# to ignore the warning. It does NOT suppress runtime errors.
#
# value = add_numbers("10", 20)  # type: ignore


# ============================================================
# 23. BACKPORTING TYPE HINTS
# ============================================================

# Newer Python versions support modern built-in generic syntax:

products: list[str]
prices: dict[str, float]


# For older Python versions, typing constructs can be used.
# Dict and List are imported at the top of the module.

products: List[str]
prices: Dict[str, float]


# ============================================================
# 24. COMMENTS VS DOCSTRINGS
# ============================================================

# Comment:
# Used to explain implementation details, decisions,
# warnings, TODOs, or other information for developers.


def calculate_inventory_value(
    prices: list[float],
) -> float:
    """
    Calculate the total value of all products.

    Args:
        prices: Product prices.

    Returns:
        The total inventory value.
    """
    # sum() performs the actual calculation.
    return sum(prices)


# ============================================================
# 25. PROFESSIONAL COMBINATION
# ============================================================


class Inventory:
    """Represents a simple product inventory."""

    def __init__(self) -> None:
        self.products: dict[str, float] = {}

    def add_product(self, name: str, price: float) -> None:
        """Add or update a product and its price."""
        self.products[name] = price

    def calculate_value(self) -> float:
        """Return the total value of all products."""
        return sum(self.products.values())

    def display(self) -> None:
        """Display all products and the total inventory value."""
        for name, price in self.products.items():
            print(f"{name}: {price}")

        print(f"Total: {self.calculate_value()}")


inventory = Inventory()

inventory.add_product("Laptop", 1000.0)
inventory.add_product("Mouse", 20.0)

inventory.display()


# ============================================================
# 26. FINAL MENTAL MODEL
# ============================================================

# Comments
#     → Explain code to human readers.
#
# Docstrings
#     → Document modules, functions, and classes.
#
# Type Hints
#     → Describe expected types.
#
# Static Type Checkers
#     → Analyze type hints before runtime.
#
# Runtime
#     → Python does not automatically enforce type hints.
#
# Gradual Typing
#     → Type hints can be introduced incrementally.
#
# Professional Python Code
#     → Clear comments
#     + useful docstrings
#     + meaningful type hints
#     + static analysis when appropriate


# ============================================================
# END OF CHAPTER 11
# ============================================================
