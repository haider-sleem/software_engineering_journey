# Chapter 9: Queues — Keeping Information in the Same Order as It Arrives

## Queue as an Abstract Data Type

A **queue** is a container where elements are inserted and removed from specific ends.

The core rule is **FIFO (First In, First Out)**:

> The element that has been in the queue the longest is removed first.

Example:

```text
enqueue(1)
enqueue(7)
enqueue(3)

Front → 1 → 7 → 3 ← Rear

dequeue() → 1
dequeue() → 7
```

A queue processes elements in the same order in which they were inserted.

---

## Queue Operations

A queue has two core operations:

* **`enqueue(x)`** — insert `x` at the rear.
* **`dequeue()`** — remove and return the oldest element from the front.

```text
             enqueue →
Front                    Rear
  ↓                        ↓
[ 1 ] → [ 7 ] → [ 3 ]

  ↑
dequeue
```

### Additional Operations

- **`peek()` / `front()`** — inspect the front element without removing it.
- **Iteration** — process elements in queue order without modifying the queue.

Unlike a stack:

* Stack: insertion and removal happen at the **same end**.
* Queue: insertion happens at the **rear**, removal happens at the **front**.

A queue therefore needs references to both its **front** and **rear**.

---

## Queues in Practice

Queues are useful when work must be processed in arrival order.

Examples:

* Bug/task processing
* Email processing
* Request processing
* Breadth-first search (BFS)

A queue can preserve chronological order implicitly, without storing a separate timestamp for every item.

---

## Queue as a Data Structure

Possible implementations include:

* Static array
* Dynamic array
* Linked list
* Stack(s)

Using stacks is possible, but implementing a queue efficiently requires two stacks.

The practical choices discussed in the chapter are mainly:

1. **Linked list**
2. **Static array**

Dynamic arrays are possible, but their complexity and performance costs make them less attractive for this use case.

---

## Linked List Implementation

A queue can be implemented efficiently with a linked list.

For a **doubly linked list**:

```text
Front → [4] ↔ [6] ↔ [3] ↔ [7] ← Rear
```

* `enqueue()` adds at the rear.
* `dequeue()` removes from the front.
* Both operations are **O(1)**.

A **singly linked list** can also work if it maintains a reference to the tail.

### Complexity

| Operation    | Linked List |
| ------------ | ----------: |
| `enqueue()`  |        O(1) |
| `dequeue()`  |        O(1) |
| Dynamic size |         Yes |

The queue can grow and shrink dynamically without array resizing.

---

## Static Array Implementation

A static array gives the queue a fixed capacity.

Unlike a stack, a queue creates a problem when elements are dequeued:

```text
Before:
[ A ][ B ][ C ][ D ][   ][   ]

dequeue A, B:

[   ][   ][ C ][ D ][   ][   ]
```

The empty space at the beginning cannot simply be ignored forever because the rear eventually reaches the end of the array.

### Linear Queue

One simple solution is to stop when the rear reaches the end.

This wastes space that was freed by previous `dequeue()` operations.

Therefore, a simple linear queue is generally impractical.

---

## Circular Queue

A **circular queue** reuses the empty space at the beginning of the array.

Conceptually:

```text
[0] [1] [2] [3] [4] [5] [6] [7]
 ↑                               ↓
 └────────── wraps around ───────┘
```

When the rear reaches the last index, it wraps back to index `0`.

The same applies to the front.

### Virtual Indexes

The chapter describes indexes beyond the physical array as **virtual indexes**.

For an array of size `8`:

```text
Virtual index:  8  → physical index 0
Virtual index:  9  → physical index 1
Virtual index: 10  → physical index 2
```

The **modulo operator** maps virtual indexes to physical indexes:

```python
physical_index = virtual_index % max_size
```

For example:

```text
8 % 8  = 0
9 % 8  = 1
10 % 8 = 2
```

---

## Front, Rear, and Size

The array-based implementation maintains:

* `front` — index of the next element to be dequeued.
* `rear` — index of the next array cell where an element can be enqueued.
* `size` — number of elements currently stored.
* `max_size` — queue capacity.

Tracking `size` makes it easy to determine whether the queue is:

* Empty → `size == 0`
* Full → `size == max_size`
* Partially full → otherwise

This also avoids relying only on the positions of `front` and `rear`, because they can point to the same index when the queue is either empty or full.

---

## Array-Based Complexity

| Implementation |                 `enqueue()` |                 `dequeue()` | Dynamic Size |
| -------------- | --------------------------: | --------------------------: | ------------ |
| Static array   |                        O(1) |                        O(1) | No           |
| Dynamic array  | O(n) worst / O(1) amortized | O(n) worst / O(1) amortized | Yes          |
| Linked list    |                        O(1) |                        O(1) | Yes          |

---

## Array vs. Linked List in Practice

Theoretical complexity is not the only consideration.

Arrays can have practical advantages:

* **Memory efficiency** — less overhead per element.
* **Memory locality** — elements are stored together, which can improve processor caching.
* **Performance** — array operations are often faster than equivalent linked-list operations.

Therefore:

* Choose a **linked list** when flexibility in queue size and simpler implementation are important.
* Choose an **array** when the maximum capacity is known and memory locality/performance are valuable.

The choice depends on the requirements, not Big-O alone.

---

## Key Mental Model

Think of a queue as a real-world line:

```text
New person
    ↓
Rear → [A] → [B] → [C] → Front
                         ↓
                    Served first
```

**FIFO = First In, First Out**

The oldest item leaves first.

---

## Recap

* A queue follows **FIFO**.
* `enqueue()` adds at the **rear**.
* `dequeue()` removes from the **front**.
* A queue needs both **front** and **rear** references.
* A linked-list queue can perform both operations in **O(1)**.
* A simple linear array queue wastes space after dequeues.
* A **circular queue** reuses that space by wrapping indexes around.
* The modulo operator maps virtual indexes to physical indexes.
* Arrays can provide better memory efficiency, locality, and practical performance.
* Big-O is important, but implementation choice also depends on practical requirements.
