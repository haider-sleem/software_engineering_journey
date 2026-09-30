# Chapter 7: Abstract Data Types — Designing the Simplest Container: The Bag

> *Grokking Data Structures — Marcello La Rocca*

---

## 1. Abstract Data Types vs. Data Structures

### Abstract Data Type (ADT)

An **ADT** describes **what** operations are available, what they should do, and what they should guarantee — without specifying how they are implemented.

### Data Structure

A **data structure** describes **how** data is represented and how operations are implemented.

**Simple mental model:**

> **ADT = What**
> **Data Structure = How**

The same ADT can be implemented using different data structures.

| | ADT | Data Structure |
|---|---|---|
| Describes | **What** operations are available | **How** data is stored and operations work |
| Specifies | Behavior and guarantees | Concrete memory layout and algorithms |
| Example | Sequence with indexed access | Array in contiguous memory |
| Client sees | The interface | Hidden |

### Example: Array

An array can be viewed at different levels:

* **Array as an ADT:** A sequence of elements with positions (indexes).
* **Array as a data structure:** Adds implementation requirements such as constant-time indexed access.
* **Array implementation:** Specifies concrete memory representation and language-level details.

---

## 2. The Light Switch Analogy

A light switch demonstrates the difference between an abstraction and its implementation.

The abstraction defines:

* `turn on`
* `turn off`

The physical implementation can vary:

* Toggle switch
* Two buttons
* Single push button
* Digital interface

The behavior stays the same even though the implementation changes.

> **ADT hides implementation details from the client.**

---

## 3. Containers

A **container** is a concept (used both at the ADT level and the data-structure level) whose main purpose is to hold a collection of elements.

### What Containers Typically Provide

Containers generally:

* Hold multiple elements.
* May contain elements of the same or different types.
* May preserve order or ignore order.
* Support basic operations such as:

  * Insert
  * Delete
  * Access
  * Modify
  * Search
* Allow their elements to be traversed.

In many implementations, traversal is exposed through an **iterator**, allowing sequential access such as:

```python
for item in container:
    ...
```

### What Isn't a Container?

Not every data structure is considered a container.

For example:

* **Graphs** primarily model relationships and connections.
* **k-d trees** primarily organize multidimensional data for efficient proximity queries.

Their main purpose goes beyond simply managing a collection of elements.

---

## 4. The Bag

A **bag** is the simplest possible container.

Its main idea is:

> Store elements without caring about their insertion order.

### Bag Properties

A bag:

* Stores a collection of elements.
* Does **not** guarantee an order.
* Allows duplicate elements.
* Does not require indexes.
* Provides only a very small interface.

### Bag Interface

The ADT defines the **minimum required** operations:

```text
insert(x)
iterate()
```

> Additional operations can be added in specific implementations, but they are not part of the core Bag ADT.

#### `insert(x)`

Adds one element to the bag.

* The insertion order is not important.
* The implementation does not need to preserve insertion order.

#### `iterate()`

Allows the client to go through all elements.

* The iteration order is **not guaranteed**.
* The order may even change between two iterations.

### Important

A bag does **not** provide:

* `search`
* `remove`

These operations are normally expected from containers, so the bag is a very restricted or borderline container.

---

## 5. Duplicates

A bag allows duplicate elements.

Example:

```text
[1, 1, 2, 3, 3, 3]
```

There is no uniqueness constraint unless the application using the bag imposes one.

---

## 6. Why Use a Bag?

A bag is useful when we only care about information that does **not depend on element order**.

For example, a bag can be used to collect daily order statistics.

If the bag contains:

```text
1 1 1 2 2 3 2 3 4 5 3 4
```

Another iteration might produce:

```text
1 1 3 3 1 2 2 3 4 3 4 5
```

The order is different, but operations such as:

* Total number of elements
* Sum
* Statistics by type

can still produce the same result because they are **order-independent** — the computation depends only on which elements are present, not the sequence in which they appear.

> **Use a bag when order does not matter.**

---

## 7. Bag Implementation

The ADT defines **what** the bag does.

Only after defining the ADT do we choose a concrete data structure to implement it.

A bag can be implemented using a **linked list**.

Because insertion order does not matter, new elements can be inserted at the beginning of a singly linked list.

```python
def insert(self, value):
    self._data.insert_in_front(value)
```

`insert_in_front()` is O(1) — no traversal needed.
Inserting at the back would require O(n) traversal (SLL has no tail reference).

### Traversal

The bag can expose its elements through an iterator or a traversal method.

For example:

```python
def traverse(self):
    return self._data.traverse()
```

The client must not assume any particular iteration order.

---

## 8. ADT Design Principle

When defining an ADT, don't only specify:

* Method names
* Arguments
* Return types

Also specify:

* Expected behavior
* Side effects
* Changes to internal state
* What the operation guarantees
* What it does **not** guarantee

This makes the interface a precise contract between the ADT and its client.

---

## 9. Key Takeaways

* **ADT = what**, **Data Structure = how**.
* The same ADT can have multiple implementations.
* A **container** holds and manages a collection of elements.
* Containers typically support insertion, deletion, access, modification, search, and traversal.
* A **bag** is the simplest container.
* A bag does not care about insertion order.
* A bag allows duplicates.
* `insert(x)` adds an element.
* `iterate()` traverses all elements without guaranteeing order.
* Bags do not provide search or removal operations.
* A bag can be implemented using a linked list.
* The ADT should define behavior and guarantees, not just method signatures.
* Clients should depend on the **ADT interface**, not the underlying implementation.
