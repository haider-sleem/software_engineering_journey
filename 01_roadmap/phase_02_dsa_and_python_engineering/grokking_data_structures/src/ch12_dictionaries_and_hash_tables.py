"""
Grokking Data Structures
Chapter 12 — Dictionaries and Hash Tables
"""

# ============================================================
# Stage 1 — The Dictionary Problem
# ============================================================

# A dictionary stores values that can be accessed by a key.
#
# Example:
#
#     product_id -> product
#     username   -> email
#     word       -> definition
#
# Main operations:
#
#     insert
#     search
#     delete


# ============================================================
# Stage 2 — Dictionary Implementations
# ============================================================

# Different data structures can implement a dictionary.
#
# Examples:
#
#     Array
#     Linked List
#     Balanced Binary Search Tree
#     Hash Table
#
# Each implementation has different performance tradeoffs.


# ============================================================
# Stage 3 — Direct-Access Table
# ============================================================

# A direct-access table uses the key directly as an array index.
#
#     key = 3
#       ↓
#     array[3]
#
# This gives O(1) access.
#
# The problem:
#
# If the possible keys are very large but only a few keys
# are actually stored, most array positions remain unused.
#
# This can waste a large amount of memory.


# ============================================================
# Stage 4 — Hash Tables
# ============================================================

# A hash table maps a key to an array index.
#
#     key
#      ↓
# hash function
#      ↓
#    index
#      ↓
#    array
#
# The table can therefore be much smaller than the possible
# range of keys.


# ============================================================
# Stage 5 — Hash Function
# ============================================================


def hash_function(key, table_size):
    # A hash function converts a key into a valid array index.
    # This example assumes the key is a non-negative integer.
    return key % table_size


index = hash_function(1119, 10)

print(index)
# 9


# ============================================================
# Stage 6 — A Good Hash Function
# ============================================================

# A good hash function should distribute keys as evenly
# as possible across the table.
#
# Ideally:
#
#     key A ──→ different bucket
#     key B ──→ different bucket
#     key C ──→ different bucket
#
# Poor distribution causes many keys to occupy the same
# bucket and makes the hash table slower.


# ============================================================
# Stage 7 — Division Method
# ============================================================

# The division method uses:
#
#     h(k) = k % m
#
# where:
#
#     k = integer key
#     m = table size
#
# A common rule is to choose a prime number for the table size
# when using this method.


# ============================================================
# Stage 8 — Multiplication Method
# ============================================================

# Another hashing method is the multiplication method.
#
# Formula:
#
#     A = (sqrt(5) - 1) / 2  ≈  0.618...
#
#     h(k) = floor(m * ((A * k) % 1))
#
# where:
#
#     k = integer key
#     m = table size
#     A = Knuth's constant — chosen because it distributes
#         keys well across many table sizes
#
# The multiplication method can help distribute nearby keys
# more evenly than the division method.


import math  # noqa

A = (math.sqrt(5) - 1) / 2


def hash_multiplication(key, table_size):
    return math.floor(table_size * ((A * key) % 1))


# ============================================================
# Stage 9 — Collision
# ============================================================

# Different keys can produce the same index.
#
# Example:
#
#     key A ──┐
#             ├──→ index 3
#     key B ──┘
#
# This is a collision.
#
# Collisions are unavoidable when there are more possible keys
# than table positions.
#
# A hash table therefore needs a collision-resolution strategy.


# ============================================================
# Stage 10 — Chaining
# ============================================================

# One way to resolve collisions is chaining.
#
# Each table position can point to a linked list.
#
#     0 → [A] → [C] → None
#     1 → [B] → None
#     2 → None
#     3 → [D] → [E] → None
#
# Multiple keys can therefore occupy the same bucket.


# ============================================================
# Stage 11 — Hash Table with Chaining
# ============================================================


