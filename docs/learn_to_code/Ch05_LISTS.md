## Chapter 5: Python Lists

### Discovering List Methods on Your Own

You can find and understand list methods using two simple tools:

#### 1. `dir()` — See All Available Methods

Use `dir()` with an empty list `[]` to see all methods you can use with lists.

**Example:**
```python
print(dir([]))
```

This will output a list of methods like `'append'`, `'clear'`, `'sort'`, and others.

#### 2. `help()` — Understand a Specific Method

Use `help()` with a method to learn how it works and what arguments it takes.

**Example:**
```python
help([].append)
```

This displays the documentation explaining what `append()` does and how to use it.

---

### `split()` and `join()`

#### `split()`

Breaks a string into a list of smaller pieces based on spaces or a specific separator.

**Example:**
```python
"0.2 0.4".split()  # Output: ['0.2', '0.4']
```

#### `join()`

Combines elements into a single string using a separator.

It works on **any sequence** (lists, strings, tuples), not just lists.

**Example on a string:**
```python
"*".join("abcd")  # Output: 'a*b*c*d'
```

---

### Modifying List Elements in a Loop

#### ❌ The Wrong Way

When you loop using `for value in lst:`, modifying `value` only changes a temporary variable. It does **not** update the actual list.

```python
proportions = ["0.2", "0.08", "0.4", "0.32"]
for value in proportions:
    value = float(value)

print(proportions)  # Output: ['0.2', '0.08', '0.4', '0.32'] — unchanged
```

#### ✅ The Right Way

To permanently update elements inside a list, loop through the indices using `range(len(lst))` and assign the new value directly to `lst[i]`.

```python
proportions = ["0.2", "0.08", "0.4", "0.32"]
for i in range(len(proportions)):
    proportions[i] = float(proportions[i])

print(proportions)  # Output: [0.2, 0.08, 0.4, 0.32]
```

---

### Rounding Numbers: Different Methods

| Method | Behavior | Example |
|---|---|---|
| `int()` | Drops the decimal part (truncates toward zero) | `int(6.9) → 6`, `int(0.9) → 0` |
| `math.floor()` | Always rounds down | `math.floor(6.9) → 6` |
| `math.ceil()` | Always rounds up | `math.ceil(6.1) → 7` |
| `round()` | Rounds to the nearest integer | `round(6.6) → 7`, `round(6.4) → 6` |

#### Special Note: Bankers' Rounding

In Python, if a number ends in exactly `.5`, `round()` rounds to the nearest **even** integer to prevent statistical bias.

```python
round(6.5)  # Output: 6 (6 is the nearest even number)
round(7.5)  # Output: 8 (8 is the nearest even number)
```

---

### Understanding Copying in Python: Simple vs. Nested Lists

How you copy a list depends on whether it is a **Simple List** (1D) or a **Nested List** (2D / list of lists).

#### 1. Simple Lists (One-Dimensional)

For a flat list containing immutable values such as numbers or strings, using `[:]` creates a new list. Changing an element in the copy does not affect the original list.

```python
original = [1, 2, 3]
copied = original[:]

copied[0] = 99

print(original)  # Output: [1, 2, 3]  — unchanged
print(copied)  # Output: [99, 2, 3] — changed
```

**Important:** This is a **shallow copy**. It works safely here because the list contains immutable values (numbers). If the list contained mutable objects (like nested lists), the inner objects would still be shared.

---

#### 2. Nested Lists (Two-Dimensional / Grids)

When you have a list of lists, using `[:]` becomes a trap. It only copies the **outer container**, but the **inner lists (rows)** are still shared in memory. This is called a **Shallow Copy**.

**The Trap:**

```python
grid = [[".", "F", "."], [".", ".", "."]]

# Shallow Copy — dangerous for 2D grids
bad_copy = grid[:]
bad_copy[1][1] = "X"

print(grid[1][1])  # Output: 'X' — the original grid is changed!
```

#### 🛠️ The Correct Way: Deep Copy for Grids

To make a truly independent copy of a 2D grid, copy **every row individually** using a list comprehension:

```python
# Safe Copy for 2D grids
good_copy = [row[:] for row in grid]
good_copy[1][1] = "X"

print(grid[1][1])  # Output: '.' — original stays clean
print(good_copy[1][1])  # Output: 'X' — only the copy changes
```

---

### Summary Table

| Use Case | Method | Safe? | Why |
|---|---|---|---|
| Simple list (immutable values) | `original[:]` | ✅ Yes | Creates a new list |
| Nested list / 2D grid | `[row[:] for row in grid]` | ✅ Yes | Copies each row individually |
| Nested list / 2D grid | `original[:]` | ❌ No | Shares inner lists (shallow copy) |

