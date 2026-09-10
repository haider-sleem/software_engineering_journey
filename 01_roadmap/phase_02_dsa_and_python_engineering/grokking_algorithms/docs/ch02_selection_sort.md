# Chapter 2: Selection Sort & Data Structures

> *Grokking Algorithms — Aditya Bhargava*

---

## How Memory Works

Computer RAM acts like a giant set of drawers — each drawer stores a piece of data and has a unique byte address (e.g., `fe0ffeeb`) for direct access. Requesting memory from the OS assigns specific address(es) to store variables.

Storing multiple items relies on two foundational approaches:
1. **Contiguous allocation** → Arrays
2. **Pointer-based allocation** → Linked Lists

---

## Arrays vs. Linked Lists

### Access Patterns

| Structure | Access Type | Complexity | Why |
|-----------|------------|-----------|-----|
| **Array** | **Random Access** | O(1) | Any element reachable directly via index (`base + i × size`) |
| **Linked List** | **Sequential Access** | O(n) | Must traverse from the head — no way to jump to the middle |

This distinction is the core of the chapter: arrays support random access; linked lists only support sequential access.

### Insert and Delete

| Operation | Array | Linked List |
|-----------|-------|-------------|
| **Insert at end** (space available) | O(1) | O(1) — if you have a tail pointer |
| **Insert in middle / beginning** | O(n) — elements must shift | O(1) — *if you already have a pointer to that node* |
| **Insert when array is full** | O(n) — reallocate + copy everything (needs a contiguous block) | Not applicable — linked list can always insert as long as any free memory exists anywhere |
| **Delete at end** | O(1) — just decrement length | O(1) — if you have a tail pointer |
| **Delete in middle / beginning** | O(n) — elements must shift | O(1) — *if you already have a pointer to that node* |

> **Key constraint:** Linked list insert/delete is O(1) **only when you already hold a pointer to the node**. Finding that node first costs O(n).

### Memory Trade-offs

| Structure | Risk |
|-----------|------|
| **Array** | May waste memory (over-preallocation), or pay O(n) to resize |
| **Linked List** | Extra bytes per node for storing the next pointer |

---

## When to Use Each

| Situation | Better Choice | Why |
|-----------|--------------|-----|
| Lots of random reads | Array | O(1) access |
| Lots of inserts/deletes in the middle | Linked List | O(1) modification (with pointer) |
| Read email/messages sequentially | Array | Cache-friendly sequential reads |
| Music playlist (frequent add/remove) | Linked List | Cheap pointer updates |

---

## Why Arrays Are Usually Faster in Practice

**Random access via index:** arrays compute the element address directly (`base + i × size`) — no traversal needed. This is what makes O(1) access possible, independent of caching.

**Spatial Locality & CPU Caching:** arrays store elements contiguously, so the CPU often loads nearby elements into cache together (cache lines), making sequential reads fast in practice.

**Linked list cache disadvantage:** node addresses are scattered across memory, causing frequent cache misses during traversal.

> *Note: spatial locality explains why sequential array reads are fast in practice. The O(1) random access itself is purely about address arithmetic.*

---

## Selection Sort

**Concept:** repeatedly find the smallest element from the unsorted portion and move it to a new sorted list.

### Time Complexity

- Finding the smallest element in a list: **O(n)**
- Repeating this `n` times: **O(n × n) = O(n²)**
- Even though the unsorted portion shrinks each pass (average size ½ × n), constants are dropped in Big O — the result stays **O(n²)**

**Intuition:** Selection Sort makes roughly n × n/2 comparisons — that's a lot even for moderately large inputs, making it impractical for real-world data.

**Takeaway:** Selection Sort is simple to implement and good for learning, but not efficient for large datasets. It exists here as a teaching example — Quicksort (O(n log n)) is preferred in production.

### Python Implementation Pattern

```python
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    copied_arr = list(arr)  # copy to avoid modifying the original
    for _ in range(len(arr)):
        smallest = find_smallest(copied_arr)
        new_arr.append(copied_arr.pop(smallest))
    return new_arr
```

- `list(arr)` creates a safe copy without modifying the original.
- `.pop(smallest_index)` removes the element and shifts the remaining ones — this is an additional O(n) cost per pass in the book's version, but the fundamental source of O(n²) is the `find_smallest` scan repeated n times. Replacing `.pop` with an in-place swap would still be O(n²).

---

## Connection to Chapter 1

Binary Search (Chapter 1) requires a **sorted** list with **random access** — which is why it only works on arrays, not linked lists.

---

## Python Note

Python's built-in `list` is a **dynamic array**, not a linked list. It supports O(1) indexed access and amortized O(1) append — not the O(1) middle-insertion of a linked list.