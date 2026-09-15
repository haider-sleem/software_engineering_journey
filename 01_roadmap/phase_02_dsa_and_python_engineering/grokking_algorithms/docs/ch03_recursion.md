# Chapter 3: Recursion

> *Grokking Algorithms — Aditya Bhargava*

---

## Core Idea

Recursion is a technique where a function calls itself. It is useful when it makes a problem **clearer** — not because it is automatically faster than a loop. Recursion is a foundation for later algorithms such as divide and conquer and quicksort.

### Boxes Example

The chapter introduces recursion by comparing two approaches to searching for a key inside nested boxes:

- **Iterative approach:** maintain a manual pile of boxes to search — you manage the pile explicitly.
- **Recursive approach:** when a box is found, call the function again for that box — the call stack manages the remaining work.

Both approaches solve the problem, but recursion can make the solution clearer. This example also directly connects to the call stack: the recursive approach uses the call stack instead of a manual pile.

---

## Recursion vs. Loops

| Aspect | Loops | Recursion |
|--------|-------|-----------|
| Memory | Usually less | Each call uses a stack frame |
| Speed | Can be faster | May have call-stack overhead |
| Clarity | Better for straightforward iteration | Better when the problem naturally breaks into smaller subproblems |

> Use recursion when it improves clarity.

---

## Base Case and Recursive Case

Every recursive function needs two parts:

| Part | Role |
|------|------|
| **Base case** | The simplest case — stops the recursion |
| **Recursive case** | Calls the function again with a smaller or simpler problem |

The recursive case must always move **toward** the base case.

```python
def countdown(i):
    print(i)
    if i <= 1:          # Base case
        return
    else:               # Recursive case
        countdown(i - 1)
```

---

## The Stack

A stack follows **LIFO (Last In, First Out)**.

| Operation | Effect |
|-----------|--------|
| `push` | Add an item to the top |
| `pop` | Remove the top item |

---

## The Call Stack

- Function calls are stored on the call stack.
- When one function calls another, the calling function is **paused** in a partially completed state — its frame stays on the stack.
- When the called function returns, its frame is removed and the previous function resumes.

---

## Recursion and the Call Stack

- Each recursive call gets its own **stack frame** with its own **independent local variables**.
- When the base case returns, the pending calls resume in **reverse order** up the stack.

```
fact(3)
  ↓
fact(2)
  ↓
fact(1)  ← base case

Returns:
fact(1) → 1
fact(2) → 2 × 1 = 2
fact(3) → 3 × 2 = 6
```

---

## Recursion and Memory

- Each recursive call adds a frame to the call stack and requires memory.
- Deep recursion creates a large stack.
- A recursive function that never reaches its base case keeps adding calls until the stack is exhausted.
- In Python, excessive recursion results in a **`RecursionError`**.

### Iterative vs. Recursive: Who Manages the Work?

| Approach | How remaining work is tracked |
|----------|------------------------------|
| Iterative | A manual pile (explicit data structure) |
| Recursive | The call stack — unfinished calls are stored automatically |

---

## Tail Recursion

Mentioned as an advanced technique — outside the scope of this chapter. Support varies between programming languages.

---

## Core Principle

> Use recursion when it makes the solution clearer. Always ensure recursive calls move toward a base case.