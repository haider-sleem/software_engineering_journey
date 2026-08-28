## Chapter 10: Big O Basics

---

### What is Big O?

Big O measures **how the running time of an algorithm grows** as the input size increases. It describes the relationship between:

- Input size (`n`)
- Amount of work the algorithm performs

Big O does **not** measure exact time in seconds.

---

### 1. Constant Time — O(1)

An algorithm is **O(1)** if it performs the same amount of work **regardless** of input size.

```python
x = numbers[5]  # Always one step
```

**Common O(1) operations (average case):**

- List indexing
- Dictionary lookup / insertion
- List append (average case)

---

### 2. Linear Time — O(n)

An algorithm is **O(n)** if the work grows **directly** with input size.

```python
for item in data:
    process(item)  # One operation per item
```

**Doubling the input → doubles the work.**

#### Python Operations That Are O(n)

| Operation | Why |
|---|---|
| `input()` | O(n) with respect to input length |
| `string.count(" ")` | Checks every character |
| `value in list` | Linear search |
| `list.index(value)` | Linear search |
| `max(list)` / `min(list)` | Scans entire list |
| `sum(list)` | Visits every element |

#### Example

```python
line = input()  # O(n) – reads all characters
words = line.count(" ") + 1  # O(n) – scans all characters
# Total: O(n) + O(n) = O(n)
```

---

### 3. Big O Ignores Constants

All of these are **O(n)**:

```
n, 2n, 10n, 10000n, 2n + 8
```

Because Big O only cares about **growth rate**, not exact numbers.

---

### 4. Quadratic Time — O(n²)

Quadratic algorithms perform work proportional to the **square** of input size.

```python
for i in range(n):
    for j in range(n):
        do_constant_work()  # n × n iterations
```

#### Comparison

| Input Size | O(n) | O(n²) |
|---|---|---|
| n = 1,000 | 1,000 | 1,000,000 |
| n = 10,000 | 10,000 | 100,000,000 |

---

### 5. Nested Loops — Not Always O(n²)

```python
for i in range(10):  # 10 is constant
    for j in range(n):
        do_work()
# Total: 10n → O(n)
```

#### Sequential Loops (Not Nested)

```python
for i in range(n):  # O(n)
    do_work()

for j in range(n):  # O(n)
    do_work()
# Total: n + n = 2n → O(n)
```

---

### 6. Hidden Quadratic

Sometimes there is only **one visible loop**, but the algorithm is still O(n²).

```python
for address in addresses:  # O(n)
    if address in my_list:  # O(n) – linear search
        ...
# Total: n × n = O(n²)
```

#### Using a Set Makes It Faster

| Operation | Complexity |
|---|---|
| `value in list` | O(n) |
| `value in set` | O(1) average |

✅ Replacing a list with a set can reduce an algorithm from **O(n²) → O(n)**.

---

### 7. Cubic Time — O(n³)

Three nested loops → O(n³).

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            do_work()  # n³ iterations
```

| Input Size | Operations |
|---|---|
| n = 1,000 | 1,000,000,000 |

---

### 8. Sequential vs Nested — Summary

| Pattern | Complexity |
|---|---|
| Sequential loops | O(a + b) — **Add** |
| Nested loops | O(a × b) — **Multiply** |

---

### 9. Multiple Variables

Sometimes Big O uses **more than one variable**.

```python
for day in range(d):  # d days
    for franchisee in range(f):  # f franchisees
        ...
# Complexity: O(d × f)
```

**Important:** Do **not** simplify `O(df)` to `O(n²)` unless `d` and `f` grow at the same rate.

---

### 10. Logarithmic Time — O(log n)

**Binary Search** is the classic logarithmic algorithm.

Instead of checking every element, it removes **half** the search space each step.

```
512 → 256 → 128 → 64 → 32 → 16 → 8 → 4 → 2 → 1
```

| Input Size | Steps |
|---|---|
| 512 | ~9 |
| 1,000,000 | ~20 |

---

### 11. O(n log n) — Sorting

Sorting in Python uses **Timsort** → O(n log n) worst case.

| Algorithm | Complexity |
|---|---|
| Bubble Sort | O(n²) |
| Insertion Sort | O(n²) |
| Merge Sort | O(n log n) |
| Python's `sort()` | O(n log n) worst case |

---

### 12. Big O — Function Calls

**Always include the cost of function calls.**

```python
def f(lst):
    for i in range(len(lst)):  # O(n)
        lst[i] += 1


for i in range(len(lst)):  # O(n)
    f(lst)  # O(n)
# Total: n × n = O(n²)
```

**Golden Rule for Function Calls:**

> Analyze the cost of each call and combine it with how many times, and with what input sizes, the function is called.

---

### 13. Context Matters

A function's complexity depends on the **size of its input**.

```python
def no_high(lst):
    if max(lst) > 10:  # O(n) normally
        ...
```

If called with **at most 4 elements**, it is effectively **O(1)**.

---

### 14. Preprocessing for Faster Queries ⭐

Sometimes we can process the data once and store useful information so that later operations become faster.

#### Example: Longest Scarf Problem

| Approach | Complexity |
|---|---|
| Searching repeatedly through original data | O(m × n) |
| Preprocess once using a dictionary | O(n) |
| Process the queries using the dictionary | O(m) |
| **Total** | **O(n + m)** |

This is an example of **trading extra memory and preprocessing time for faster queries** — a key idea in Data Structures and Algorithms.

---

### 15. Big O Ranking (Fastest → Slowest)

```
O(1)       ← Fastest
O(log n)
O(n)
O(n log n)
O(n²)
O(n³)
O(2ⁿ)
O(n!)      ← Slowest
```

---

### 16. Practical Rule

| Complexity | Verdict |
|---|---|
| O(1), O(log n), O(n), O(n log n) | ✅ Usually fast enough |
| O(n²), O(n³) | ⚠️ Check constraints carefully |

---

### 17. Key Takeaways

- Big O measures **growth**, not exact speed.
- **Ignore constants** (`10n → O(n)`).
- **Ignore small additions** (`2n + 8 → O(n)`).
- One loop → usually **O(n)**.
- Two nested loops → usually **O(n²)**.
- Three nested loops → **O(n³)**.
- Sequential loops are still **O(n)**.
- Some Python operations are **already O(n)**.
- A single loop can be **O(n²)** if it calls an O(n) operation inside.
- Choose the right data structure (e.g., `set` instead of `list`) for better performance.
- Preprocessing can turn **O(m × n)** into **O(n + m)**.

---

### 18. Golden Rules

> When you see a function call:
> 1. Analyze the function itself.
> 2. Analyze the size of its input.
> 3. Combine with how many times it is called.

> Sorting is **O(n log n)** — not O(n), not O(n²).

> Write code that is:
> - Correct
> - Readable
> - Pythonic
> - Efficient enough for the constraints

> Optimize only when necessary.

