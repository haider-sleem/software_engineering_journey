# Chapter 5: Dynamic Arrays — Handling Dynamically Sized Datasets

> *Grokking Data Structures — Marcello La Rocca*

---

## Why Dynamic Arrays?

Static arrays have a fixed size in a contiguous block of memory. When resizing is needed, a new larger block must be allocated and all elements copied — expensive. Pre-allocating large static arrays avoids frequent resizing but wastes memory if underused.

Dynamic arrays automate size management, trading a minor performance overhead for flexibility and efficient memory usage.

---

## Growth Strategy: Why Doubling?

| Strategy | Total cost over n insertions | Why |
|----------|---------------------------|-----|
| **Constant growth** (+1 or +X per resize) | O(n²) | Reallocations happen too frequently |
| **Geometric growth** (×2 per resize) | O(n) total — O(1) amortized per insertion | Reallocations become exponentially rarer |

**Intuition:** doubling spaces out reallocations exponentially. The cost of copying is "spread" over the many cheap insertions between reallocations — each insertion costs O(1) on average, even though occasional copies are expensive.

Dynamic arrays trade a small amount of unused memory (capacity overhead) for dramatically better insertion performance.

---

## Shrinking Strategy: Avoiding Thrashing

Shrinking is essential to prevent memory waste after usage spikes, but the timing matters:

| Strategy | Problem |
|----------|---------|
| **Halve at 50% usage** | Causes thrashing — a sequence of insert/delete around the boundary triggers constant resizing (O(n²) total cost) |
| **Halve at 25% usage** | Provides a buffer — avoids rapid back-and-forth resizing while still recovering wasted memory |

Delaying shrinking until utilization drops to 25% is a **safe and reasonably effective strategy** that helps avoid repeated resizing — though the ideal threshold depends on the use case.

---

## Implementation Overview

`DynamicArray` wraps a core `Array` using **composition** and tracks `size`, `capacity`, and `typecode`.

> A dynamic array is not a fundamentally different structure — it uses a fixed-size array underneath and automatically resizes it when needed.

| Operation | Complexity | Notes |
|-----------|-----------|-------|
| `insert` | O(1) amortized | Triggers `_double_size()` when full |
| `find` | O(n) | Linear scan over active elements |
| `delete` | O(n) | Linear search + shifting elements; may also trigger shrinking |

---

## When to Use Static vs. Dynamic Arrays

| Choice | When |
|--------|------|
| **Static array** | Number of elements is known in advance or changes only slightly |
| **Dynamic array** | Dataset size is unpredictable or varies significantly over time |