class HashTable:
    def __init__(self, size):
        # A table size of zero would cause a ZeroDivisionError
        # when computing the index with key % self.size.
        if size <= 0:
            raise ValueError("Table size must be greater than zero.")

        self.table = [None] * size
        self.size = size

    def insert(self, key, value):
        index = key % self.size

        if self.table[index] is None:
            self.table[index] = []

        # Note: this implementation uses a Python list as the bucket,
        # not a linked list. list.append() is O(1) amortized.
        #
        # Also note: this insert does NOT check for duplicate keys.
        # The same key can be inserted more than once.
        # The book's analysis assumes no duplicate checking, giving O(1) insert.
        # If duplicate checking were required, insert would become O(n) worst case.
        self.table[index].append((key, value))

    def search(self, key):
        index = key % self.size
        bucket = self.table[index]

        if bucket is None:
            return None

        for stored_key, value in bucket:
            if stored_key == key:
                return value

        return None

    def delete(self, key):
        index = key % self.size
        bucket = self.table[index]

        if bucket is None:
            return

        for position, (stored_key, value) in enumerate(bucket):
            if stored_key == key:
                del bucket[position]
                return


# ============================================================
# Stage 12 — Using the Hash Table
# ============================================================

products = HashTable(10)

products.insert(101, "Keyboard")
products.insert(202, "Mouse")
products.insert(111, "Monitor")

print(products.search(101))
# Keyboard

products.delete(101)

print(products.search(101))
# None


# ============================================================
# Stage 13 — Why Collisions Matter
# ============================================================

# If many keys are mapped to the same bucket:
#
#     index 4
#       ↓
#     [A] → [B] → [C] → [D]
#
# Searching becomes slower because the bucket must be scanned.
#
# With good distribution, buckets remain short and operations
# stay close to O(1) on average.


# ============================================================
# Stage 14 — Open Addressing
# ============================================================

# Another collision-resolution strategy is open addressing.
#
# Instead of storing a linked list in each bucket, the elements
# are stored directly inside the table.
#
# When a collision occurs:
#
#     1. Calculate the first index.
#     2. If occupied, try another index.
#     3. Continue until an available position is found.
#
# The exact sequence depends on the probing strategy.


# ============================================================
# Stage 15 — Linear Probing
# ============================================================

# Linear probing checks the next positions sequentially.
#
# Conceptually:
#
#     first position
#          ↓
#     occupied?
#          ↓ yes
#     next position
#          ↓
#     occupied?
#          ↓ yes
#     next position
#          ↓
#       empty → insert
#
# A common formula is:
#
#     (hash(key) + attempt) % table_size


# ============================================================
# Stage 15b — Quadratic Probing
# ============================================================

# Quadratic probing is another open-addressing strategy.
#
# Instead of checking the next position linearly, it uses
# a quadratic formula to compute the probe sequence.
#
# General form:
#
#     p(k, i) = (h(k) + a*i + b*i²) % m
#
# where a and b are constants that determine the stepping pattern.
#
# The simple form (a=0, b=1) shown in the book:
#
#     attempt 0 → hash(key) % m
#     attempt 1 → (hash(key) + 1) % m
#     attempt 2 → (hash(key) + 4) % m
#     attempt 3 → (hash(key) + 9) % m
#     ...
#
# This is a specific choice, not a universal rule.
#
# Advantage over linear probing:
#     reduces clustering — nearby keys are spread more widely.
#
# Limitation:
#     not all positions are guaranteed to be visited,
#     so it may fail to find an empty slot even if one exists.


# ============================================================
# Stage 15c — Deletion in Open Addressing
# ============================================================

