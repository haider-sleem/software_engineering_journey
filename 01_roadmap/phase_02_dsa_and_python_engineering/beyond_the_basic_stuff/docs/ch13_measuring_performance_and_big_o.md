# Chapter 13: Measuring Performance and Big O Algorithm Analysis

---

## The Danger of Premature Optimization

> *"Premature optimization is the root of all evil"* — attributed to Donald Knuth and Tony Hoare.

Programmers often use overly complex tricks to save memory or speed before confirming there's a real performance problem. The result is usually messy, unreadable code that works against Python's focus on readability (*The Zen of Python*).

---

## Measuring Runtime vs. Assuming

Never guess that a clever trick is faster, or that the original code is slow — measure and compare using empirical tools.

**Runtime:** the time it takes for code to run. Increasing runtime means the program is slowing down.

---

## `timeit` Module

**Purpose:** measures the runtime of a small code snippet by running it many times to find an average.

- Disables garbage collection by default during timing, for consistent results — can be re-enabled if the code being measured depends on it.
- Accepts a string of code (multiple lines separated by `;`) passed to `timeit.timeit()`.

### Practical Example: Swapping Variables

| Approach | Code | Result |
|----------|------|--------|
| **XOR trick** | `a ^= b; b ^= a; a ^= b` | Cryptic and surprisingly **slower** (~0.13s per million runs) |
| **Temp variable** | `temp = a; a = b; b = temp` | Very readable and **twice as fast** as XOR |
| **Tuple unpacking (Pythonic)** | `a, b = b, a` | Clean, readable, and the **fastest** |

> **Takeaway:** sacrificing readability to save bytes or nanoseconds is almost never worth it.

---

## Advanced `timeit` Techniques

### The `setup` Argument

Runs preparation code **once**, before the measured code, so setup time doesn't pollute the results.

```python
timeit.timeit("random.randint(1, 100)", setup="import random", number=10_000_000)
```

### Fixing `NameError` with `globals=globals()`

By default, `timeit.timeit()` runs in an isolated scope and can't see your script's variables — pass `globals=globals()` to fix this:

```python
spam = "hello"
timeit.timeit("print(spam)", number=1, globals=globals())
```

### Reusable Benchmarking with `timeit.Timer`

Instantiate a `Timer` once and reuse it across multiple measurements:

```python
import timeit

my_timer = timeit.Timer(stmt="pass", setup="import random", globals=globals())

time_a = my_timer.timeit(stmt="random.randint(1, 10)", number=100_000)
time_b = my_timer.timeit(stmt="random.choice([1, 2, 3])", number=100_000)
```

### Default Signature

```python
timeit.Timer(stmt='pass', setup='pass', timer=<default_timer>, globals=None)
```

| Parameter | Meaning |
|-----------|---------|
| `stmt` | Code snippet to measure (default `'pass'`) |
| `setup` | Initialization code run once before timing (default `'pass'`) |
| `timer` | Internal timing function (platform-dependent default) |
| `globals` | Namespace scope dictionary (default `None`) |

---

## Program/Function-Level Profiling with `cProfile`

| Tool | Best for |
|------|----------|
| `timeit` | Tiny code snippets (micro-benchmarking) |
| `cProfile` | Entire programs or large functions — shows time spent in every function |

### Output Metrics

| Column | Meaning |
|--------|---------|
| `ncalls` | Number of times the function was called |
| `tottime` | Time spent *only* inside that function (excluding sub-functions) |
| `cumtime` | Total time in the function **and** all sub-functions — the key metric for finding the main problem |
| `percall` | Average time per call — exact meaning depends on the column/context in the profiler output |

### Professional Profiling Template

```python
import cProfile
# import your_heavy_module


def main():
    print("Starting profiling...")

    profiler = cProfile.Profile()
    profiler.enable()

    # your_heavy_module.process_data()

    profiler.disable()
    profiler.print_stats(sort="cumulative")  # slowest functions on top


if __name__ == "__main__":
    main()
```

---

## Bottlenecks and Amdahl's Law

**Bottleneck:** the single slowest component holding back overall performance (e.g., `builtins.pow` taking 99% of runtime in an RSA cipher).

**Amdahl's Law:** the maximum overall speed-up from optimizing one part of a program.

```
Speed-up = 1 / ((1 - p) + (p / s))
```
- `p` = the portion of time that part takes (e.g., 90% = 0.9)
- `s` = the speed multiplier (e.g., twice as fast = 2)

> **Golden Rule:** always optimize the heaviest, slowest part first. Speeding up a function that's 90% of runtime matters far more than optimizing one that's 1%.

**Analogy:** a 10% discount on an expensive house saves far more than 10% off cheap shoes.

