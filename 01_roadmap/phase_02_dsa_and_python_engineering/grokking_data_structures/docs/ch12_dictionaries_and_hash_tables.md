# Chapter 12 — Dictionaries and Hash Tables

## 1. The Dictionary ADT

A **dictionary** is an ADT for storing values that can later be searched or deleted by **key**.

Core operations:

- `insert` — add a value.
- `search` — retrieve the value associated with a key.
- `delete` — remove a value or key.

A dictionary stores **key-value associations**.

Examples:

```text
product_id → product
username   → email
word       → definition
````

Python's `dict` is an implementation of this idea.

---

## 2. Implementing a Dictionary

Several data structures can implement the Dictionary ADT:

| Implementation              |   Insert |   Search |   Delete |
| --------------------------- | -------: | -------: | -------: |
| Unsorted array              |     O(1) |     O(n) |     O(n) |
| Sorted array                |     O(n) | O(log n) |     O(n) |
| Unsorted doubly linked list |     O(1) |     O(n) |     O(n) |
| Sorted doubly linked list   |     O(n) |     O(n) |     O(n) |
| Balanced BST                | O(log n) | O(log n) | O(log n) |

* **Balanced BSTs** provide good performance across all main dictionary operations.
* **Hash tables** provide better average performance for insert, search, and delete.

---

## 3. Direct-Access Tables

A **direct-access table** uses the key itself as the array index:

```text
key → array index
```

For example:

```text
key = 3
     ↓
array[3]
```

This gives constant-time access.

### Problem

The range of possible keys can be enormous compared with the number of stored elements.

Most array cells may remain empty, causing huge memory waste.

Therefore, direct-access tables are practical only when the key range is reasonably small.

---

## 4. Hash Tables

A **hash table** solves the large-key-range problem.

Instead of using the key directly as an array index:

```text
key → index
```

we use:

```text
key → hash function → index
```

The hash table can therefore be much smaller than the range of possible keys.

A hash function must return a valid index:

```text
0 ≤ index < m
```

where `m` is the table size.

---

## 5. Hash Function

A hash function:

* Accepts all possible keys in its domain.
* Returns a valid table index.
* Should distribute keys as uniformly as possible.

The ideal property is **uniformity**:

> Each key should be equally likely to map to any table slot.

Perfect uniformity is difficult to achieve, so practical hash functions use heuristics that avoid patterns in the input data.

---

## 6. Extracting an Integer Key

Objects may not have integer keys.

A common process is:

```text
Object
  ↓
Extract unique ID
  ↓
Convert to integer
  ↓
Hash integer
  ↓
Table index
```

For example, a string can be converted into an integer by treating its characters as digits in a base-256 representation.

The cost of extracting a key may depend on the size of the object.

---

## 7. Division Method

The **division method** computes the index as:

```text
h(k) = k % m
```

where:

* `k` = integer key
* `m` = hash table size

Example:

```text
k = 1119
m = 10

1119 % 10 = 9
```

So the key is stored at index `9`.

### Table size

When using the division method, a common rule of thumb is to choose `m` as a **prime number** that is not close to a power of two.

---

## 8. Multiplication Method

The **multiplication method** uses a constant `A`:

```text
h(k) = floor(m * ((A * k) % 1))
```

where `m` is the table size.

A commonly recommended value is:

```text
A = (√5 - 1) / 2
```

The multiplication method gives more freedom when choosing the table size.

It also tends to spread nearby keys farther apart, helping distribute the load across the table.

---

## 9. Hashing Conflicts

A hash table usually has fewer cells than possible keys.

Therefore, two different keys can map to the same index.

This is called a **conflict** or **collision**:

```text
key A ──┐
        ├──→ index 3
