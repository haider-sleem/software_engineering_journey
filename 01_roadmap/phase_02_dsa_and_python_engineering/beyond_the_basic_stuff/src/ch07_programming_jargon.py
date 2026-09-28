# ============================================================
# Chapter 7 — Programming Jargon
# Beyond the Basic Stuff with Python — Al Sweigart
#
# A small warehouse story that introduces each term
# as it naturally appears in the code.
# ============================================================


# ============================================================
# STAGE 1 — Python Language vs. Python Interpreter
# ============================================================

# This is Python code — Python here refers to the language.
name = "Keyboard"

# The Python Interpreter is the program that reads this code
# and executes it. CPython is the standard interpreter,
# written in C.


# ============================================================
# STAGE 1b — Garbage Collection
# ============================================================

# Python manages memory automatically through garbage collection.
# Python uses automatic memory management, including garbage collection.
# It tracks objects that are no longer needed so their memory
# can be made available for other data.
#
# For example, local objects created inside a function can become
# eligible for garbage collection after the function returns.

product = {"name": "Keyboard", "price": 25}
product = None
# The original dict is no longer referenced.
# It is now eligible for garbage collection.


# ============================================================
# STAGE 2 — Literals
# ============================================================

product_name = "Keyboard"  # string literal
price = 25  # integer literal
discount = 0.10  # float literal
is_active = True  # bool
description = None  # None
# Note: True, False, and None are technically keywords in Python,
# though they are commonly shown as examples of literals.

products = []  # empty list literal
product = {"name": "Mouse"}  # dict literal


# ============================================================
# STAGE 3 — Keywords
# ============================================================

# Keywords are reserved words with special meaning in Python.
# They cannot be used as variable names.
#
# Examples: if, else, for, while, def, class, return

if price > 0:
    print("Valid price")


# ============================================================
# STAGE 3b — Identifiers
# ============================================================

# An identifier is the name used to refer to something in code.
# Variables, function names, class names, and module names
# are all identifiers.

product_name = "Keyboard"  # product_name is an identifier
price = 25  # price is an identifier


def calculate_total(price, quantity):  # noqa: F811
    return price * quantity


# calculate_total is an identifier.
# price and quantity inside the definition are also identifiers.


# ============================================================
# STAGE 4 — Objects, Values, Types, Identity
# ============================================================

product_name = "Keyboard"

# product_name → variable (a name bound to an object)
# "Keyboard"   → the object
#
# Every object has:
#     value
#     data type
#     identity

print(type(product_name))  # <class 'str'>
print(id(product_name))  # memory address (identity)

price = 25

print(type(price))  # <class 'int'>
print(id(price))


# ============================================================
# STAGE 5 — Variables Are References
# ============================================================

product = {"name": "Keyboard", "stock": 10}

another_product = product

# Both variables reference the same object.
# Modifying through one name affects the other.

product["stock"] = 20

print(another_product)
# {'name': 'Keyboard', 'stock': 20}


# ============================================================
# STAGE 6 — == vs. is
# ============================================================

product_a = {"name": "Keyboard"}
product_b = {"name": "Keyboard"}

print(product_a == product_b)
# True — same value

print(product_a is product_b)
# False — different objects in memory

product_c = product_a

print(product_a == product_c)
# True

print(product_a is product_c)
# True — same object

# Note: do not use is to compare values such as integers
# or strings. Python may cache small integers and intern
# strings, which can make is return True unexpectedly.
# Use == for value comparison.


# ============================================================
# STAGE 7 — Instances
# ============================================================


class Product:
    pass


product = Product()

# product is an instance of Product.
# "Instance" emphasizes the relationship to the class.


# ============================================================
# STAGE 8 — Items
# ============================================================

products = ["Keyboard", "Mouse", "Monitor"]

for item in products:
    print(item)

# Each element inside a container is called an item.


# ============================================================
# STAGE 9 — Mutable vs. Immutable
# ============================================================