---

## Big O Notation — Fundamentals

**What is Big O?** describes how an algorithm's runtime grows as input size grows — it measures the **trend**, not exact seconds.

**What is `n`?** the size of the input data (e.g., the number of books in a list passed to a function).

### The 4 Steps to Determine Big O

1. **Identify `n`** — which input parameter drives the workload.
2. **Count the dominant operations** — this is a simplification for analysis, not a literal rule: count the work each line performs (a line calling an O(n) function is not "1 step"), and loops multiply that work by how many times they execute (nested loops → n × n = n²).
3. **Drop lower orders** — keep only the largest term: `2n + 3` → `2n`.
4. **Drop coefficients** — remove multipliers: `2n` → `O(n)`.

### Why Drop Lower Orders and Coefficients?

- At massive scale (n = 10 billion), adding 3 extra steps makes no real difference.
- Higher-order terms always win eventually: O(n²) will overtake O(n) as `n` grows, even if the O(n) algorithm has a huge coefficient (e.g., `1000n`).

---

## Common Big O Ranks

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Getting an item from a list by index |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | A single `for` loop |
| O(n²) | Quadratic | Two nested `for` loops |

**Quick math rules:**
- **Coefficients** (e.g., the `3` in `3n²`) are ignored in Big O.
- **Exponents:** `n × n = n²` (nested loops).
- **Logarithms** are the inverse of exponents: `log₂(16) = 4` because `2⁴ = 16`.

---

## Practical Code Patterns

| Pattern | Big O |
|---------|-------|
| Fixed-length loop (e.g., `for i in range(10):`) | O(1) — doesn't depend on `n` |
| Loop running `100 × n` times | O(n) — coefficient dropped |
| Nested loops, both over `n` | O(n²) |
| Binary Search on a sorted list | O(log n) |
| Binary Search **including** the `.sort()` call needed first | O(n log n) |

---

## Big O of Common Python Built-ins

### Lists & Sequences

| Operation | Complexity | Note |
|-----------|-----------|------|
| `s[i]` (read/assign by index) | O(1) | |
| `len(s)` | O(1) | Python stores the length — doesn't count items |
| `s.append(value)` | O(1) | |
| `s.insert(i, value)` / `s.remove(value)` | O(n) | Requires shifting elements |
| `s.reverse()` | O(n) | Moves items by position, no comparisons |
| `s.sort()` | O(n log n) | Compares values to determine order — commonly efficient for comparison-based sorting at scale |
| `value in s` | O(n) | Checks items one by one |

### Dictionaries & Sets

> Dicts and sets use hashing, making lookups very fast.

| Structure | Operation | Complexity |
|-----------|-----------|-----------|
| Dictionary | `m[key]` / `m[key] = value` | O(1) |
| Set | `m.add(value)` | O(1) |
| Dictionary / Set | membership (`value in m`) | O(1) average — much faster than list search |

---

## Big O "At a Glance"

| Pattern | Big O |
|---------|-------|
| No data access | O(1) |
| A loop over data | O(n) |
| Two nested loops over data | O(n²) |
| Dividing data in half repeatedly | O(log n) |
| Sorting data | O(n log n) |
| Testing every combination | O(2ⁿ) |
| Testing every permutation | O(n!) |

**Intuition:**
- **O(2ⁿ):** each element creates two choices (include/exclude), so the number of possibilities doubles with every added element.
- **O(n!):** counts every possible ordering of all the elements.

### Sorting Before Binary Search: Where Does the Cost Go?

If the list is **unsorted** and you sort it first:

```python
haystack.sort()  # O(n log n)
binary_search(haystack)  # O(log n)
```

Total: `O(n log n) + O(log n) = O(n log n)` — the sort dominates.

If the list is **already guaranteed sorted**, only the search cost applies: `O(log n)`.

> Moving the sort elsewhere doesn't make the overall program faster — it just relocates where the O(n log n) cost is paid.

---

## The Golden Rule: "n Is Usually Small"

> **Rob Pike's Rule:** "Fancy algorithms are slow when `n` is small, and `n` is usually small."

- Big O matters most at massive scale — real-world data is often small.
- Don't over-engineer: a complex O(log n) solution may not be worth it if a simple O(n) approach handles a small list just fine.
- **Big O does not replace profiling** — always use `timeit` or `cProfile` to find real bottlenecks.

### Reminder: Big O ≠ Actual Speed

```python
def wait_an_hour():
    time.sleep(3600)
```

This function is technically **O(1)** — its runtime doesn't depend on any input size `n` — yet it takes a full hour to run.

> **O(1) does not necessarily mean fast.** Big O describes how performance changes as `n` grows, not the actual number of seconds a function takes.