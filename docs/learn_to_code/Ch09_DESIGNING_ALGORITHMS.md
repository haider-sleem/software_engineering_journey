## Chapter 9: Designing Algorithms with Complete Search

---

### 1. What is Complete Search?

**Complete Search** (also called **Brute Force**) means:

> Try every possible candidate solution, check each one, and keep the best valid result.

The term "Complete Search" is preferred over "Brute Force" because the algorithm design itself is often intelligent. The computer only performs the exhaustive checking.

---

### 2. Engineering Mindset Before Writing Code

Think in this order:

```
Problem → Idea → Algorithm → Code
```

Do not reinvent a solution for every problem. First identify the algorithmic pattern.

The hardest part is often **identifying the correct search space**, not writing the loop.

A candidate solution is any possible answer that could satisfy the problem.

---

### 3. When to Use Complete Search

- When no simple rule is guaranteed to work
- When the search space is small enough to check all possibilities
- As a starting point to understand a problem before optimizing

Do not trust an intuitive rule until you test it against counterexamples.

---

### 4. Common Complete Search Pattern

A typical Complete Search solution follows this structure:

1. Write a function that evaluates **one candidate solution**
2. Try every candidate solution
3. Keep the best result found so far (the "score to beat")

```python
best = 0
for candidate in all_candidates():
    score = evaluate(candidate)
    if score > best:
        best = score
```

---

### 5. Using `set` in Complete Search

`set` is ideal when duplicate counting must be avoided automatically.

Use `set` when you need:
- Unique values
- Fast membership checking
- Automatic duplicate removal

---

### 6. Complete Search Limitations

Small input size does **not** always mean a Complete Search solution is fast.

The real bottleneck is often the **number of operations**, especially with many nested loops.

Always analyze both:
- Input size (`N`)
- Number of operations performed by the algorithm

#### Estimating Performance

| Loop Structure | Time Complexity |
|---|---|
| 1 loop | O(n) |
| 2 nested loops | O(n²) |
| 3 nested loops | O(n³) |

Always analyze using the **general case (`n`)**, not only small examples.

If estimated operations greatly exceed the time limit, a more efficient algorithm is required.

---

### 7. Correct vs Efficient

An algorithm can be **correct** but still fail because it is too slow.

Always compare the estimated number of operations with the problem's time limit.

For large inputs (`n = 1000`), an **O(n³)** solution becomes impractical.

**Before optimizing**, first identify **what is being recomputed unnecessarily**.

---

### 8. Search Space Pruning

- Choosing the correct **search space** is often harder than writing the algorithm
- Do not assume the optimal solution must come directly from the input values
- Use problem constraints to safely reduce the search space
- If one candidate is always worse than another, it can be safely ignored (pruning)

A Complete Search is practical when the number of candidates is small.

---

### 9. Linear Search vs Binary Search

| Search Type | How It Works | Time | Requirement |
|---|---|---|---|
| **Linear Search** | Checks elements one by one | O(n) | None |
| **Binary Search** | Repeatedly halves the search space | O(log n) | Sorted data |

Binary Search is much faster but requires the data to be **sorted**.

Sorting is often done to enable faster searching algorithms like Binary Search.

---

### 10. The `bisect` Module

`bisect` provides fast binary search functions for sorted lists.

#### Key Functions

| Function | What It Does |
|---|---|
| `bisect_left(lst, x)` | Returns index of first element **>= x** |
| `bisect_right(lst, x)` | Returns index of first element **> x** |

If `x` is not in the list, both return the same insertion index.

```python
from bisect import bisect_left, bisect_right

lst = [10, 50, 80, 80, 100]

bisect_left(lst, 80)  # 2 (first 80)
bisect_right(lst, 80)  # 4 (after last 80)

bisect_left(lst, 15)  # 1
bisect_right(lst, 15)  # 1 (same, value not found)
```

#### Visual Explanation

For `lst = [10, 50, 80, 80, 100]`:

```
Index:  0    1    2    3    4
Value: 10   50   80   80   100
               ↑         ↑
               │         │
      bisect_left(80)=2  │
                         │
               bisect_right(80)=4
```

**Why `bisect_right` returns a larger index:**
- `bisect_left` says: "Give me the first place I can insert 80" → 2
- `bisect_right` says: "Give me the first place after the last 80" → 4

When the value is not found, there is no "first version" or "last version" difference, so both return the same index.

