# Chapter 6: Linked Lists — A Flexible Dynamic Collection

> *Grokking Data Structures — Marcello La Rocca*

---

## Linked Lists vs. Arrays

A **linked list** is a sequence of **nodes**. Each node stores:
- the element's data
- a reference to the next node

Unlike arrays, nodes do not need to be stored contiguously in memory. Nodes can be allocated and removed as needed, without reallocating and moving the entire collection as arrays may require. The tradeoff is that linked lists do not support direct access by index — to reach the `n`th element, traversal from the head is required.

**Allocation advantage:** removing a node from a linked list does not leave an empty slot that must later be compacted, unlike an array where deletion may require shifting elements.

| Operation | Array | Linked List |
|-----------|-------|------------|
| Access by index | O(1) | O(n) |
| Search | O(n) | O(n) |
| Insert at beginning | O(n) | O(1) |
| Insert at end | O(1)* | O(n) in SLL |
| Delete by value | O(n) | O(n) |
| Resize | Costly | Easy |
| Extra memory per element | Low | Higher (links) |

> *Array insert at end is O(1) amortized for dynamic arrays.

---

## Singly Linked List (SLL)

One link per node, pointing to the next node.

- **Head** = first node
- **Tail** = last node; its `next` is `None`
- Traversal is only possible from head toward tail

```
Head
 ↓
[Data | Next] → [Data | Next] → [Data | None]
                                      ↑
                                     Tail
```

### Two-Tier Structure

| Layer | Responsibility |
|-------|---------------|
| **Linked-list wrapper** | Maintains `head`, provides the public API |
| **Nodes** | Store data and the link to the next node |

The `Node` implementation should remain an internal detail — not exposed to clients.

```python
class Node:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node
```

An empty list starts with `self._head = None`.

---

## Operations

### Insert at End — O(n)

Traverse to the tail, then update its `next` link to point to the new node. In the book's implementation, this is done via `Node.append()`, which updates the current node's `next` link — not Python's `list.append()`:

```python
while current.next() is not None:
    current = current.next()

current.append(Node(data))  # updates current node's next link
```

The SLL stores no `_tail` reference, so traversal is required. Inserting `n` elements one by one into an empty SLL can therefore cost **O(n²)** total.

### Insert at Front — O(1)

```python
old_head = self._head
self._head = Node(data, old_head)
```

The new node becomes the head and points to the previous head. This is one of the major strengths of linked lists.

### Search — O(n)

```python
current = self._head

while current is not None:
    if current.data() == target:
        return current
    current = current.next()

return None
```

`_search()` is kept internal — exposing `Node` objects to clients would expose the internal implementation and allow them to corrupt the list's links. Keeping nodes private allows the implementation to change later without breaking clients.

### Delete by Value — O(n)

Deleting a node requires bypassing it. For `A → B → C`, deleting `B` means changing `A`'s link to point to `C`.

An SLL needs access to the **predecessor** of the node being deleted — in an SLL, a direct reference to the target node does not let us reach its predecessor. Two references are maintained during traversal:

```python
# previous.next → current.next
# In the book's implementation:
previous.append(current.next())  # updates previous node's next link
```

**Edge cases:**
- **Delete head:** no predecessor → `self._head = current.next()`
- **Delete tail:** predecessor's `next` becomes `None`

Even with a direct reference to the target node, the predecessor must still be found — so deletion is **O(n)**.

### Delete from Front — O(1)

Updating only the head is a special case, useful when implementing a **Stack**.

---

## Encapsulation and Least Authority

```
Client → Linked List API → Internal Nodes
```

Not:

```
Client → Internal Nodes
```

Giving clients a mutable `Node` reference could allow them to corrupt the list's structure.

---

## Sorted Linked Lists

Insertion must find the correct position to preserve order:

1. Traverse the list
2. Find the insertion point
3. Insert between two nodes
4. Update links

**Sorted insertion: O(n)**

### Why Binary Search Doesn't Help

Binary search requires O(1) access to the middle element. A linked list requires traversal to reach the middle, so search remains **O(n)** — no O(log n) advantage. The benefit of a sorted linked list is maintaining order or efficient access to the smallest element at the head.

---

## Doubly Linked List (DLL)

