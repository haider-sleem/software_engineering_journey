# ============================================================
# Chapter 4 — Quicksort
# Grokking Algorithms
#
# A small warehouse story that introduces:
# Divide and Conquer, recursion, Quicksort,
# pivot, partitioning, and Big-O behavior.
# ============================================================


# ============================================================
# STAGE 1 — The Warehouse Problem
# ============================================================

# The warehouse receives product prices in random order.
prices = [10, 5, 2, 3]

print("Unsorted prices:", prices)


# ============================================================
# STAGE 2 — Divide and Conquer
# ============================================================

# Divide and Conquer solves a problem by:
#
# 1. Finding a simple base case.
# 2. Breaking the problem down into smaller and smaller pieces
#    until it reaches that base case.
#
# D&C is a way of thinking about a problem.
# It is commonly implemented using recursion.


# ============================================================
# STAGE 3 — Recursive Sum
# ============================================================

# Before Quicksort, consider a simpler problem:
# calculate the sum of all prices.


def sum_prices(prices):
    # Base case: an empty list has a sum of 0.
    # This is the simplest case — no more work to do.
    if len(prices) == 0:
        return 0

    # Recursive case:
    # add the first price to the sum of the remaining prices.
    # Each call brings us closer to the base case.
    return prices[0] + sum_prices(prices[1:])


# Note: for Quicksort, the base case is len(array) < 2,
# because a list of 0 or 1 elements is already sorted.
# The base case depends on the problem being solved.


print("Total:", sum_prices([10, 5, 2, 3]))


# ============================================================
# STAGE 4 — Why the Base Case Matters
# ============================================================

# Every recursive solution needs a stopping point.
#
# For array problems, an empty array or a one-element array
# is often a useful base case.


# ============================================================
# STAGE 5 — Start Quicksort
# ============================================================

# Quicksort is a sorting algorithm based on Divide and Conquer.
#
# The basic process is:
#
# 1. Choose a pivot.
# 2. Partition the remaining elements.
# 3. Recursively sort the two sub-arrays.
# 4. Combine the results.


# ============================================================
# STAGE 6 — Quicksort Base Case
# ============================================================


def quicksort(prices):
    # An empty list or one-element list is already sorted.
    if len(prices) < 2:
        return prices


# ============================================================
# STAGE 7 — Choose a Pivot
# ============================================================


def quicksort(prices):  # noqa
    if len(prices) < 2:
        return prices

    # The first element is used as the pivot.
    pivot = prices[0]  # noqa


# ============================================================
# STAGE 8 — Partition the Array
# ============================================================


def quicksort(prices):  # noqa
    if len(prices) < 2:
        return prices

    pivot = prices[0]

    # Elements less than or equal to the pivot.
    less = [price for price in prices[1:] if price <= pivot]  # noqa

    # Elements greater than the pivot.
    greater = [price for price in prices[1:] if price > pivot]  # noqa


# ============================================================
# STAGE 9 — Recursively Sort Both Sides
# ============================================================


def quicksort(prices):  # noqa
    if len(prices) < 2:
        return prices

    pivot = prices[0]

    less = [price for price in prices[1:] if price <= pivot]
    greater = [price for price in prices[1:] if price > pivot]

    # Recursively sort both sub-arrays.
    sorted_less = quicksort(less)  # noqa
    sorted_greater = quicksort(greater)  # noqa


# ============================================================
# STAGE 10 — Combine the Results
# ============================================================


def quicksort(prices):  # noqa
    if len(prices) < 2:
        return prices

    pivot = prices[0]

    less = [price for price in prices[1:] if price <= pivot]
    greater = [price for price in prices[1:] if price > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


prices = [10, 5, 2, 3]

print("Sorted prices:", quicksort(prices))


# ============================================================
# STAGE 11 — See the Partition
# ============================================================

prices = [10, 5, 2, 3]

pivot = prices[0]

less = [price for price in prices[1:] if price <= pivot]
greater = [price for price in prices[1:] if price > pivot]

print("Pivot:", pivot)
print("Less:", less)
print("Greater:", greater)


# ============================================================
# STAGE 12 — The Recursive Idea
# ============================================================

# The sub-arrays do not have to be sorted yet.
#
# Quicksort keeps reducing them:
#
# [10, 5, 2, 3]
#       ↓
# [5, 2, 3] + [10] + []
#       ↓
# [2, 3] + [5] + []
#       ↓
# [2] + [3] + []
#
# Eventually every sub-array reaches the base case.


# ============================================================
# STAGE 13 — Pivot Quality
# ============================================================

# Pivot choice strongly affects Quicksort's performance.
#
# A reasonably balanced pivot:
#
#       [large problem]
#          /       \
#      smaller    smaller
#
# creates shorter recursive paths.
#
# A poor pivot:
#
#       [large problem]
#             \
#           almost all
#
# creates a long recursive path.


# ============================================================
# STAGE 14 — Best Case
# ============================================================

# If each pivot divides the array into reasonably balanced parts,
# the recursive depth is approximately O(log n).
#
# Each level processes O(n) elements.
#
# Therefore:
#
# O(n) * O(log n) = O(n log n)


# ============================================================
# STAGE 15 — Worst Case
# ============================================================

# If the pivot repeatedly produces one empty sub-array
# and one almost-full sub-array:
#
# [1, 2, 3, 4, 5]
#  ^
# pivot
#
# the recursive depth becomes O(n).
#
# Across one level of the recursion tree,
# the total work is O(n).
#
# Therefore:
#
# O(n) * O(n) = O(n²)


# ============================================================
# STAGE 16 — Average Case
# ============================================================

# With a random pivot, Quicksort runs in O(n log n) on average.
#
# This is why pivot selection matters.
#
# Caveat: if all elements are equal, this simple implementation
# may still reach O(n²) without additional logic to handle duplicates.


# ============================================================
# STAGE 17 — Call Stack
# ============================================================

# Quicksort uses recursion, so every recursive call uses
# the call stack.
#
# Best case:
#     O(log n) stack space
#
# Worst case:
#     O(n) stack space


# ============================================================
# STAGE 18 — Quicksort vs. Selection Sort
# ============================================================

# Selection Sort:
#
#     O(n²)
#
# Quicksort:
#
#     Average: O(n log n)
#     Worst:   O(n²)
#
# Quicksort can therefore be much faster for large inputs
# when the partitions are reasonably balanced.


# ============================================================
# STAGE 19 — Big-O vs. Real Runtime
# ============================================================

# Big-O ignores constant factors.
#
# For example:
#
#     10 ms * n
#     1 second * n
#
# are both O(n).
#
# The constants can still affect actual runtime.
# However, when growth rates differ significantly,
# the Big-O difference usually becomes much more important.


# ============================================================
# STAGE 20 — Final Warehouse Example
# ============================================================

products = [
    {"name": "Keyboard", "price": 25},
    {"name": "Mouse", "price": 15},
    {"name": "Monitor", "price": 100},
    {"name": "USB Cable", "price": 5},
]


def quicksort_products(products):
    # Base case.
    if len(products) < 2:
        return products

    # Choose the first product as the pivot.
    pivot = products[0]

    # Partition by price.
    cheaper = [
        product for product in products[1:] if product["price"] <= pivot["price"]
    ]

    more_expensive = [
        product for product in products[1:] if product["price"] > pivot["price"]
    ]

    # Recursively sort both partitions.
    return quicksort_products(cheaper) + [pivot] + quicksort_products(more_expensive)


sorted_products = quicksort_products(products)

for product in sorted_products:
    print(product["name"], product["price"])


# ============================================================
# END OF CHAPTER 4
# ============================================================
