# Chapter 8: Stacks — Piling Up Data Before Processing It

## What Is a Stack?

A **stack** is a data structure that follows the **LIFO** rule:

> **Last In, First Out**

The last element added to the stack is the first one removed.

Example:

```text
Top
 ↓
[ 3 ]  ← last added
[ 2 ]
[ 1 ]  ← first added
````

If we call `pop()`, `3` is removed first.

---

## Stack ADT

The Stack ADT provides a restricted interface.

### Main Operations

| Operation    | Meaning                                    |
| ------------ | ------------------------------------------ |
| `push(x)`    | Add `x` to the top                         |
| `pop()`      | Remove and return the top element          |
| `peek()`     | Return the top element without removing it |
| `is_empty()` | Check whether the stack is empty           |

The essential operations of the stack are **push** and **pop**.

`peek` is commonly provided as a read-only operation.

---

## Why Use a Stack?

Stacks are useful when data must be processed in reverse order of insertion.

Common examples include:

* Undo operations
* Redo operations
* Function calls and the **call stack**
* Processing expressions
* Backtracking
* Parentheses matching

---

## Stack Implementation Options

A stack can be implemented using:

1. **Static Array**
2. **Dynamic Array**
3. **Singly Linked List**

The Stack ADT stays the same; only the underlying implementation changes.

```text
Stack ADT
   │
   ├── Static Array
   ├── Dynamic Array
   └── Singly Linked List
```

---

## Static Array Implementation

A static array can store the stack elements.

The **top** can be represented by an index.

```text
[ 4 ][ -1 ][ 0 ][ 2 ][  ]
                    ↑
                   Top
```

### Advantages

* `push` can be O(1)
* `pop` can be O(1)
* Constant additional memory for the operations

### Main Problem

The capacity is fixed.

If the array becomes full, another element cannot be pushed.

Therefore, static arrays are useful when the maximum stack size is known in advance.

---

## Dynamic Array Implementation

A dynamic array removes the fixed-capacity limitation.

When the underlying array becomes full, it can be resized.

However, resizing requires allocating a larger array and copying elements.

Therefore:

* `push` — O(n) worst case
* `pop` — O(n) worst case
* `n` pushes — O(n) amortized
* `n` pops — O(n) amortized

Dynamic arrays can also require additional memory during resizing.

For very large stacks, the cost of allocating large contiguous memory can become a concern.

---

## Linked List Implementation

A stack works especially well with a **Singly Linked List (SLL)**.

We only need to modify one side of the list: the front.

```text
Top
 ↓
[ 2 ] → [ 0 ] → [ -1 ] → [ 4 ] → None
```

`push` inserts at the front.

`pop` deletes from the front.

Both operations are **O(1)**.

There is no need for a **Doubly Linked List** because we never need to move backward through the elements.

---

## Stack as a Wrapper

The Stack class can use a linked list internally.

```python
class Stack:
    def __init__(self):
        self._data = SinglyLinkedList()
```

The Stack exposes only the operations that belong to the Stack ADT.

The underlying linked list remains an implementation detail.

This is another example of **composition** and **encapsulation**.

---

## Push

`push(x)` adds an element to the top.

With a linked-list implementation:

```python
def push(self, value):
    self._data.insert_in_front(value)
```

The stack delegates the actual insertion to the underlying linked list.

### Complexity

**O(1)**

---

## Pop

`pop()` removes and returns the element at the top.

For an empty stack, `pop()` should raise an appropriate exception.

Example:

```python
def pop(self):
    if self.is_empty():
        raise ValueError("Cannot pop from an empty stack")

    return self._data.delete_from_front()
```

### Complexity

**O(1)**

---

## Peek

`peek()` returns the top element without modifying the stack.

It should:

1. Check whether the stack is empty.
2. Access the top element through an appropriate interface.
3. Avoid exposing the linked list's private implementation details.

The chapter emphasizes that directly accessing the linked list's private `_head` is not a good design.

---

## Stack Operations Example

Start with an empty stack:

```text
empty
```

### `push(4)`

```text
Top
 ↓
