# Chapter 10: Writing Effective Functions

> *Beyond the Basic Stuff with Python — Al Sweigart*

---

## Core Idea

Good functions are not simply short functions. They should be readable, predictable, easy to test, and reasonably simple.

---

## Function Names

- Use **long, descriptive names** — prefer clarity over brevity or acronyms.
- Function names usually contain a verb.
- Methods inside a class or module may not need a noun if the surrounding context already makes the target clear (e.g., `reset()` inside `SatelliteConnection`).
- Avoid shadowing Python built-ins: `list`, `sum`, `open`, `type`, etc.

---

## Function Size

Small functions tend to:
- require fewer parameters
- have fewer side effects
- raise fewer different kinds of exceptions
- be easier to test and debug

Excessive splitting can increase overall program complexity. There is no strict universal line-count rule — keep functions as short as reasonably possible without splitting them into unnecessary smaller functions.

---

## Parameters and Arguments

| Term | Definition |
|------|-----------|
| **Parameter** | Name in the function definition |
| **Argument** | Value passed in the function call |

More parameters increase flexibility but also increase complexity.

### Default Arguments

```python
def introduction(name, greeting="Hello"):
    ...
```

- Parameters with default arguments must come **after** parameters without default arguments.
- Use defaults when a parameter usually has the same value.
- **Never use mutable defaults** such as `[]` or `{}` — they are shared across all calls.

---

## `*args` and `**kwargs`

### Passing arguments (at the call site)

```python
func(*items)    # expands an iterable into positional arguments
func(**options) # expands a mapping into keyword arguments
```

### Receiving arguments (in the definition)

```python
def func(*args):    # args is a tuple of positional arguments
    ...

def func(**kwargs): # kwargs is a dictionary of keyword arguments
    ...
```

- When both are used in a definition, `*args` must come before `**kwargs`.

### Forwarding arguments (wrapper functions)

```python
def wrapper(*args, **kwargs):
    return target(*args, **kwargs)
```

Use variadic arguments only when they make the API more natural.

---

## Functional Programming Concepts

Functional programming emphasizes functions that avoid modifying external state.

### Side Effects

Examples of side effects:
- Modifying global variables
- Writing files or databases
- Network operations
- Printing output
- Modifying a mutable object passed into a function — if that object is also referenced outside the function, this counts as a side effect

### Deterministic Functions

A deterministic function always returns the same result for the same inputs. A function can be non-deterministic if it depends on **external resources** such as:
- Global variables
- Files or databases
- Network or internet
- System clock
- Random number generators

> Deterministic functions can be cached because the same inputs always produce the same result — a useful space/time trade-off.

### Pure Functions

A **pure function** is both deterministic and free of side effects.

Pure functions are:
- Easier to unit test and reproduce/debug
- Composable with other pure functions
- Safe for concurrent execution (no dependency on external mutable state)

> Python does not enforce function purity — it is a design convention, not a language feature.

---

## Higher-Order Functions

Functions are first-class objects in Python — they can be stored in variables, passed as arguments, and returned from other functions.

### Lambda Functions

A lambda is a small anonymous function consisting of a single expression that acts as its return value:

```python
sorted(items, key=lambda item: item.price)
```

- Use `lambda` mainly for small functions passed directly as arguments.
- Use `def` when a function needs a meaningful name or will be reused.
- Avoid using `lambda` simply to store a function in a variable — use `def` instead.

### `map()` and `filter()`

- `map()` returns a **map object** (an iterator); convert with `list()` if needed.
- `filter()` returns a **filter object** (an iterator); convert with `list()` if needed.

List comprehensions are usually preferred — they are more readable and often faster:

```python
[str(n) for n in numbers]           # instead of map()
[n for n in numbers if n % 2 == 0]  # instead of filter()
```

---

## Return Values

- A function should generally return one consistent data type.
- Avoid mixing a normal return value with `None` as an error indicator — callers are forced to handle two different types, making bugs harder to track.
- Use **exceptions** to report error conditions when appropriate.

> Example: `str.find()` returns `-1` as an error code, which can silently cause bugs. `str.index()` raises a `ValueError` instead, making the error explicit.

> Exception: returning `None` is acceptable when the function *always* returns `None` (i.e., it is the expected return type, not an error signal).