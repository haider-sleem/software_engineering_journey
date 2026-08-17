# CS50P — Week 1: Conditionals
> Decision-making in Python — Organized Study Notes

---

## Table of Contents

1. [Boolean Expressions](#1-boolean-expressions)
2. [Comparison Operators](#2-comparison-operators)
3. [Logical Operators](#3-logical-operators)
4. [if / elif / else](#4-if--elif--else)
5. [Modulo Operator](#5-modulo-operator)
6. [Boolean Functions](#6-boolean-functions)
7. [match Statement](#7-match-statement)
8. [Code Design & Refactoring](#8-code-design--refactoring)
9. [Backend Connection](#9-backend-connection)
10. [Quick Reference](#10-quick-reference)

---

## 1. Boolean Expressions

A **Boolean expression** is any expression that evaluates to exactly one of two values:

```python
True
False
```

Every condition inside an `if` statement is a Boolean expression.

```python
x < y  # True or False
x == y  # True or False
x != y  # True or False
```

---

## 2. Comparison Operators

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `>` | Greater than | `x > y` |
| `>=` | Greater than or equal | `x >= y` |
| `<` | Less than | `x < y` |
| `<=` | Less than or equal | `x <= y` |

> ⚠️ **Critical distinction:**
> - `=` → **assignment** (stores a value)
> - `==` → **comparison** (checks equality)
>
> ```python
> x = 5      # assigns 5 to x
> x == 5     # checks if x equals 5 → True or False
> ```

### Chained Comparisons

Python allows chaining comparison operators — a cleaner alternative to using `and`.

```python
# Instead of this:
score >= 80 and score < 90

# Write this:
80 <= score < 90

# Or this:
90 <= score <= 100
```

---

## 3. Logical Operators

### `and`

All conditions must be `True`.

```python
if score >= 90 and score <= 100:
    print("A")
```

### `or`

At least one condition must be `True`.

```python
if name == "Harry" or name == "Ron":
    print("Gryffindor")
```

### `not`

Inverts the Boolean value.

```python
if not is_authenticated:
    print("Access denied")
```

### Prefer simpler conditions when possible

```python
# Instead of:
if x < y or x > y:
    print("Not equal")

# Write:
if x != y:
    print("Not equal")
```

---

## 4. if / elif / else

### Syntax

```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

> - Every conditional line ends with a **colon** `:`
> - The **indented block** below it belongs to that condition
> - Python skips all remaining branches once one condition is `True`

### `if` only

Executes the block if the condition is `True`, skips it otherwise.

```python
if x < y:
    print("x is less than y")
```

### `elif`

Checked only if all previous conditions were `False`.

```python
if x < y:
    print("Less")
elif x > y:
    print("Greater")
```

### `else`

Runs when **all** previous conditions are `False`. No condition needed.

```python
if x < y:
    print("Less")
elif x > y:
    print("Greater")
else:
    print("Equal")  # no need to write: elif x == y
```

### `if` vs `elif` — Key difference

```python
# ❌ Multiple independent if — ALL are evaluated
if score >= 90:
    print("A")
if score >= 80:  # also runs even if score is 95
    print("B")

# ✅ elif — stops at the first True condition
if score >= 90:
    print("A")
elif score >= 80:  # skipped if score >= 90
    print("B")
```

> Use `elif` whenever the conditions are **mutually exclusive** (only one should run).

### Grade example — Refactored

```python
# ❌ Verbose — checks full range unnecessarily
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")

# ✅ Clean — earlier conditions already eliminate higher values
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

---

## 5. Modulo Operator

```python
%
```

Returns the **remainder** after division.

```python
5 % 2  # → 1   (5 divided by 2, remainder is 1)
6 % 2  # → 0   (6 divided by 2, no remainder)
10 % 3  # → 1   (10 divided by 3, remainder is 1)
```

**Common use:** detecting even or odd numbers.

```python
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 6. Boolean Functions

A function can return `True` or `False` directly.

### The Pythonic way

```python
# ❌ Unnecessary if/else
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# ✅ Return the expression directly
def is_even(n):
    return n % 2 == 0
```

The condition `n % 2 == 0` is already a Boolean expression — return it directly.

### Using a Boolean function

```python
if is_even(x):
    print("Even")
```

### Backend examples

```python
def is_authenticated(user):
    return user.token is not None


def is_admin(user):
    return user.role == "admin"


def has_permission(user, action):
    return action in user.permissions


def email_exists(email, db):
    return db.find_by_email(email) is not None
```

These functions return `True` or `False` and are used directly inside `if` statements — clean, readable, and reusable.

---

## 7. match Statement

An alternative to long `if / elif / else` chains when comparing one value against many options.

### Syntax

```python
match value:
    case "A":
        ...
    case "B":
        ...
    case _:  # default — like else
        ...
```

### Multiple values in one case

```python
match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Unknown")
```

This replaces:

```python
if name == "Harry" or name == "Ron" or name == "Hermione":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Unknown")
```

> Use `match` when you're comparing **one variable** against **many fixed values**.
> Use `if/elif` when your conditions involve ranges, calculations, or complex logic.

---

## 8. Code Design & Refactoring

**Refactoring** means rewriting code to improve its quality **without changing what it does**.

### What good code looks like

| Property | Meaning |
|---|---|
| **Simple** | Does only what is needed |
| **Readable** | Easy to understand at first glance |
| **Efficient** | Avoids unnecessary work |
| **Maintainable** | Easy to change later |

### Control flow

Python reads code **top to bottom**. Conditionals change which path is taken:

```
Start
  ↓
Evaluate condition
  ↓
True  → execute block → continue
False → skip block   → continue
  ↓
End
```

### Refactoring checklist

- Replace multiple independent `if` with `elif` when conditions are mutually exclusive.
- Remove unnecessary `else` when the previous `if` already covers the only other case.
- Simplify `if condition: return True else: return False` to `return condition`.
- Replace `score >= 80 and score < 90` with `80 <= score < 90`.
- Replace long `or` chains with `match` when checking one variable.

---

## 9. Backend Connection

Conditionals appear in **every** part of a backend application.

| Use case | Example |
|---|---|
| Authentication | Is the user logged in? |
| Authorization | Does the user have permission? |
| Input validation | Is the email format valid? |
| Business logic | Is the order amount above the minimum? |
| Error handling | Did the database query succeed? |
| Role-based access | Is the user an admin? |
| API decisions | Which response to return based on status? |

```python
# Real backend pattern
def process_request(user, action):
    if not is_authenticated(user):
        return 401  # Unauthorized

    if not has_permission(user, action):
        return 403  # Forbidden

    return 200  # OK
```

> Without conditionals, a backend application cannot make any decisions.

---

## 10. Quick Reference

### Conditional structure

```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

### Comparison operators

```python
==   !=   >   >=   <   <=
```

### Logical operators

```python
and    or    not
```

### Chained comparison

```python
80 <= score < 90  # instead of: score >= 80 and score < 90
```

### Pythonic Boolean return

```python
return n % 2 == 0  # instead of: if ... return True else return False
```

### match statement

```python
match value:
    case "x" | "y":
        ...
    case _:
        ...
```

### Modulo

```python
n % 2 == 0  # even
n % 2 != 0  # odd
```

---

## Key Rules to Remember

1. `=` assigns, `==` compares — never confuse them.
2. Use `elif` when only one branch should execute — not multiple `if`.
3. Use `else` when it's the only remaining possibility — no condition needed.
4. Return Boolean expressions directly — don't wrap them in `if/else`.
5. Prefer chained comparisons (`80 <= x < 90`) over `and`.
6. Use `match` when comparing one variable to many fixed values.
7. Good code is not just correct — it is simple, readable, and easy to maintain.