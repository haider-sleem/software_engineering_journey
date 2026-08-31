# Grokking Algorithms (2nd Edition) — Introduction & Chapter 1

> *Aditya Bhargava*

---

## About the Book

**Teaching style:** Visual and practical — illustrated, real-world examples rather than heavy mathematical formulas. Skips non-essential theory to focus on algorithms useful for software engineering. Concepts build gradually without sudden jumps.

**Changes in the 2nd Edition:**
- Code examples updated to Python 3 (from Python 2.7 in the 1st edition)
- New chapters added on trees, covering basic tree concepts and binary search trees
- Expanded explanations of complex topics like NP-completeness and dynamic programming

**Best practices for reading:**
- Type the code yourself instead of just reading it — builds muscle memory
- Spend 2–5 minutes on inline exercises before moving forward

---

## Roadmap Overview

| Area | Covers |
|------|--------|
| **Foundations** | Binary Search, Big O Notation, Arrays, Linked Lists, Recursion |
| **Hash Tables & Graphs** | Key-value pairs, network modeling (BFS, Dijkstra's algorithm) for connectivity problems |

> Note: exact chapter numbers vary slightly by edition — treat the above as a topic map rather than a strict table of contents.

**Problem-Solving Strategies:**

| Strategy | Idea |
|----------|------|
| **Divide and Conquer** | Break a problem into smaller, independent chunks |
| **Dynamic Programming** | Break into overlapping sub-problems and cache intermediate results |
| **Greedy Algorithms** | Find fast, "good-enough" approximate solutions when exact ones are too slow |

---

## Chapter 1: Binary Search vs. Linear Search

### Linear Search (Simple Search)

- Checks every element one by one, from start to finish.
- **Worst case:** the target is at the end (or not in the list) — every item must be checked.
- **Time Complexity:** O(n)
- Example: a list of 1,024 items may take up to **1,024 steps**.

### Binary Search

- Starts at the middle of the list. If the guess is too high, eliminate the top half; if too low, eliminate the bottom half. Repeat until found.
- **Core intuition:** each comparison eliminates roughly half of the remaining search space:
  ```
  n → n/2 → n/4 → n/8 → ...
  ```
  This halving pattern is exactly where O(log n) comes from.
- **Requirement:** the list **must be sorted** — this is non-negotiable.
- **Time Complexity:** O(log n)
- Example: a list of 1,024 items takes at most **10 steps**.

**Implementation basics:**

```
low  → beginning of the remaining search range
high → end of the remaining search range
mid  → middle index of that range

mid = (low + high) // 2
```

`low` and `high` track the boundaries of the part of the list that hasn't been eliminated yet.

### Understanding Logarithms in This Context

- A logarithm is the inverse of an exponent.
- In algorithms, `log` always means **log base 2**.
- It answers: *"How many times do I divide this number by 2 to reach 1?"*

```
2³ = 8      →  log₂ 8 = 3     (max 3 steps for 8 items)
2¹⁰ = 1024  →  log₂ 1024 = 10  (max 10 steps for 1,024 items)
```

**The power of log time:** doubling the data size (e.g., 128 → 256) adds only **one extra step** to Binary Search.

> **Key takeaway:** Binary Search is dramatically faster than Linear Search as data grows — but the data must be sorted first.

---

## Big O Notation

**Definition:** Big O describes how an algorithm's running time grows as the input size (`n`) grows — it is not a measure of speed in seconds.

### Why Not Measure in Seconds?

Hardware changes, but growth rate stays constant. Example: searching 1 billion items with Simple Search (O(n)) at 1ms per item takes **about 11 days**. What matters is *how the time grows*, not the raw number.

### Best Case vs. Worst Case

In this chapter, the book commonly uses Big O to describe the **worst-case** running time. Finding a name instantly in a phone book is the best case — but Simple Search is still rated O(n) because, in the worst case, every entry must be checked. Big O itself isn't limited to worst case, though — best-case and average-case running times can also be expressed with it.

### Constants Are Ignored — But They Still Matter in Practice

Big O ignores constant factors when describing growth rate. Constants can matter for small inputs and real-world performance, but they don't change the asymptotic complexity — an algorithm's Big O classification stays the same regardless of hardware speed or implementation details.

### Common Big O Run Times (Fastest → Slowest)

| Complexity | Example | Behavior |
|------------|---------|----------|
| O(log n) | Binary Search | Extremely fast — doubling data adds only one step |
| O(n) | Simple Search | Grows directly with input size |
| O(n log n) | Efficient sorting algorithms (e.g., Quicksort — average case) | Efficient sorting |
| O(n²) | Selection Sort | Slow — grows with the square of input size |
| O(n!) | Traveling Salesperson Problem | Explodes extremely quickly as `n` grows |