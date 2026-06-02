## Chapter 5: Python Lists

Here is how you can find and understand list methods on your own using two simple rules:

### 1. Discovering List Methods

To see all available methods for a list, use the `dir()` function with an empty list `[]`.

* **Example:**
```python
print(dir([]))

```


*This will output a list of all methods you can use with lists, such as `'append'`, `'clear'`, `'sort'`, and others.*

### 2. Understanding a Specific Method

To learn how a specific method works and see what arguments it takes, use the `help()` function. Replace `xxx` with the name of the method you want to explore.

* **Example:** If you want to learn about the `append` method, run:
```python
help([].append)

```


*This will display the documentation explaining exactly what `append` does and how to use it.*

-----

* **`split()` Method**: It is used to break a single string into a list of smaller pieces based on spaces or a specific separator. For example, `'0.2 0.4'.split()` becomes `['0.2', '0.4']`.

* **`join()` Method**: It is used to combine elements into a single string using a separator. Crucially, `join()` can work on **any sequence** (like lists or even strings), not just lists. For example, using it on a string of characters:
  ```python
  '*'.join('abcd')  # Output: 'a*b*c*d'

-----

* **Modifying List Elements**: 
  When you loop using `for value in lst:`, modifying `value` only changes a temporary variable, **not** the actual list. 
  
  >>> for value in proportions:
...     value = float(value)
>>> proportions
['0.2', '0.08', '0.4', '0.32']

To permanently update elements inside a list (like converting strings to floats), you must loop through the indices using `range(len(lst))` and assign the new value directly to `lst[i]`.

>>> proportions
['0.2', '0.08', '0.4', '0.32']
>>> for i in range(len(proportions)):
...     proportions[i] = float(proportions[i])
...
>>> proportions
[0.2, 0.08, 0.4, 0.32]

-----

```markdown
* **`int()` for Truncation (Rounding Down)**: 
  Using `int()` on a float drops the fractional part completely and moves toward zero. It does not round to the nearest number; it simply cuts off the decimal.
  ```python
  int(6.3)  # Output: 6
  int(6.9)  # Output: 6
  int(0.9)  # Output: 0

```

* **`math.ceil()` for Rounding Up**:
Imported from the `math` module, `math.ceil()` always rounds a float up to the next highest integer, no matter how small the decimal part is.
```python
import math
math.ceil(6.1)  # Output: 7
math.ceil(0.1)  # Output: 1

```


* **`math.floor()` for Always Rounding Down**:
Also from the `math` module, `math.floor()` always rounds a float down to the next lowest integer. For positive numbers, it works exactly like `int()`.
```python
import math
math.floor(6.9)  # Output: 6

```


* **`round()` for Nearest Integer (Bankers' Rounding)**:
The built-in `round()` function rounds to the nearest whole number. However, if the number ends in exactly `.5`, Python rounds it to the nearest **even** integer to prevent statistical bias.
```python
round(6.6)  # Output: 7 (Standard rounding)
round(6.4)  # Output: 6 (Standard rounding)
round(6.5)  # Output: 6 (6 is the nearest EVEN number)
round(7.5)  # Output: 8 (8 is the nearest EVEN number)

```
----


## Understanding Copying in Python: Simple vs. Nested Lists

In Python, how you copy a list depends on whether it is a **Simple List** (1D) or a **Nested List** (2D/List of Lists). 

---

### 1. Simple Lists (One-Dimensional)
When you have a flat, simple list, using the slice operator `[:]` creates a **completely independent copy** in memory.

```python
# Example:
original = [1, 2, 3]
copied = original[:]

copied[0] = 99

print(original)  # Output: [1, 2, 3]    -> Unchanged (Safe!)
print(copied)    # Output: [99, 2, 3]   -> Changed

```

**Why it works:** The list only contains basic elements (like numbers or strings). Python copies them directly into a new list.

---

### 2. Nested Lists (Two-Dimensional / Grid)

When you have a list of lists, using `[:]` directly becomes a trap. It only copies the **outer container**, but it keeps sharing the **inner lists (rows)** in memory. This is called a **Shallow Copy**.

If you modify the copy, the original grid will change too!

```python
# The Trap:
grid = [
    ['.', 'F', '.'],
    ['.', '.', '.']
]

# Shallow Copy (Dangerous for 2D grids)
bad_copy = grid[:] 

bad_copy[1][1] = 'X'

print(grid[1][1])  # Output: 'X' -> The original grid is RUINED!

```

#### 🛠️ The Correct Way (Deep Copy for Grids)

To make a truly independent copy of a 2D grid, you must copy **every row individually** using a list comprehension:

```python
# Safe Copy for 2D grids:
good_copy = [row[:] for row in grid]

good_copy[1][1] = 'X'

print(grid[1][1])       # Output: '.' -> Original stays clean and safe!
print(good_copy[1][1])  # Output: 'X' -> Only the copy changes

```

**Summary for your notes:**

* Use `list[:]` ONLY for simple, flat lists.
* Use `[row[:] for row in grid]` for 2D grids/matrices to avoid memory reference bugs.

```

---

