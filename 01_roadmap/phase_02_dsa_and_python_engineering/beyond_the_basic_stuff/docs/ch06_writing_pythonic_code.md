# Chapter 6: Writing Pythonic Code

> *Beyond the Basic Stuff with Python — Al Sweigart*

---

## The Zen of Python (Tim Peters)

| Principle | Meaning |
|-----------|---------|
| Beautiful is better than ugly | Prioritize clean, readable, maintainable code |
| Explicit is better than implicit | Avoid hidden magic or obscure features |
| Simple is better than complex | Keep solutions straightforward |
| Complex is better than complicated | Manage necessary complexity rather than tangled code |
| Flat is better than nested | Avoid excessive hierarchies and deep nesting |
| Sparse is better than dense | Avoid unreadable one-liners; spread code out for clarity |
| Readability counts | Write with the human reader in mind |
| Practicality beats purity | Special cases aren't special enough to break rules — but pragmatism matters |
| Errors should never pass silently | Raise exceptions early to fail fast, unless explicitly silenced |
| Refuse the temptation to guess | Use critical thinking, not blind trial-and-error |
| There should be one — and preferably only one — obvious way to do it | Prefer the single clear, idiomatic approach |
| Now is better than never | Avoid paralysis — but never is often better than *right now* (avoid premature action) |
| If the implementation is hard to explain, it's a bad idea | Prefer implementations that are easy to explain |
| Namespaces are great | Use separate containers to prevent naming conflicts without needless categorization |

> The Zen of Python provides **guidelines, not absolute rules**.

---

## Indentation and Whitespace

- Python uses indentation to define code blocks instead of curly braces.
- Indentation determines scope and hierarchy, while other whitespace (such as spaces around operators) does not affect syntax.
- This eliminates debates about brace placement style found in other languages.

---

## Pythonic Idioms

### Loops

```python
# Use enumerate() instead of range(len())
for i, item in enumerate(my_list):
    print(i, item)
```

### File I/O

```python
# Always use 'with' — guarantees automatic resource cleanup
with open("file.txt") as f:
    data = f.read()
```

### None Checks

```python
# Use 'is None', not '== None'
if value is None:
    ...
```

### Boolean Checks

```python
# Avoid: if spam == True or if spam is True
# Use truthiness directly:
if spam:
    ...
if not spam:
    ...
```

### Strings

```python
# Raw strings for Windows paths and regex
path = r"C:\Users\name\file.txt"

# F-strings for embedding variables (Python 3.6+)
name = "Haider"
msg = f"Hello, {name}!"
```

For Python 3.6+ code, prefer f-strings for string interpolation.

### Direct Iteration

```python
# Iterate directly over the values you need — no index needed.
for item in my_list:
    print(item)
```

Use direct iteration when you do not need the index. Use `enumerate()` when you do.

---

## Dictionary Best Practices

```python
# Safe value retrieval — avoids KeyError when used instead of dict[key]
value = my_dict.get(key, default)

# Initialize a missing key before modifying
my_dict.setdefault(key, []).append(item)

# Auto-initialize with defaultdict
from collections import defaultdict

counts = defaultdict(int)
groups = defaultdict(list)

# Replace long if-elif chains with a lookup dict
actions = {"quit": quit_func, "go": go_func}
actions[command]()
```

> Dictionary lookups are O(1) on average because dictionaries use hash tables.

---

## Conditional Expressions (Ternary Operator)

```python
# Syntax: TrueValue if condition else FalseValue
result = "yes" if is_valid else "no"
```

- Python puts the condition **in the middle** — unlike most languages.
- Never use the old workaround `condition and val1 or val2` — it fails silently when `val1` is falsy (`0`, `False`, `None`, `""`).
- Avoid nesting conditional expressions — technically valid, practically unreadable.

---

## Variable Value Best Practices

```python
# Chain comparison operators
if 42 < spam < 99:
    ...

# Chain assignment operators — same value for multiple variables
spam = eggs = bacon = 0

# Use 'in' with a tuple instead of repeated 'or'
if val in ("a", "b", "c"):
    ...
```

Using `in` with a tuple of literal values is more readable and slightly faster than repeated `or` conditions.

---

## Tuple Unpacking (Multiple Assignment)

Tuple unpacking assigns **different values** to multiple variables in a single statement.

```python
# Unpack a tuple into named variables
name, price, quantity = "Keyboard", 750, 12

# Swap two variables without a temporary variable
a, b = b, a


# Unpack from any iterable — including function returns
def get_product():
    return "Mouse", 15.0


product_name, product_price = get_product()
```

- **Tuple unpacking** → different values to different names (`a, b = 1, 2`).
- **Chained assignment** → same value to different names (`a = b = 1`).
- Mixing them up is a common source of confusion for beginners.

---

## Shallow Copies

- `copy.copy()` creates a new outer list, but nested mutable objects are still shared.
- `[:]` also creates a shallow copy, but `copy.copy()` is more readable.
- Do not confuse a shallow copy with a completely independent deep copy.


