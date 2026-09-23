# Chapter 11: Comments, Docstrings, and Type Hints

> *Beyond the Basic Stuff with Python — Al Sweigart*

---

## The Three Tools

| Tool | Purpose |
|------|---------|
| **Comments** | Explain information for programmers reading the source code |
| **Docstrings** | Document modules, classes, functions, and methods — accessible by Python and documentation tools |
| **Type hints** | Describe expected data types; used by static analysis tools, not enforced at runtime |

---

## Comments

A single-line comment starts with `#`. Python ignores it during execution.

```python
# Calculate the total price.
total = price * quantity
```

**Multiline comments:** Python has no dedicated multiline-comment syntax. A standalone triple-quoted string can be used as a multiline comment:

```python
"""
This is a multiline comment.
It explains a larger part of the program.
"""
```

> Note: triple-quoted strings placed at the start of a module, class, or function are **docstrings**, not comments.

> Technical note: a standalone triple-quoted string is technically an **unassigned string literal**, not a comment. Unlike `#` comments, which the interpreter discards entirely, an unassigned string literal occupies memory at runtime (unless it is a docstring, in which case it is attached to the object's `__doc__`). Use it sparingly when a block explanation is needed.

### Comment Style

- One space after `#`: `# Good` not `#Bad`
- Usually on their own line, same indentation as the code
- Clear language, correct capitalization, punctuation
- Respect the project's line-length limit

### Block vs. Inline Comments

```python
# Block comment — a group of related lines
# Check that the product exists.
# Check that enough inventory is available.

while True:  # Inline — short explanation at end of a line
    ...

TOTAL_DISKS = 5  # More disks means a harder puzzle.
```

Inline comments should be short. If the explanation is long, move it to its own line.

---

## What Should a Comment Explain?

**The most important rule: explain WHY, not WHAT.**

```python
# Bad — the code already says this:
current_wages *= 1.5  # Multiply wages by 1.5.

# Good — explains the reason:
current_wages *= 1.5  # Account for the time-and-a-half wage rate.
```

> This rule applies mainly to **explanatory comments**. Other comment types serve different purposes: **summary comments** describe what a block does at a higher level, and **lessons-learned comments** preserve knowledge. The "WHY not WHAT" rule is the most important guideline for explanatory comments specifically — not a universal rule for every comment.

### Summary Comments

Describe a group of statements at a higher level — helps readers scan large files quickly:

```python
# Switch turns to the other player.
if player_turn == PLAYER_X:
    player_turn = PLAYER_O
elif player_turn == PLAYER_O:
    player_turn = PLAYER_X
```

### Lessons-Learned Comments

Preserve important knowledge discovered during development — especially when:
- a problem took significant effort to discover
- a library has an unexpected limitation
- a non-obvious workaround is required
- future developers could easily repeat the same mistake

```python
# The library cannot safely update the chart while the data buffer
# is being resized, so the resize must happen before the update loop.
```

### TODO Comments

```python
# TODO: Add barcode validation.
```

Other common tags: `FIXME`, `HACK`, `XXX`. The author recommends keeping it simple and mainly using `TODO`. These are useful reminders but should not replace a proper issue-tracking system.

### Legal Comments

```python
"""
Warehouse System
Copyright (C) 2026
See LICENSE for the full license text.
"""
```

Prefer linking to the full license rather than copying large license text into every file.

### Professional Tone

Avoid jokes, insults, emotional comments, or frustration directed at other programmers. Keep comments polite, direct, and clear.

---

## Magic Comments

```python
#!/usr/bin/env python3       # Shebang — tells the OS which interpreter to use
# -*- coding: utf-8 -*-      # Encoding declaration
```

Modern Python 3 uses UTF-8 by default — an explicit UTF-8 encoding comment is normally unnecessary. Magic comments can appear before a module docstring.

---

## Docstrings

A docstring is a string placed:
- at the beginning of a module
- immediately after a `class` statement
- immediately after a `def` statement

Use **triple double quotes** (`"""`) by convention.

### Function Docstring

```python
def calculate_total(price, quantity):
    """Return the total price."""
    return price * quantity
```

### Class Docstring

```python
class Product:
    """Represent a product in the inventory."""

    def __init__(self, name, price):
        self.name = name
        self.price = price
```

### Module Docstring

```python
"""
Inventory management functions.

This module contains functions for adding,
removing, and searching inventory items.
"""
```

### Accessing Docstrings

```python
print(calculate_total.__doc__)   # via __doc__
help(calculate_total)            # via help()
```

Documentation tools can also extract docstrings automatically.

---

## Type Hints

Introduced in Python 3.5. Python **does not enforce** them at runtime — type hints are for static analysis tools and human readers.

```python
def describe_number(number: int) -> str:
    ...
```

- `number: int` — parameter expected to be an integer
- `-> str` — function expected to return a string

### Variable Type Hints

```python
my_lucky_number: int = 42
```

### Gradual Typing

Python is dynamically typed; type hints provide optional static typing — you don't have to annotate everything. The more hints you provide, the more a static checker can help.

### Type Inference

Static checkers can often infer types without explicit hints:

```python
spam = 42        # inferred as int
spam: int = 42   # explicit — makes intention clearer and catches unintentional changes
```

### Classes as Types

```python
class CatTail:
    def __init__(self, length: int, color: str) -> None:
        ...

zophie_tail: CatTail = CatTail(29, "grey")
```

---

## Static Analyzers — Mypy as an Example

```bash
python -m pip install --user mypy
python -m mypy example.py
```

An editor can run Mypy in the background to show type errors while writing code.

> Other tools in this category include **Pyright**, **Pyre**, and **Pylance**. Mypy is the most widely used and is the one covered in this chapter.

### Ignoring a Warning

```python
value = some_operation()  # type: ignore
```

Use sparingly — ignoring warnings can hide real bugs. It is usually better to fix the code.

---

## Multiple Types — `Union`

```python
from typing import Union

value: Union[int, str, float] = 42
```

`Union[int, str, float]` means the value may be an `int`, `str`, or `float`.

## `Optional`

```python
from typing import Optional

last_name: Optional[str] = None
```

`Optional[str]` is shorthand for `Union[str, None]` — the value may be a `str` or `None`.

## `Any`

```python
from typing import Any

value: Any = 42
value = "hello"
```

`Any` means the value may be of any type. Use it sparingly — it reduces the benefits of static type checking.

---

## Container Type Hints

```python
from typing import List, Dict

numbers: List[int] = [10, 20, 30]

prices: Dict[str, float] = {
    "apple": 1.5,
    "orange": 2.0,
}
```

Other aliases from `typing`: `Tuple`, `Set`, `FrozenSet`, `Sequence`, `Mapping`, `ByteString`.

- `Sequence` — any sequence type (list, tuple, etc.)
- `Mapping` — any mapping type (dict, etc.)

These broader types are useful when a function doesn't require a specific concrete container.

---

## Modern Syntax (Python 3.10+)

Python 3.10 introduced the `|` operator for unions:

```python
value: int | str = 42
name: str | None = None
```

Python 3.9+ allows built-in generics directly:

```python
numbers: list[int] = [1, 2, 3]
prices: dict[str, float] = {"apple": 1.5}
```

The `typing` module versions (`List`, `Dict`, `Union`, `Optional`) are still valid and needed for backward compatibility, but new code can use the shorter built-in syntax.

---

## Backporting Type Hints (older Python)

For Python versions before 3.5, use comment-based hints:

```python
spam = 42  # type: int

def add_two_numbers(numbers, double_sum):
    # type: (List[float], bool) -> float
    ...
```

Less readable than modern syntax — use only when supporting older versions requires it.

---

## Comparison: Comments vs. Docstrings vs. Type Hints

```python
# Use cents internally to avoid floating-point money calculations.
DEFAULT_QUANTITY: int = 1


def calculate_total(price: float, quantity: int) -> float:
    """Return the total price for a product."""
    return price * quantity
```

- **Comment** — explains a design reason (WHY)
- **Type hints** — describe expected data types
- **Docstring** — describes the function's purpose

These tools provide different information and work together.

---

## Key Takeaways

- Comments should explain WHY, not WHAT.
- Summary comments help readers scan large files quickly.
- Lessons-learned comments preserve knowledge that is not obvious from the code.
- Docstrings are accessible through `__doc__` and `help()`.
- Python does not enforce type hints at runtime — they are for static tools and readers.
- `Union` handles multiple possible types; `typing` provides container aliases.
- The goal of all three tools is **maintainability**.
