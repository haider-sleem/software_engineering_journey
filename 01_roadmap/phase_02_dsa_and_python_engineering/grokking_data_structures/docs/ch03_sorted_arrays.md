# Chapter 3: Sorted Arrays — Searching Faster, at a Price

> *Grokking Data Structures — Marcello La Rocca*

---

## Overview

Sorted arrays make searching dramatically faster — but maintaining sorted order makes insertion and deletion slower and more complex.

---

## Key Concepts

### Invariant

A condition that must always remain true: **the array must always stay sorted**. Every operation that modifies the array must preserve this invariant.

### Encapsulation

The underlying array is hidden from the user so they can't break the order manually. They must use the provided `insert` and `delete` methods.

### Capacity vs. Size

| Term | Meaning |
|------|---------|
| `capacity` (`max_size`) | Total memory allocated for the array |
| `size` | Actual number of elements currently stored |

`len(array)` should return `size`, not `capacity`.

---

## Operations

### Insertion

We cannot append at the end — the sorted order must be preserved.

1. Starting from the last active element, shift every element larger than the new value **one position to the right**.
2. Once the correct position is empty, insert the new value.
3. Increment `_size`.

**Complexity:** O(n) worst case due to shifting.

### Deletion

We cannot use the unsorted swap trick — swapping with the last element would break the sorted order.

1. Find the target's index (using search). If not found, raise an error.
2. Shift all elements to the right of the deleted index **one position to the left**, overwriting the deleted slot.
3. Decrement `_size`.

**Complexity:** O(n) worst case — finding the target and shifting elements may both contribute.

---

## Searching

### Linear Search

- Traverse from left to right looking for the target.
- **Early termination:** if an element larger than the target is encountered, stop — the array is sorted, so the target cannot exist further right.
- Still O(n) in the worst case, but early termination can reduce the actual number of comparisons.

### Binary Search

- Inspect the **middle element** of the active range.
- If the target is larger → discard the left half.
- If the target is smaller → discard the right half.
- Repeat using two pointers (`left` and `right`) that close in on each other.

**Complexity:** O(log n) — each comparison eliminates more than half the remaining elements. After two comparisons, over 75% is eliminated.

**Caveats:**
- **Duplicates:** standard binary search can find an occurrence of the target, but it doesn't guarantee the first or last occurrence — additional logic is needed.
- **Implementation:** known for being tricky to get exactly right on the first try — requires thorough testing.

---

## Traversal vs. Linear Search

| Aspect | Traversal | Linear Search |
|--------|-----------|---------------|
| **Purpose** | Visit and process every active element | Find a specific target value |
| **Range** | Always processes the full active range (index 0 to `_size - 1`) | Stops early when target is found or exceeded |
| **Target** | None — all elements treated equally | Requires a specific search target |
| **Example use** | Printing all values | Finding a product by name |

---

## Traversal

Visits every active element exactly once. In a sorted array, traversal is typically performed in **ascending order** (smallest to largest).

---

## Trade-off Summary

| Operation | Unsorted Array | Sorted Array |
|-----------|----------------|--------------|
| Insert    | O(1) at end | O(n) worst case — must shift to maintain order |
| Delete    | O(1) — swap with last | O(n) worst case — must shift to maintain order |
| Search    | O(n) — no early stop possible | O(log n) — binary search |

### When to Prefer a Sorted Array

Prefer a sorted array when the workload has a **high read-to-write ratio** — many more searches than insertions and deletions. If writes are frequent, the shifting cost makes sorted arrays expensive.