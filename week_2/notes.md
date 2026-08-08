# Week 2: Loops, Lists, and Dictionaries

---

## Why Loops?

- Avoid repeating the same code.
- Make programs shorter and easier to maintain.
- Easy to change the number of repetitions.

---

## `while` Loop

Repeats code while a condition is `True`. Always ensure the condition eventually becomes `False`, or you create an **infinite loop**.

```python
i = 0
while i < 3:
    print("Meow")
    i += 1
```

### Short Assignment Operators

| Instead of | Use |
|------------|-----|
| `i = i + 1` | `i += 1` |
| `i = i - 1` | `i -= 1` |

> Python has no `++` or `--` operators.

### Intentional Infinite Loop

Use `while True:` with `break` to exit when a condition is met:

```python
while True:
    n = int(input("Number: "))
    if n > 0:
        break
```

- `break` — exits the nearest loop only.
- `continue` — skips the current iteration and starts the next one.

---

## `for` Loop

Use `for` when iterating over an iterable or a known sequence of values. Python handles the counter automatically.

```python
for i in range(3):
    print("Meow")
```

### `range()`

- `range(n)` generates numbers from `0` up to (but not including) `n`.
- Much cleaner than writing a list manually.

```python
range(3)  # → 0, 1, 2
range(1000000)  # instead of [0, 1, 2, ..., 999999]
```

### Unused Variable (`_`)

If the loop variable is not used, replace it with `_`:

```python
for _ in range(3):
    print("Meow")
```

This tells other programmers the variable is intentionally unused.

---

## `while` vs `for`

| Use | When |
|-----|------|
| `for` | Number of repetitions is known |
| `while` | Repetition depends on a condition |

---

## Functions and Loops

- `return` exits the whole function and returns a value — cleaner than using `break` followed by `return`.
- Split programs into small functions, each with one responsibility.

```python
def get_number():
    """Validates and returns a positive integer."""
    while True:
        n = int(input("Number: "))
        if n > 0:
            return n


def meow(n):
    """Prints 'Meow' exactly n times."""
    for _ in range(n):
        print("Meow")
```

---

## Lists

A list stores multiple values in one variable, in order.

```python
students = ["Hermione", "Harry", "Ron"]
```

- Written using square brackets `[]`.
- Can contain strings, numbers, or other types.
- **Zero-indexed** — first item is at index `0`.

### Iterating Over a List

```python
# Direct iteration — preferred when you only need values
for student in students:
    print(student)

# Index-based — use when you need the index
for i in range(len(students)):
    print(i + 1, students[i])  # numbering from 1
```

- `len()` returns the number of items in a list.
- Use meaningful variable names (`student`, not `s`).
- Use `_` only if the loop variable is **not used**.

---

## Dictionaries

A dictionary stores **key → value** pairs.

```python
student = {"name": "Harry", "house": "Gryffindor"}
print(student["name"])  # → Harry
```

- Written using curly braces `{}`.
- Keys must be unique.
- Looping over a dictionary gives you the **keys** by default:

```python
for key in student:
    print(key, student[key])
```

---

## List of Dictionaries

Use when each item has multiple attributes — a common pattern for real-world data:

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
]

for student in students:
    print(student["name"], student["house"])
```

---

## `None`

- `None` means **no value** — different from `""` or `0`.
- Use `None` when data does not exist.

```python
house = None
```

---

## Nested Loops

A loop inside another loop — useful for 2D structures.

```python
for i in range(3):  # rows
    for j in range(3):  # items per row
        print("#", end="")
    print()  # move to next line
```

**Mental model:**
- Outer loop → top to bottom (rows)
- Inner loop → left to right (items in each row)

### `print()` and `end`

- `print()` moves to a new line by default.
- `end=""` keeps output on the same line.

### String Multiplication

Repeat a character without a loop:

```python
print("#" * 3)  # → ###
```

---

## Functions as Abstractions

Hide implementation details behind a clear name:

```python
def print_row(width):
    print("#" * width)


def print_square(size):
    for _ in range(size):
        print_row(size)
```

- The caller does not need to know *how* the function works.
- Internal implementation can change without affecting calling code.
- Each function handles one specific responsibility (**decomposition**).

---

## Key Takeaways

- Use `for` for a known number of repetitions; use `while` for condition-based repetition.
- `range(n)` starts at `0` and stops before `n`.
- `_` signals an intentionally unused variable.
- Prefer direct list iteration unless you need the index.
- Use a **list** for a collection of similar items.
- Use a **dictionary** when each item has associated information.
- Use a **list of dictionaries** for real-world records.
- Nested loops handle 2D structures.
- Good functions abstract complexity and make code reusable.