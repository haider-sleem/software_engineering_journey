# Chapter 2: Static Arrays — Building Your First Data Structure

> *Grokking Data Structures — Marcello La Rocca*

---

## What Is a Static Array?

- Fixed size determined at creation — cannot grow or shrink.
- In many implementations, elements have the same data type, allowing efficient memory allocation and address calculation.
- Indexed access is O(1) because the element's memory location can be calculated directly.

### Arrays in Python

| Type | Behavior |
|------|---------|
| `list` | Dynamic array-like structure — can grow/shrink, supports mixed types |
| `array` module | Type-consistent, but dynamically sized |
| True static array | Not natively provided by Python; can be simulated or provided by external libraries |

To simulate a fixed-capacity array in Python, pre-allocate a list with `[None] * N` and enforce the fixed capacity yourself — the list itself remains dynamic.

> **Optimization note:** dynamic structures offer flexibility at the cost of performance and memory overhead. Avoid optimizing until you've identified a real bottleneck — premature optimization is a known anti-pattern.

**Indexing rules (Python `list` of size `n`):**
- `[-1]` → last element
- `[-n]` → first element (`n > 0`)
- `[n]` → `IndexError`

---

## Design Concepts

### Left-Justified Array

Elements stored contiguously starting from index 0. Only one integer (`size`) is needed to distinguish meaningful data from empty space.

### Encapsulation

Group data (`_array`) and its metadata (`_size`) inside a class — prevents external code from modifying them out of sync.

### Composition over Inheritance

Use another class as an attribute (`self._array = Array()`) rather than inheriting from it. Provides better encapsulation and hides lower-level API details from the user.

---

## Unsorted Array Operations

### 1. Insertion

1. **Check capacity first** — if `self._size >= max_capacity`, raise an exception (e.g., `ValueError`). Don't hide errors.
2. **Place at `_size` index** — the left-justified rule: `_size` always points to the first empty slot.
3. **Increment `_size`** after a successful insertion.

**Complexity:** O(1)

### 2. Deletion — The Smart Swap Trick

Deleting from the middle and shifting everything left is O(n). Because the array is **unsorted** (order doesn't matter), we avoid shifting entirely:

1. Overwrite the element to delete with the **last active element**.
2. Decrement `_size` by 1.

**Complexity:** O(1)

### Array Loitering

After decrementing `_size`, the old last element remains in the underlying array outside the active portion. This is called **array loitering**. It is ignored by the data structure, but the stale reference may remain until that slot is overwritten or the array is released — in Python, this means the old object may be kept alive longer than expected.

### 3. Search (`find`)

- **Linear search** — the array is unsorted, so we check elements one by one.
- Returns the **index of the first occurrence** if found.
- Returns `None` if not found — avoids `-1` because that's a valid negative index in Python.

**Complexity:** O(n) worst case

### 4. Traversal (`traverse`)

Visit every active element exactly once. Accepts a **callback function** and applies it to each element:

```python
callback(self._array[index])
```

Used for applying an operation to every active element, typically one with a side effect (printing, logging). If we need to collect the results, that is closer to a `map` operation.

---

## Fixed-Size Frequency Counters

Arrays can track frequencies where each index maps to a specific category.

**Example — Dice faces (1 to 6) → indices (0 to 5):**

```python
counts = [0] * 6
counts[face - 1] += 1  # index mapping: k - 1
```

**Finding extremes:** initialize with the first element (`max_index = 0`), not a hardcoded default — makes the function safer and more generic.

---

## Collections and Multidimensional Arrays

- Unsorted arrays naturally model fixed-capacity collections (e.g., a card binder) — append freely, search, delete.
- Arrays can store other arrays, forming **matrices** and multidimensional structures.
- Widely used in linear algebra, machine learning, and physics simulations.