# Mutable — can be changed after creation.

products = ["Keyboard", "Mouse"]
products.append("Monitor")
print(products)


# Immutable — cannot be changed after creation.

name = "Keyboard"

# name[0] = "X"  →  TypeError

# Reassigning the variable does not modify the string.
# It binds the name to a different string object.
name = "Mouse"


# ============================================================
# STAGE 10 — Tuple Containing a Mutable Object
# ============================================================

product_info = (
    "Keyboard",
    25,
    ["Warehouse A", "Warehouse B"],
)

# The tuple itself is immutable — its references cannot change.
# But the list inside it is mutable and can be modified.

product_info[2].append("Warehouse C")

print(product_info)


# ============================================================
# STAGE 11 — Index
# ============================================================

products = ["Keyboard", "Mouse", "Monitor"]

print(products[0])  # first item
print(products[1])  # second item
print(products[-1])  # last item

# An index is an integer that identifies a position
# inside a sequence.


# ============================================================
# STAGE 12 — Dictionary Key
# ============================================================

product = {
    "name": "Keyboard",
    "price": 25,
    "stock": 10,
}

print(product["name"])
print(product["price"])

# "name" and "price" are keys.
# A key identifies a value inside a mapping.


# ============================================================
# STAGE 13 — Hash
# ============================================================

product_code = "KB-001"

print(hash(product_code))

# Hashable objects can be used as dictionary keys.

products = {
    "KB-001": "Keyboard",
    "MS-001": "Mouse",
}

print(products["KB-001"])

# Lists are not hashable:
#
# hash(["Keyboard", "Mouse"])  →  TypeError
#
# Tuples are hashable only when all of their items are hashable.


# ============================================================
# STAGE 14 — Containers / Sequences / Mappings / Sets
# ============================================================

# Container — holds references to other objects.
products = ["Keyboard", "Mouse"]

# Sequence — ordered container accessible by integer index.
products = ["Keyboard", "Mouse", "Monitor"]

# Mapping — stores key-value pairs.
products = {
    "KB-001": "Keyboard",
    "MS-001": "Mouse",
}

# Set — unordered collection of unique items.
categories = {"hardware", "software", "hardware"}
print(categories)
# {"hardware", "software"}  — duplicates removed


# ============================================================
# STAGE 15 — Built-in vs. User-defined
# ============================================================

products = list()
# list → built-in type


def calculate_total(price, quantity):  # noqa
    return price * quantity


# calculate_total → user-defined function


class Warehouse:
    pass


# Warehouse → user-defined class


# ============================================================
# STAGE 16 — Dunder / Magic Methods
# ============================================================


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Keyboard", 25)

# __init__ is a dunder method (double underscore on both sides).
# Also called magic methods.
# Python calls them automatically at appropriate times.


# ============================================================
# STAGE 17 — Module
# ============================================================

# A Python file that can be imported is called a module.
#
# Imagine a file named inventory.py:
#
#   def add_product(name):
#       ...
#
# Another file can use it:
#
#   import inventory
#   inventory.add_product("Keyboard")


# ============================================================
# STAGE 18 — Package
# ============================================================

# A package is a directory of modules with an __init__.py file.
#
# warehouse/
# ├── __init__.py
# ├── products.py
# ├── sales.py
# └── inventory.py
#
# warehouse    → package
# products.py  → module
# sales.py     → module
# inventory.py → module


# ============================================================
# STAGE 19 — Callable
# ============================================================


def say_hello():
    print("Hello")


say_hello()

# A callable is an object that can be called using ().
# Functions and classes are common examples.
# Objects can also be made callable by defining __call__().


class Product:  # noqa: F811
    pass


product = Product()

# A class is callable — calling it creates and returns a new instance.
# Objects with a __call__ method are also callable.


# ============================================================
# STAGE 20 — First-Class Functions
# ============================================================


