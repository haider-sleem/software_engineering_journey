# Chapter 4 — Quicksort

## Divide and Conquer (D&C)

Divide and Conquer is a general problem-solving technique based on recursion.

Two steps:

1. Identify the **base case** — the simplest possible case.
2. **Break** the problem down into smaller and smaller pieces until it reaches the base case.

D&C is a way of thinking about a problem, not a single algorithm.

### Example: Summing an Array

For a recursive solution:

- **Base case:** an empty array or an array with one element.
- **Recursive case:** reduce the array and solve the smaller problem.

When working with recursive arrays, an empty array or a one-element array is often a good starting point for finding the base case.

---

## Quicksort

Quicksort is a sorting algorithm that uses Divide and Conquer.

### Basic Process

1. Choose an element as the **pivot**.
2. **Partition** the remaining elements into:
   - elements less than the pivot
   - elements greater than the pivot
3. Recursively apply quicksort to both sub-arrays.
4. Combine:

```text
sorted left + pivot + sorted right
````

The sub-arrays do not need to be sorted during partitioning; they only need to be divided around the pivot.

### Base Case

Arrays with fewer than two elements are already sorted:

```python
if len(array) < 2:
    return array
```

### Example Implementation

```python
def quicksort(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)
```

---

## Pivot Choice

Quicksort's performance depends heavily on the pivot.

### Good Split

A pivot near the middle produces smaller sub-arrays:

```text
        array
       /     \
    smaller  greater
```

The recursive depth is approximately:

```text
O(log n)
```

### Bad Split

If the pivot repeatedly produces one empty sub-array and one large sub-array:

```text
        array
           \
         n - 1
            \
           n - 2
              \
              ...
```

The recursive depth becomes:

```text
O(n)
```

---

## Quicksort Complexity

Each partitioning step examines the elements in the current sub-array:

```text
O(n)
```

### Best / Average Case

When the partitions are reasonably balanced:

```text
O(n) × O(log n) = O(n log n)
```

Average-case time:

```text
O(n log n)
```

### Worst Case

When partitions are extremely unbalanced:

```text
O(n) × O(n) = O(n²)
```

Worst-case time:

```text
O(n²)
```

The book recommends choosing a **random element as the pivot** to obtain `O(n log n)` average performance.

> **Caveat:** if all elements are equal, the simple implementation shown above still reaches `O(n²)` worst case without additional logic to handle duplicates.

---

## Call Stack Size

Quicksort also uses recursion, so pivot choice affects the call stack.

| Case       | Call Stack |
| ---------- | ---------: |
| Best case  |   O(log n) |
| Worst case |       O(n) |

---

## Big O and Constants

Two algorithms can have the same Big O complexity but different practical speeds.

For example:

```text
10 ms × n
1 second × n
```

Both are:

```text
O(n)
```

Big O focuses on how runtime grows as input size increases, so constants are normally ignored.

However, constants can sometimes matter in practice when comparing algorithms with the same Big O.

The book uses Quicksort and Merge Sort as an example: both can be `O(n log n)`, but Quicksort can be faster in practice because of implementation details and its typical behavior.

---

## Quicksort vs. Selection Sort

Selection Sort:

```text
O(n²)
```

Quicksort:

```text
Average: O(n log n)
Worst:   O(n²)
```

So Quicksort can be much faster for large inputs when its partitions are reasonably balanced.

---

## Inductive Proof Connection

The reasoning behind Quicksort resembles an **inductive proof**:

* **Base case:** Quicksort correctly sorts arrays of size 0 or 1.
* **Inductive case:** If Quicksort works correctly for smaller cases, the same logic extends to larger sizes — partitioning the array and recursively applying Quicksort to the resulting sub-arrays.

---

## Mental Model

Think of Quicksort as repeatedly asking:

> "Can I make this problem smaller until it becomes trivial?"

For an array:

```text
[10, 5, 2, 3]

pivot = 10

less    = [5, 2, 3]
pivot   = [10]
greater = []
```

Then recursively sort:

```text
quicksort([5, 2, 3])
```

until every sub-array reaches the base case.

---

## Key Takeaways

* **Divide and Conquer** = reduce a problem into smaller problems until reaching a base case.
* D&C is commonly implemented with **recursion**.
* **Quicksort** uses D&C to sort an array.
* The **pivot** determines how the array is partitioned.
* Balanced partitions lead to `O(n log n)` performance.
* Highly unbalanced partitions lead to `O(n²)` performance.
* Random pivot selection gives Quicksort `O(n log n)` average runtime.
* Call stack size is `O(log n)` in the best case and `O(n)` in the worst case.
* Big O ignores constants, but constants can still affect practical performance.