---

### 11. `index()` vs `bisect`

| Method | Search Type | Time | Requirement |
|---|---|---|---|
| `list.index(x)` | Linear Search | O(n) | None |
| `bisect_left()` / `bisect_right()` | Binary Search | O(log n) | Sorted list |

**When to use which:**
- Use `bisect` when you repeatedly search in a sorted list
- Use `index()` for one-time searches or unsorted lists

---

### 12. Why `bisect_right` in Problems (Example)

In a problem like Cow Baseball, we needed to find positions where:

```
low <= position3 <= high
```

We used two bounds:
- Left bound: `bisect_left(positions, low)` (first element >= low)
- Right bound: `bisect_right(positions, high)` (first element > high)

Count of valid positions:
```python
count = right_index - left_index
```

This replaces a slow `while` loop with a fast binary search.

---

### 13. The Power of Binary Search

**Example:**
```python
from bisect import bisect_left

lst = list(range(1, 1000001))

for i in range(1000000):
    where = bisect_left(lst, 1000000)
```

This performs:
- 1,000,000 searches
- Each in a list of 1,000,000 elements

**Why it is fast:**
- Linear search would check 1,000,000 elements per search
- Binary search checks only **~20 elements** per search (log₂(1,000,000))

---

### 14. Improving an Algorithm

1. Start with a **correct** solution first
2. Measure where the program is slow
3. Optimize only the bottleneck
4. Replacing Linear Search with Binary Search can greatly improve performance

Improving one small part of an algorithm can reduce the overall time complexity significantly.

---

### 15. Modules in Python

#### What is a Module?

A **module** is a collection of related Python code, usually containing multiple functions.

Python provides many built-in modules: `random`, `math`, `datetime`, `statistics`, etc.

#### Using Modules

```python
import module_name  # Import entire module

dir(module_name)  # List available names
help(module_name.function)  # View documentation
```

#### Common `random` Functions

| Function | Description |
|---|---|
| `random.randint(a, b)` | Random integer in `[a, b]` |
| `random.choice(seq)` | Random element from sequence |

#### Selective Import

```python
from module import function  # Import specific function, call without module name
```

#### Creating Your Own Module

- Place related functions in a separate `.py` file
- A module should **not** execute program logic immediately when imported
- It should wait until one of its functions is called
- Built-in modules like `random` only perform work when their functions are invoked

---

### 16. Common Mistakes to Avoid

| Mistake | Correction |
|---|---|
| Assuming small input means fast algorithm | Analyze number of operations, not just input size |
| Optimizing before measuring | Find the bottleneck first |
| Using Linear Search on sorted data repeatedly | Use `bisect` for faster searches |
| Ignoring time complexity | Always estimate operations for worst case |
| Trying to optimize before having a correct solution | Get correctness first, then optimize |

---

### 17. Golden Rules

> **Think: Problem → Idea → Algorithm → Code**

> **Before optimizing, identify what is being recomputed unnecessarily**

> **A correct algorithm is not always an efficient algorithm**

> **The hardest part is often identifying the correct search space**

> **Estimate operations using the general case, not small examples**

> **Small input size does not guarantee a fast Complete Search**

> **Use `set` when you need automatic duplicate removal**

> **Use `bisect` when you repeatedly search in sorted data**

> **Modules organize code and should not execute on import**

---

### 18. Quick Reference

#### Search Methods Comparison

| Method | Time | Requires Sorted |
|---|---|---|
| `list.index(x)` | O(n) | ❌ |
| `bisect_left(lst, x)` | O(log n) | ✅ |
| `bisect_right(lst, x)` | O(log n) | ✅ |

#### Common Complete Search Pattern

```python
best = initial_value
for candidate in all_candidates:
    if is_valid(candidate):
        score = evaluate(candidate)
        best = max(best, score)
```

#### Module Import

```python
import module
from module import function
```

---

### 19. Summary

- Complete Search tries all candidate solutions and keeps the best
- Choose the search space carefully; it is often the hardest part
- Small inputs do not guarantee fast algorithms — analyze operations
- Binary Search (`bisect`) is much faster than Linear Search on sorted data
- Modules organize code; do not execute logic on import
- Start with correctness, then optimize the bottleneck
- `set` is useful for automatic duplicate removal and fast membership
- Always think: Problem → Idea → Algorithm → Code