def calculate_total(price, quantity):  # noqa: F811
    return price * quantity


# Functions are first-class objects in Python.
# They can be stored in variables.

calculate = calculate_total

print(calculate(25, 4))


# They can also be passed as arguments.


def run_calculation(function, price, quantity):
    return function(price, quantity)


print(run_calculation(calculate_total, 25, 4))


# Functions can also be returned from other functions.


def get_operation(operation_name):
    def multiply(price, quantity):
        return price * quantity

    def add(price, quantity):
        return price + quantity

    if operation_name == "total":
        return multiply
    return add


operation = get_operation("total")
print(operation(25, 4))


# ============================================================
# STAGE 21 — Expression vs. Statement
# ============================================================

price = 25
# Assignment statement.

total = price * 4
# price * 4 is an expression — it evaluates to a value.

result = total > 50
# total > 50 is also an expression.

if total > 50:
    print("Large order")
# The if line is a statement — it performs an action.


# ============================================================
# STAGE 22 — Block / Body
# ============================================================

if price > 0:
    print("Valid price")
    print("Product can be processed")

# Block: a group of statements at the same indentation level.
# Body: the block belonging to a compound statement.
# Clause: one branch of a compound statement (the if part,
#         the elif part, or the else part are each a clause).

# if price > 0:           ← this is a clause
#     print(...)          ← this is the body / block
# else:                   ← this is another clause
#     print(...)          ← body of the else clause


# ============================================================
# STAGE 23 — Variable vs. Attribute
# ============================================================


class Product:  # noqa: F811
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Keyboard", 25)

# product       → variable (a name in the local or global scope)
# product.name  → attribute (a name accessed through an object)
# product.price → attribute

print(product.name)
print(product.price)


# ============================================================
# STAGE 24 — Function vs. Method
# ============================================================

name = "keyboard"

print(len(name))
# len() → function (not tied to a specific object type)

print(name.upper())
# upper() → method (associated with the string object)

# Not everything after a dot is a method.

import math  # noqa: E402

print(math.sqrt(25))
# sqrt() is a function inside the math module,
# not a method bound to an instance.


# ============================================================
# STAGE 25 — Iterable
# ============================================================

products = ["Keyboard", "Mouse", "Monitor"]

for product in products:
    print(product)

# A list is iterable — Python can loop over its items.


# ============================================================
# STAGE 26 — Iterator
# ============================================================

products = ["Keyboard", "Mouse", "Monitor"]

iterator = iter(products)

print(next(iterator))  # Keyboard
print(next(iterator))  # Mouse
print(next(iterator))  # Monitor

# iter() returns an iterator from an iterable.
# An iterator tracks the current position and
# returns the next item each time next() is called.


# ============================================================
# STAGE 27 — Syntax Error
# ============================================================

# A syntax error prevents Python from parsing the code at all.
#
# print("Keyboard"
#
# SyntaxError: unexpected EOF


# ============================================================
# STAGE 28 — Runtime Error
# ============================================================

price = 100
quantity = 0

# total = price / quantity
#
# The program starts normally, then fails during execution.
# ZeroDivisionError: division by zero


# ============================================================
# STAGE 29 — Semantic / Logical Error
# ============================================================

price = 100
quantity = 5

total = price + quantity

print(total)

# The code runs without error, but the result is wrong.
# total should be price * quantity, not price + quantity.
# This is a semantic (logical) error.


# ============================================================
# STAGE 30 — Parameters vs. Arguments
# ============================================================


def calculate_total(price, quantity):  # noqa: F811
    return price * quantity


# price and quantity → parameters
# (names in the function definition)


calculate_total(25, 4)

# 25 and 4 → arguments
# (values supplied in the function call)


# ============================================================
# STAGE 30b — Type Coercion vs. Type Casting
# ============================================================

# Type Coercion: Python automatically converts one type to another.
#
# Example: int and float in the same expression.