Each node has two links: `next` (successor) and `prev` (predecessor).

```
None ← [Prev|Data|Next] ⇄ [Prev|Data|Next] ⇄ [Prev|Data|Next] → None
           ↑                                          ↑
          Head                                       Tail
```

The list maintains both `_head` and `_tail`:

```python
self._head = None
self._tail = None
```

Storing `_tail` enables O(1) access to the last node.

```python
self._data = data
self._next = None
self._prev = None
```

| Advantage | Disadvantage |
|-----------|-------------|
| Bidirectional traversal | Extra memory per node for `prev` |
| O(1) insert/delete at both ends (with `_head`/`_tail`) | Every structural change may update two links |
| Node knows its own predecessor | More complex implementation |

**Space overhead:** both SLL and DLL are O(n) total storage, but a DLL has a larger constant — two links per node instead of one.

### Insert at Front — O(1)

The old head must point backward to the new head. For an empty list, both `_head` and `_tail` point to the new node.

### Insert at End — O(1)

Because `_tail` is stored directly, no traversal is needed. Major improvement over SLL.

### Insert in Middle

- Finding the position: **O(n)**
- Actual insertion (once position is known): **O(1)** — no shifting required
- Overall: **O(n)**

### Delete

| Situation | Complexity |
|-----------|-----------|
| Delete by value | O(n) — search first, then O(1) deletion |
| Delete given node reference | O(1) — `prev` and `next` are both accessible |

In a DLL, if we already have a reference to the node, deletion is O(1) because the node can reach its own predecessor via `prev`. When deleting by value, we first search (O(n)), then delete (O(1)), for an overall O(n).

**Edge cases:** deleting the head, the tail, the only node, or a middle node.

### Search — O(n)

The `prev` links do not improve ordinary search. Forward and backward traversal are both O(n).

---

## Concatenating Lists

Two lists can be joined by connecting the tail of the first to the head of the second.

- **DLL with `_tail` reference:** O(1)
- **SLL (book's implementation, no `_tail`):** O(n) — must traverse to find the tail first

With arrays, concatenation requires allocating a new array and copying all elements.

---

## Circular Linked Lists

The tail points back to the head — no true end exists.

```
      ┌──────────────────────────┐
      ↓                          │
Head → A → B → C → D ────────────┘
```

Can be singly or doubly linked.

**Typical applications:** cyclic processes, slideshows/carousels, repeated resource allocation, server rotation, round-robin task scheduling.

### Circular SLL vs. Circular DLL

| Type | When to Use |
|------|------------|
| Circular SLL | Forward-only traversal needed |
| Circular DLL | Bidirectional traversal needed |

In a circular DLL, `head.prev` can serve as the tail reference — a separate `_tail` is not strictly required.

### Traversal Danger

No `None` at the end means infinite traversal is possible. A stopping mechanism is required:
- Track the starting node
- Use a step-by-step traversal mechanism, such as an iterator-like interface

---

## Complexity Summary

| Operation | SLL | DLL |
|-----------|-----|-----|
| Access by position | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert at front | O(1) | O(1) |
| Insert at back | O(n) | O(1) |
| Insert given node reference | O(1) | O(1) |
| Delete by value | O(n) | O(n) |
| Delete given node reference | O(n) — must find predecessor | O(1) |
| Traverse forward | O(n) | O(n) |
| Traverse backward | Not supported | O(n) |
| Concatenate | O(n) | O(1) |

---

## Key Takeaways

- Linked lists trade **direct access** for **flexible node-by-node allocation and efficient structural changes**.
- Nodes are allocated as needed; removing a node leaves no empty slot to compact.
- SLL nodes store data + `next`; DLL nodes store data + `next` + `prev`.
- Both SLL and DLL are O(n) in total space, but DLL has a larger constant per node.
- SLLs are especially efficient at the **head**.
- DLLs are useful when bidirectional traversal or O(1) tail operations are needed — and when a node reference is available, deletion is O(1).
- Both provide **O(n) access and search**.
- Circular linked lists suit **cyclic or repeatedly traversed data**.

```
Arrays:        Fast direct access    → Less flexible resizing
Linked Lists:  Flexible allocation   → No O(1) indexed access
```