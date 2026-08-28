# CS50P — Lecture 3: Exceptions

---

## Exception Handling Basics

- Always catch **specific** exceptions (e.g., `except ValueError:`) — never use a bare `except:`, which catches everything including system exits and `NameError`s from typos, hiding real bugs.
- Keep the `try` block as **small as possible** — only include lines that can directly raise the target exception.
- Catching exceptions prevents ugly tracebacks and lets programs fail gracefully.

---

## Variable Binding and Scope

- In `x = expression`, the right-hand side is **fully evaluated before** binding the value to `x`.
- If the right-hand side raises an exception, the binding step is skipped — `x` remains undefined.
- Accessing an undefined variable raises a `NameError`.

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    pass
# If ValueError was raised, x is undefined here — accessing it would cause NameError
```

- Python has **no block scope** for `try/except`. A variable defined inside `try` is accessible outside it — but only if the assignment completed successfully.

---

## `try / except / else`

| Block | When it runs |
|-------|-------------|
| `try` | Always attempted |
| `except` | Only if `try` raised the specified exception |
| `else` | Only if `try` completed without any exception |

Use `else` to separate code that depends on a successfully bound variable from the error-handling logic:

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Not a valid integer.")
else:
    print(f"x is {x}")  # safe — x is guaranteed to be defined here
```

---

## Loops and Input Validation

```python
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass  # silently ignore and re-prompt
```

- `while True` creates an intentional infinite loop — runs until valid input is received.
- `break` can be placed in the `else` block (runs only on success) or directly after the risky line inside `try` (same effect).
- `pass` keeps the program running silently — cleaner UI, but users may not understand why they're being re-prompted.

---

## Design Principles

**EAFP vs LBYL**

| Style | Meaning | Python preference |
|-------|---------|-----------------|
| EAFP | Easier to Ask Forgiveness than Permission — use `try/except` | ✅ Preferred |
| LBYL | Look Before You Leap — use `if/else` to check first | Less idiomatic |

**Encapsulation** — handling exceptions inside a function hides errors from the caller and keeps the main flow clean.

**Dynamic functions** — pass parameters (e.g., a custom prompt string) instead of hard-coding values, to maximize reusability.

**Intentional design** — every line should be a deliberate decision. Never leave code in place just because "it works."

---

## Common Built-in Exceptions

| Exception | Raised when |
|-----------|------------|
| `SyntaxError` | Code has invalid Python syntax |
| `NameError` | A variable or name is used before being defined |
| `ValueError` | A function receives an argument of the right type but wrong value |