key B ──┘
```

Conflicts cannot be completely avoided.

They must be **resolved**.

The chapter presents two main strategies:

1. **Chaining**
2. **Open Addressing**

---

## 10. Chaining

With **chaining**, each table cell stores the head of a linked list.

```text
0 → [A] → [C] → None
1 → [B] → None
2 → None
3 → [D] → [E] → None
```

Multiple values can therefore occupy the same bucket.

When inserting, the new element can be added to the front of the linked list.

### Why a linked list?

A hash bucket may contain multiple elements, so the list allows the bucket to grow as needed.

---

## 11. Chaining Performance

Suppose:

* `m` = number of buckets
* `n` = number of stored elements

On average, each bucket contains:

```text
n / m
```

elements.

With chaining:

> **Assumption:** duplicate checking is not required, and new elements are inserted at the front of each linked list.

| Operation |    Average | Worst Case |
| --------- | ---------: | ---------: |
| Insert    |       O(1) |       O(1) |
| Search    | O(1 + n/m) |       O(n) |
| Delete    | O(1 + n/m) |       O(n) |

Insert is O(1) when new elements are added to the front and duplicate checking is not required. If keys must be unique and duplicate checking is required, insert can become O(n) in the worst case.

If all keys end up in one bucket, search and delete can become O(n).

---

## 12. Iteration and Extra Operations

Iterating through all elements requires visiting the table's buckets and stored elements:

```text
O(n + m)
```

Finding operations such as:

* minimum
* maximum
* successor
* predecessor

also require scanning the table and therefore take:

```text
O(n + m)
```

Hash tables are optimized mainly for:

```text
insert
search
delete
```

not for ordered operations.

---

## 13. Open Addressing

**Open addressing** stores elements directly inside the hash table.

When a collision occurs, the table probes another position.

Conceptually:

```text
First index
    ↓
occupied?
    ↓ yes
Try another index
    ↓
occupied?
    ↓ yes
Try another index
    ↓
empty → insert
```

The probing function depends on:

```text
key + attempt number
```

For a valid probing strategy, the sequence of positions should eventually cover every table index.

---

## 14. Linear Probing

One common probing method is **linear probing**:

```text
p(k, i) = (h(k) + i) % m
```

After a collision, it checks the next position:

```text
h(k)
h(k) + 1
h(k) + 2
...
```

This is simple but can create clusters of elements.

---

## 15. Quadratic Probing

Another method is **quadratic probing**:

```text
p(k, i) = (h(k) + a*i + b*i²) % m
```

It spreads probes differently from linear probing and can reduce some clustering.

However, not every choice of `a` and `b` produces a valid sequence covering the whole table.

---

## 16. Chaining vs. Open Addressing

|                           | Chaining                   | Open Addressing      |
| ------------------------- | -------------------------- | -------------------- |
| Storage                   | Linked lists + table       | Table only           |
| Capacity                  | Can grow beyond table size | `n ≤ m`              |
| Memory overhead           | Higher                     | Lower                |
| Deletion                  | Simpler                    | Complicated          |
| Clustering                | No probing clusters        | Can occur            |
| Empty slots               | Can remain empty           | Important for search |
| Recommended when deleting | Yes                        | Problematic          |

The chapter's recommendation is:

> If you need to delete items, use **chaining**.

---

## 17. Why Deletion Is Difficult in Open Addressing

Suppose:

```text
key A → index 1
key B → index 6
```

and `B` was placed at index 6 after probing.

If we simply delete the element at index 1 and leave the cell empty, a later search for `B` might stop at index 1 and incorrectly conclude that `B` does not exist.

Possible solutions use special markers for deleted cells, but this makes searching slower and complicates the implementation.

---

## 18. Hash Table Performance

With chaining:

- **Insert:** O(1) when duplicate checking is not required.
- **Search and delete:** O(1 + n/m) on average.
- **Search and delete:** O(n) in the worst case.

When the load factor remains bounded and keys are distributed well, average insert, search, and delete operations can be described as O(1).

Worst-case performance can be O(n), especially when many keys collide.

---

## 19. Hashing Risks

A deterministic or predictable hash function can create a security problem.

If an attacker can discover which keys map to the same bucket, they can deliberately send many such keys.

This can turn normally fast hash-table operations into very slow operations.

A possible countermeasure is to introduce a **random element** into the hash function when the table is created.

The goal is to prevent an attacker from predicting the key-to-bucket mapping.

---

## 20. Key Takeaways

* A **Dictionary ADT** stores values that can be accessed by key.
* Arrays, linked lists, and balanced BSTs can implement dictionaries.
* **Balanced BSTs** provide O(log n) operations across the main dictionary operations.
* **Hash tables** provide O(1) average insert, search, and delete.
* A **direct-access table** uses the key directly as an array index but can waste enormous amounts of memory.
* A **hash function** converts a key into a valid table index.
* **Collisions** are unavoidable when the key range is larger than the table.
* **Chaining** resolves collisions using linked lists.
* **Open addressing** resolves collisions by probing other table positions.
* Open addressing saves memory but makes deletion difficult and performance sensitive to table filling.
* Hash tables have **O(n)** worst-case performance.
* Hash functions should distribute keys as uniformly as possible.
* Hash tables are mainly optimized for **insert, search, and delete**, not ordered operations.