result = 10 + 2.5
print(result)  # 12.5  — int was coerced to float automatically
print(type(result))  # <class 'float'>


# Type Casting: explicitly converting a value to another type.

price_str = "25"
price_int = int(price_str)  # explicit cast: str → int

print(price_int)
print(type(price_int))


# ============================================================
# STAGE 31 — Attribute vs. Property
# ============================================================


class Product:  # noqa: F811
    def __init__(self, price):
        self.price = price


product = Product(25)

print(product.price)
# price is an attribute — direct data stored on the object.

# A property provides attribute-style access but runs
# a method (getter/setter/deleter) behind the scenes.


# ============================================================
# STAGE 32 — Bytecode
# ============================================================

# Python source code is compiled to bytecode by CPython.
# CPython then executes that bytecode.
#
# Python source code (.py)
#         ↓ compiled by CPython
# Python bytecode (.pyc)
#         ↓ executed by CPython's virtual machine
#
# Bytecode is not CPU machine code.
# It runs on the Python virtual machine, not directly on the CPU.

# .pyc files in __pycache__ contain this bytecode.


# ============================================================
# STAGE 33 — Script vs. Program
# ============================================================

print("Warehouse started")

# The terms "script" and "program" overlap significantly.
# The distinction is vague and somewhat arbitrary.
# The same Python file could reasonably be called either.
#
# Similarly, "scripting language" vs "programming language"
# is not a clear technical distinction for Python.
# Python is used for both scripting tasks and large programs.


# ============================================================
# STAGE 34 — Library
# ============================================================

import math  # noqa

result = math.sqrt(100)
print(result)

# We call functionality from the math library.
# Our program controls the flow — we decide when to call it.


# ============================================================
# STAGE 35 — Framework
# ============================================================

# Imagine a web framework:
#
# framework receives HTTP request
#         ↓
# framework calls the function you wrote
#
# You do not control the overall flow — the framework does.
# This is called Inversion of Control (IoC):
#
#   "Don't call us, we'll call you."


# ============================================================
# STAGE 36 — SDK
# ============================================================

# SDK = Software Development Kit
#
# A collection of libraries, tools, and documentation
# for building software on a specific platform or system.
#
# Examples:
#   Android SDK
#   iOS SDK
#   Java Development Kit (JDK)


# ============================================================
# STAGE 37 — Engine
# ============================================================

# An engine is a large, self-contained system that performs
# complex tasks and can be controlled by external software.
#
# Examples:
#   Game Engine
#   Database Engine
#   Search Engine
#
# Your program calls the engine to use its functionality.


# ============================================================
# STAGE 38 — API
# ============================================================

# API = Application Programming Interface
#
# The public-facing interface used to interact with software.
# Callers do not need to know the internal implementation.
# They only need to know:
#
#   what operations are available
#   how to call them
#   what results to expect


def get_product(product_id): ...


# get_product() represents an interface.
# Callers use it without knowing how it is implemented.


# ============================================================
# STAGE 39 — Putting the Jargon Together
# ============================================================


class Product:  # noqa: F811
    """Represent a product."""

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def total_value(self):
        return self.price * self.stock


products = [
    Product("Keyboard", 25, 10),
    Product("Mouse", 15, 5),
]


def calculate_inventory_value(products):  # noqa: F811
    total = 0

    for product in products:
        total += product.total_value()

    return total


inventory_value = calculate_inventory_value(products)

print(inventory_value)


# Terms demonstrated here:
#
# Product              → class
# Product(...)         → instance creation (callable)
# product              → variable / reference
# product.name         → attribute
# total_value()        → method
# calculate_inventory_value() → function
# products             → variable, iterable, argument (at call site)
#                        and parameter (in definition)
# list                 → built-in type
# Product objects      → items inside the list
# for                  → keyword
# total += ...         → statement
# product.total_value()→ expression
# 25, 10, 15, 5        → literals


# ============================================================
# END OF CHAPTER 7
# ============================================================
