"""
Grokking Algorithms — Chapter 5: Hash Tables
Practical Code Story — Warehouse Price Lookup

This file follows the main ideas of Chapter 5:
- Hash tables and key/value pairs
- Hash functions
- Collisions
- Performance
- Load factor
- Resizing
- Good hash functions
- Python dict
"""

# ============================================================
# Stage 1 — The Problem: Fast Price Lookup
# ============================================================

products = {
    "apple": 1.00,
    "milk": 2.50,
    "bread": 1.75,
}

print(products["apple"])


# ============================================================
# Stage 2 — Key → Value
# ============================================================

# A hash table stores data as key → value pairs.

prices = {
    "apple": 1.00,
    "banana": 0.75,
    "orange": 1.25,
}

print(prices["banana"])


# ============================================================
# Stage 3 — Why Hash Tables Are Fast
# ============================================================

# In the average case, hash-table lookup is O(1).

print(prices["orange"])  # Average case: O(1)


# ============================================================
# Stage 4 — Hash Function
# ============================================================

# A hash function takes a string (or data) and maps it to a number.
# The number is then used to find a slot in the array.
#
# The function must be consistent:
# the same key should always produce the same result.


def hash_function(key, size):
    return sum(ord(char) for char in key) % size


# This is a simple deterministic toy function for illustration.
# The same key always produces the same result.


table_size = 10

index = hash_function("apple", table_size)

print(index)


# ============================================================
# Stage 5 — The Basic Idea
# ============================================================

# Conceptually:
#
# key
#  ↓
# hash function
#  ↓
# number (hash result)
#  ↓
# array index (number % table_size)
#  ↓
# stored value


# ============================================================
# Stage 6 — Collisions
# ============================================================

# A collision happens when different keys map to the same index.

key1 = "apple"
key2 = "orange"

index1 = hash_function(key1, table_size)
index2 = hash_function(key2, table_size)

print(index1)
print(index2)

# If index1 == index2, a collision has occurred.


# ============================================================
# Stage 7 — Collisions Are a Problem
# ============================================================

# Too many collisions make the hash table slower.
#
# In the worst case, many keys can end up together,
# making operations O(n).


# ============================================================
# Stage 8 — Avoiding Collisions
# ============================================================

# The chapter highlights two important factors:
#
# 1. A good hash function
# 2. A low load factor


# ============================================================
# Stage 9 — Load Factor
# ============================================================

# Load factor measures how full the hash table is.
#
# load factor = number of items / total slots

number_of_items = 2
total_slots = 5

load_factor = number_of_items / total_slots

print(load_factor)


# ============================================================
# Stage 10 — High Load Factor
# ============================================================

# As the load factor grows, collisions become more likely.

number_of_items = 7
total_slots = 10

load_factor = number_of_items / total_slots

print(load_factor)


# ============================================================
# Stage 11 — Resizing
# ============================================================

# When the table becomes too full, it needs more slots.
#
# A rule of thumb from the chapter:
# resize when the load factor becomes greater than 0.7.

load_factor = 0.8

if load_factor > 0.7:
    print("Resize the hash table")


# ============================================================
# Stage 12 — What Happens During Resizing?
# ============================================================

# 1. Create a larger array.
# 2. Reinsert the existing items.
# 3. Use the hash function again for the new indexes.

old_size = 5
new_size = old_size * 2

print(new_size)


# ============================================================
# Stage 13 — Resizing Is Expensive
# ============================================================

# Resizing takes time because existing items must be reinserted.
#
# However, averaged over many operations,
# hash tables still provide O(1) average performance.


# ============================================================
# Stage 14 — Hash Function Example
# ============================================================

# A good hash function distributes values evenly.
# This simple function is used only as a deterministic example.


def hash_function_example(key, size):
    return sum(ord(char) for char in key) % size


print(hash_function_example("apple", 10))
print(hash_function_example("banana", 10))
print(hash_function_example("orange", 10))


# ============================================================
# Stage 15 — Bad Hash Function
# ============================================================

# A bad hash function can map many keys to the same slot.


def bad_hash_function(key, size):
    return 1


print(bad_hash_function("apple", 10))
print(bad_hash_function("banana", 10))
print(bad_hash_function("orange", 10))

# All keys go to the same slot.
# This produces many collisions.


# ============================================================
# Stage 16 — Worst Case
# ============================================================

# If many keys collide, operations can degrade to O(n).

# Average case:
# Search → O(1)
# Insert → O(1)
# Delete → O(1)

# Worst case:
# Search → O(n)
# Insert → O(n)
# Delete → O(n)


# ============================================================
# Stage 17 — Python's Built-in Hash Table
# ============================================================

# In practice, you normally do not implement a hash table yourself.
# Python provides a built-in hash-table implementation: dict.

products = {
    "apple": 1.00,
    "banana": 0.75,
    "orange": 1.25,
}

print(products["apple"])

products["milk"] = 2.50
products["apple"] = 1.10

del products["banana"]

print(products)


# ============================================================
# Stage 18 — Final Mental Model
# ============================================================

# Hash Table
#
#        key
#         ↓
#   hash function
#         ↓
#    array index
#         ↓
#       value
#
# Performance depends heavily on:
#
# - Good distribution
# - Low load factor
# - Few collisions
#
# Average: O(1)
# Worst:   O(n)
