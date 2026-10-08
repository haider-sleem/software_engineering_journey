# Chapter 5 — Hash Tables

## 1. What Is a Hash Table?

A hash table is a data structure that combines:

- An **array**
- A **hash function**

It stores data as **key → value** pairs.

Example:

```text
"apple" → $1.00
"milk"  → $2.50
```

Hash tables are useful when you need to look up a value quickly by its key.

---

## 2. Performance

In the **average case**:

| Operation | Hash Table |
| --------- | ---------: |
| Search    |       O(1) |
| Insert    |       O(1) |
| Delete    |       O(1) |

In the **worst case**:

| Operation | Hash Table |
| --------- | ---------: |
| Search    |       O(n) |
| Insert    |       O(n) |
| Delete    |       O(n) |

The worst case happens when many keys collide.

In the average case, hash tables combine useful properties of arrays and linked lists:

- Search is as fast as an array.
- Insert and delete are as fast as a linked list.

In the worst case, all three operations can become O(n).

---

## 3. Hash Functions

A **hash function** takes a string (or data) and maps it to a number.

```text
key → hash function → number
```

The hash function must be **consistent**: the same key should always produce the same result.

A good hash function:

* Distributes values evenly across the array.
* Minimizes collisions.

A bad hash function:

* Groups many values together.
* Produces many collisions.

---

## 4. Collisions

A **collision** happens when two different keys map to the same array index.

```text
key1 ──┐
       ├──→ same index
key2 ──┘
```

Collisions cannot always be avoided.

The goal is to **minimize collisions** with:

* A good hash function
* A low load factor

---

## 5. Load Factor

The **load factor** measures how full a hash table is.

```text
load factor = number of occupied slots / total slots
```

Example:

```text
2 occupied slots
---------------- = 0.4
5 total slots
```

As the load factor increases, collisions become more likely.

When the table becomes too full, it can be **resized**.

### Resizing

A common rule of thumb is:

1. Create a larger array.
2. Make it about twice the original size.
3. Reinsert all existing items using the hash function.

Resizing is expensive, but averaged over many operations, hash tables still provide **O(1)** average performance.

A rule of thumb from the chapter is to resize when the load factor becomes greater than **0.7**.

---

## 6. A Good Hash Function

A good hash function should distribute values as broadly as possible.

The worst case is a hash function that maps every key to the same slot:

```text
key1 ──┐
key2 ──┤
key3 ──┼──→ same slot
key4 ──┘
```

This creates many collisions and can make operations **O(n)**.

The chapter mentions **CityHash** as an example of a hash function used in Google's Abseil library.

---

## 7. Python Hash Tables

You normally do **not** need to implement a hash table yourself.

Programming languages provide built-in hash-table implementations.

In Python, the main example is:

```python
dict
```

You can generally assume average-case **O(1)** performance for dictionary lookup, insertion, and deletion.

---

## 8. Key Takeaways

* A hash table combines a **hash function** with an **array**.
* It stores data as **key → value**.
* Average search, insert, and delete are **O(1)**.
* Worst-case performance is **O(n)**.
* **Collisions** reduce performance.
* A good hash function distributes keys evenly.
* A low **load factor** helps reduce collisions.
* Resizing increases the table size when it becomes too full.
* Python provides hash tables through `dict`.
* You will rarely need to implement a hash table yourself.
