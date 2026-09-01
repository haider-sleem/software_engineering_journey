# Chapter 4: Big-O Notation — A Framework for Measuring Algorithm Efficiency

> *Grokking Data Structures — Marcello La Rocca*

---

## The Core Problem: How Do We Choose the Best Option?

When comparing algorithms (like Linear Search vs. Binary Search), we need a consistent, objective way to measure performance (time and memory) — we cannot rely on specific examples or coincidences.

Two main approaches exist: **Profiling** and **Asymptotic Analysis**.

---

## Profiling (Empirical Measurement)

Running actual code with various inputs and measuring the exact time and memory consumed. In Python: `cProfile`.

| Pros | Cons |
|------|------|
| Tools are ready to use | **Hardware/environment dependent** — results change with OS, processor, compiler |
| Excellent for finding real bottlenecks line-by-line | **Implementation dependent** — profiling measures the performance of a *specific implementation* under specific hardware/software/input conditions, and can reveal a bad implementation or an unsuitable data structure choice |
| | **Finite inputs** — limited to sizes your machine can handle; hard to generalize to distributed systems or massive data |

---

## Asymptotic Analysis (Theoretical Measurement)

Reasoning about an algorithm using abstract mathematics — a formula describing how running time or memory grows as input size approaches infinity.

| Pros | Cons |
|------|------|
| **Universal** — independent of language, hardware, or implementation | Requires mathematics (already worked out for standard data structures) |
| **Scalable** — helps us reason about how performance scales as input size grows, not exact runtime | Theoretical — not a tool you run directly on your code |

---

## Which One Should I Use?

Both are essential, at different stages:

| Analysis | When | Purpose |
|----------|------|---------|
| **Asymptotic Analysis** | Design phase — before writing code | Choose the right data structure and algorithm on paper |
| **Profiling** | Implementation phase — after writing code | Find real bottlenecks, fix bad implementations, catch a wrong initial choice |

---

## What Is Big-O Notation?

Big-O measures how an algorithm's time or memory grows as input size (`n`) gets much larger. We don't care about small delays or exact seconds — only the overall shape of the growth curve as `n` becomes very large.

> **Big-O focuses on the *rate* at which a resource grows as `n` increases — not the exact runtime.** This is the foundation the entire chapter builds on.

### Common Growth Rates (Fastest → Slowest)

| Notation | Name | Behavior |
|----------|------|----------|
| O(1) | Constant | Speed never changes regardless of input size |
| O(log n) | Logarithmic | Extremely fast — e.g., Binary Search |
| O(n) | Linear | Grows steadily and proportionally with input |
| O(n log n) | Linearithmic | Slightly slower than linear, excellent for sorting large data — e.g., Mergesort, Heapsort |
| O(n²) | Quadratic | Very slow for large data — e.g., Selection Sort |
| O(2ⁿ) | Exponential | Extremely slow — even n = 60 can take an impractically long time |

### Rules of Big-O Math

- **Drop constants:** `O(5n)` → `O(n)`
- **Drop smaller terms:** keep only the fastest-growing term — `O(3n + 5)` → `O(n)`
- **Keep multiplied variables together:** `O(n) × O(log n)` → `O(n log n)`

---

## Types of Performance Analysis

| Type | Measures | Use Case |
|------|----------|----------|
| **Worst-Case** | The input (for a given size `n`) that makes the algorithm use the most time or memory | Guarantees safety — critical for systems where failure isn't an option |
| **Average-Case** | Expected performance across typical inputs | Realistic picture, but no guarantee for a single run |
| **Amortized** | Overall cost across a sequence of operations | For structures that are fast (O(1)) almost always but occasionally hit a slow operation (O(n)) — the heavy cost is "spread out" to show the batch remains efficient overall. Amortized analysis does **not** guarantee every single operation is fast — it guarantees the cost of a large sequence of operations combined. |

---

## Measured Resources

**Running Time — T(n):** how much time the code needs to finish.

**Space/Memory — S(n):** the memory or resources used by the algorithm or data structure. The chapter uses "space" as a general term rather than distinguishing RAM, disk, or cache — and focuses specifically on **extra space**: memory needed beyond the original input data.

```
Creating a second array to hold results  →  S(n) = O(n)  (extra space grows with n)
Modifying the data in place (e.g., reversing an array using a temp variable)  →  S(n) = O(1)
```

---

## Asymptotic Analysis in Practice

**How to analyze:** examine code line by line, determine the Big-O of each instruction, and combine them into a final formula.

**Main goal — Upper Bound:** the chapter's analysis focuses on finding the **Upper Bound** for running time and extra space — a formula describing the worst-case asymptotic growth. This is a classification of growth behavior, not a literal guarantee of the exact maximum runtime.

**Lower Bound:** proving the absolute fastest possible time is mathematically complex and usually unnecessary for standard engineering work.

---

## Linear Search Analysis

| Property | Value |
|----------|-------|
| Worst/Average case T(n) | O(n) — may scan up to n elements |
| Best case | O(1) — target is the first element |
| Space S(n) | O(1) — just a loop index |
| Array requirement | Works on sorted **and** unsorted arrays |

---

## Binary Search Analysis

| Property | Value |
|----------|-------|
| How it works | Compares target to middle element, halves the search space each step |
| Time T(n) | O(log n) — repeatedly dividing n by 2 takes log₂(n) steps |
| Space S(n) | O(1) |
| Array requirement | **Sorted arrays only** |

---

## Array Operations: Sorted vs. Unsorted

> Note: the complexities below reflect the specific implementations and assumptions discussed in the book (e.g., unsorted deletion swaps in the last element rather than preserving order) — not a universal rule for every possible array implementation. Choice of algorithm/implementation changes these trade-offs.

| Operation | Unsorted | Sorted |
|-----------|----------|--------|
| **Insert** | O(1) — add at the end, no shifting | O(n) — shifting required to maintain order |
| **Delete** | O(n) overall — O(n) to find, O(1) to swap the last element into the gap | O(n) — O(log n) to find, but O(n) to shift elements back |
| **Traverse** | O(n) | O(n) — must visit every element |

---

## Big-O Complexity Hierarchy

| Notation | Name | Practical Note |
|----------|------|----------------|
| O(1) | Constant | Independent of `n` (e.g., variable assignment) |
| O(log n) | Logarithmic | Extremely efficient, very slow growth (e.g., Binary Search) |
| O(n) | Linear | Grows proportionally with `n` (e.g., Linear Search) |
| O(n log n) | Linearithmic | Standard for efficient sorting and priority queues |
| O(n²) | Quadratic | Grows quickly and can become impractical as `n` gets large — e.g., nested loops |
| O(2ⁿ) | Exponential | Grows extremely rapidly and becomes impractical even for relatively small `n` — e.g., generating all subsets |

---

## Fundamental Concepts

**RAM Model:** short for **Random-Access Machine** (not Random-Access Memory) — a theoretical computer model where elementary operations take constant time O(1). It assumes a single-core processor and uniform random access to memory, where accessing any memory location takes O(1). This model is the foundation the rest of the algorithm analysis builds on.

**Hidden Costs:** loop control variables, condition checks, and method calls inside loops all add operations that must be accounted for in performance analysis.