[4]
```

### `push(1)`

```text
Top
 ↓
[1]
[4]
```

### `push(6)`

```text
Top
 ↓
[6]
[1]
[4]
```

### `pop()`

`6` is removed:

```text
Top
 ↓
[1]
[4]
```

This demonstrates **LIFO**.

---

## Complexity Comparison

| Implementation     |            Push |             Pop | Main Tradeoff            |
| ------------------ | --------------: | --------------: | ------------------------ |
| Static Array       |            O(1) |            O(1) | Fixed capacity           |
| Dynamic Array      | O(n) worst case; O(1) amortized | O(n) worst case; O(1) amortized | Resizing occurs occasionally; flexible capacity |
| Singly Linked List |            O(1) |            O(1) | Extra memory per element |

For linked lists, each node requires additional memory for its link.

---

## Performance vs. Asymptotic Analysis

The chapter compares linked-list and Python-list implementations using profiling.

The results show that Python's built-in list can perform stack operations much faster in practice.

This does **not** invalidate Big-O analysis.

Important factors include:

* Python's `list` is highly optimized.
* Built-in operations are implemented efficiently.
* Linked lists require creating and destroying Node objects.
* Both implementations can have the same amortized asymptotic behavior for many operations.

**Big-O describes growth behavior; profiling measures actual implementation performance.**

---

## Key Idea

A Stack is defined by its **LIFO behavior**, not by how it is implemented.

```text
             Stack ADT
                 │
        ┌────────┼────────┐
        ↓        ↓        ↓
     Array     Dynamic    SLL
     Array
```

The same Stack interface can be implemented using different data structures, each with different tradeoffs.

---

## Stack Applications

### Call Stack

Every function call is pushed onto the call stack. When a function returns, its frame is popped.

```text
main()
  ↓ calls
process_order()
  ↓ calls
calculate_total()   ← currently executing
```

When `calculate_total()` returns → popped → `process_order()` resumes.

Recursive functions use the call stack in exactly this way. Deep recursion can exhaust the stack → **stack overflow**.

---

### Undo / Redo

Every user action is pushed onto an **undo stack**.

```text
Undo stack:
[ add_product ]
[ update_price ]
[ delete_item ]   ← last action
```

When the user presses Undo → `pop()` from undo stack → push onto redo stack.

When the user presses Redo → `pop()` from redo stack → push back onto undo stack.

---

### Postfix Expression Evaluation

Postfix notation eliminates the need for parentheses:

```text
Infix:    3 + 4 × 2
Postfix:  3 4 2 × +
```

**Algorithm:**
- Scan left to right.
- If operand → `push`.
- If operator → `pop` two operands, apply the operator, `push` the result.

```text
3 4 2 × +

push 3   → [3]
push 4   → [3, 4]
push 2   → [3, 4, 2]
×: pop 2 and 4, push 8   → [3, 8]
+: pop 8 and 3, push 11  → [11]

Result: 11
```

---

### Backtracking / DFS

A stack can replace recursion in Depth-First Search (DFS).

```text
push starting node
while stack is not empty:
    node = pop()
    visit node
    push unvisited neighbors
```

The stack preserves the path back — the same role the call stack plays in recursive DFS.

---

## Key Takeaways

* A **Stack** follows **LIFO: Last In, First Out**.
* The main operations are `push` and `pop`.
* `peek` reads the top element without removing it.
* A stack can be implemented using arrays or linked lists.
* A **Singly Linked List** is particularly suitable because insertion and deletion at the front are O(1).
* A Doubly Linked List is unnecessary for a basic stack.
* Static arrays have fixed capacity.
* Dynamic arrays provide flexibility but may require resizing.
* Amortized analysis is important when evaluating dynamic-array stacks.
* Big-O and profiling answer different questions.
* The **ADT defines behavior; the underlying data structure determines implementation and tradeoffs.**
