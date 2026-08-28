# Chapter 8: Functions

> *Python Crash Course*

---

## Function Basics

A named block of code that performs a specific task — reduces repetition, improves readability, and organizes logic.

```python
def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"
```

- A **docstring** is a string literal placed as the first statement inside a function.
- It documents what the function does.
- Python's built-in `help()` can display it: `help(greet)`.

---

## Parameters and Arguments

| Term | Definition |
|------|-----------|
| **Parameter** | Variable defined in the function signature |
| **Argument** | Actual value passed when calling the function |

### Positional Arguments

```python
def describe(animal, color):
    print(f"A {color} {animal}.")


describe("cat", "black")
```

### Keyword Arguments

```python
describe(color="black", animal="cat")  # order doesn't matter
```

### Default Values

```python
def describe(animal, color="brown"):
    print(f"A {color} {animal}.")
```

- Parameters with defaults must come **after** parameters without defaults.
- If no argument is provided, the default is used.

---

## `*args` and `**kwargs`

```python
# *args — collects extra positional arguments into a tuple
def make_pizza(size, *toppings):
    print(f"{size} pizza with: {toppings}")


make_pizza("large", "mushrooms", "peppers")
# large pizza with: ('mushrooms', 'peppers')


# **kwargs — collects extra keyword arguments into a dictionary
def build_profile(name, **info):
    info["name"] = name
    return info


profile = build_profile("Haider", city="Damietta", role="developer")
# {'city': 'Damietta', 'role': 'developer', 'name': 'Haider'}
```

- `*args` is useful when the number of positional arguments is not known in advance.
- `**kwargs` is useful when the number of keyword arguments is not known in advance.

---

## Return Values

A function can return any Python object — a value, list, dictionary, or other structure.

```python
def full_name(first, last):
    return f"{first} {last}".title()


name = full_name("haider", "sleem")  # "Haider Sleem"
```

A function that reaches the end without a `return` statement returns `None`.

---

## Lists and Functions

```python
# Modifies the original list
def add_item(lst, item):
    lst.append(item)


# Works on a copy — original unchanged
def add_item_safe(lst, item):
    copy = lst[:]
    copy.append(item)
    return copy
```

Pass `lst[:]` when calling the function if you want to protect the original list from modification.

---

## Modules and Importing

A module is a `.py` file containing functions that can be imported elsewhere.

```python
# Preferred — explicit, avoids naming conflicts
import module_name

module_name.function()

# Import specific names
from module_name import function_one, function_two

# Avoid — pollutes the namespace, causes unpredictable conflicts
from module import *
```

---

## Practical Application: Backend Thinking

> *Personal notes connecting Chapter 8 concepts to backend development goals.*

| Principle | What It Means in Practice |
|-----------|--------------------------|
| **Modularity** | Each function has one job: `add_product()`, `remove_product()`, `get_products()` |
| **Maintainability** | Change logic in one place — the rest of the system updates automatically |
| **Abstraction** | The main file says *what* happens; functions define *how* |
| **Separation of Concerns** | Do not mix input handling, business logic, and output in the same function |

**Common mistakes to avoid:**
- Writing everything in one file
- Functions that do more than one job
- Vague or unclear naming
- Mixing logic with input/output handling

---

## Review Notes

**Substantive corrections made:**

1. **Docstring description** — changed "first line" to "first statement" (technically accurate: a docstring is a string literal as the first *statement*, not simply the first line).
2. **`*args` / `**kwargs` output comments** — added sample output in comments to make the behavior immediately visible without running the code.
3. **`None` return** — added a note that functions without an explicit `return` return `None`; this is a common source of beginner errors and belongs in this section.
4. **Removed source-uncertainty notes** — replaced with clean, accurate content per the review instructions.