# Deleting from an open-addressing hash table is not as simple
# as setting the slot to None.
#
# Problem:
#
#     Suppose keys A, B, C are inserted and B collides with A:
#
#         slot 3 → A
#         slot 4 → B  (placed here by probing)
#         slot 5 → C  (placed here by probing)
#
#     If we delete B by setting slot 4 → None:
#
#         Searching for C reaches slot 4, finds None, and STOPS.
#         C is never found, even though it is stored at slot 5.
#
# Solution:
#     Mark the deleted slot with a special "tombstone" sentinel
#     instead of None. The search passes through tombstones but
#     can insert into them.
#
# A tombstone is a special marker that distinguishes a slot
# that was deleted from a slot that has never been used.


# ============================================================
# Stage 16 — Chaining vs Open Addressing
# ============================================================

# Chaining:
#
#     table → linked lists
#
# Advantages:
#     - Handles collisions naturally.
#     - Can store more elements than table positions.
#     - Deletion is simpler.
#
# Open addressing:
#
#     table → elements directly
#
# Advantages:
#     - No linked-list nodes.
#     - Lower additional memory overhead.
#
# But deletion is more complicated because removing an element
# can break future searches.


# ============================================================
# Stage 17 — Hash Table Performance
# ============================================================

# Theoretical analysis (book — Linked List chaining,
# assuming no duplicate checking):
#
#     Average:
#         insert          → O(1), assuming no duplicate check
#                             and insertion at the list front
#         search, delete  → O(1 + α) average
#         where α = n/m is the load factor
#
#     Worst case:
#         insert  → O(1)
#         search  → O(n)
#         delete  → O(n)
#
# This implementation (Python list as bucket):
#     append() is O(1) amortized — most operations are fast,
#     but an individual append may trigger O(n) reallocation.
#     Asymptotically equivalent, but the individual-operation
#     guarantee is weaker.
#
#     search and delete are O(n) when all keys share
#     the same bucket.
#
#     If duplicate checking is required, insert becomes
#     O(n) worst case because the bucket must be searched.
#
# When the load factor is bounded and keys are well distributed,
# all operations can be described as O(1) on average.


# ============================================================
# Stage 18 — Hash Table and the Warehouse
# ============================================================

# A warehouse can use a dictionary/hash table to associate
# product IDs with product information.
#
#     product ID
#          ↓
#     hash function
#          ↓
#        bucket
#          ↓
#       product
#
# This allows fast average-case lookup:
#
#     product_id → product information


# ============================================================
# Stage 19 — Important Limitation
# ============================================================

# Hash tables are designed mainly for:
#
#     insert
#     search
#     delete
#
# They are not optimized for ordered operations such as:
#
#     minimum
#     maximum
#     successor
#     predecessor
#
# These operations are possible on a hash table, but require
# scanning all buckets and their contents — O(n + m) in the
# worst case, where n is the number of items and m is the
# number of buckets.
#
# Data structures such as balanced BSTs support ordered
# operations in O(log n), making them more suitable when
# ordered access is important.


# ============================================================
# Stage 19b — Hashing Risks
# ============================================================

# If an attacker can predict the hash function,
# they may craft keys that all map to the same bucket.
#
# This can make search and delete take O(n) per operation.
#
# If duplicate checking is required, insert may also
# become O(n) in the worst case.
#
# Repeated expensive operations can seriously degrade
# server performance, potentially causing a DoS attack.
#
# A possible defense is to introduce randomization into
# the hash function, making collisions harder to predict.
#
# This reduces the risk but does not guarantee
# protection against every adversarial input.


# ============================================================
# Stage 20 — Final Mental Model
# ============================================================

# Dictionary:
#
#     "I want to associate a key with a value."
#
# Hash table:
#
#     key
#      ↓
# hash function
#      ↓
# index
#      ↓
# bucket / table position
#      ↓
# value
#
# Main idea:
#
#     Hash tables trade ordering for very fast
#     average-case key-based operations.
#
# Core complexity:
#
#     Average → O(1)
#     Worst   → O(n)
#
# The quality of the hash function and the way collisions
# are resolved strongly affect performance.


# ============================================================
# Chapter 12 Complete
# ============================================================
