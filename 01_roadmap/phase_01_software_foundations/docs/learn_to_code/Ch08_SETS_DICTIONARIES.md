## Chapter 8: Sets & Dictionaries

> Learn to Code in Python · Study Notes

---

## Part 1: Sets

### What is a Set?

A set is a collection of **unique** values.

- No duplicate values — duplicates are removed automatically.
- Order is **not guaranteed** — never rely on the order of a set.
- Best for fast membership checking (the `in` operator).

```python
numbers = {1, 2, 3}
```

---

### Why Use a Set?

Use a set when you do **not** care about order, only whether a value exists.

- You need unique values only.
- You need fast membership testing.
- You want duplicates removed automatically.

```python
emails = set()
emails.add("a@gmail.com")
emails.add("a@gmail.com")  # duplicate — ignored

print(emails)  # {'a@gmail.com'}
```

---

### Set vs List

| Feature | List | Set |
|---|---|---|
| Order | Keeps insertion order | Order is NOT guaranteed |
| Duplicates | Allowed | Not allowed (auto-removed) |
| Indexing | Supported (`list[0]`) | Not supported |
| Membership testing (`in`) | O(n) average | O(1) average |

---

### Creating a Set

```python
numbers = {2, 4, 6}  # set with values
numbers = set()  # empty set
```

> ❌ **Warning:** `{}` creates a **dictionary**, NOT a set. Always use `set()` for an empty set.

---

### Duplicate Values

Duplicates are silently removed when a set is created.

```python
{1, 1, 2, 2, 3}  # becomes {1, 2, 3}
```

---

### Looping, Length, and Indexing

- Iterate with a `for` loop — order is not guaranteed.
- Use `len()` to count elements.
- Indexing (`numbers[0]`) is **NOT** supported — raises an error.

```python
for value in numbers:
    print(value)

len(numbers)  # number of elements
numbers[0]  # ❌ IndexError
```

---

### Mutable vs Immutable

A set itself is **mutable** (you can add/remove elements), but every **element inside** must be **immutable**.

```python
# ✅ Allowed — all elements are immutable
{1, "abc", (1, 2)}

# ❌ Not allowed — list is mutable
{[1, 2]}  # TypeError

# A list of sets is fine
data = [{1, 2}, {3, 4}]
```

---

## Part 2: Set Methods

### add()

Adds one element. If the value already exists, nothing happens.

```python
numbers = set()
numbers.add(5)
numbers.add(5)  # no effect
```

---

### remove()

Removes one element. Raises `KeyError` if the value does not exist.

```python
numbers.remove(5)  # OK
numbers.remove(99)  # KeyError!
```

---

### update()

Adds all elements from another iterable into the set. **Modifies** the original set.

```python
a = {1, 3}
b = {2, 3, 4}
a.update(b)

print(a)  # {1, 2, 3, 4}
```

> ⚠️ **Note:** `update()` modifies the original set directly.

---

### intersection()

Returns a **new** set containing only the elements common to both sets. Does **NOT** modify either set.

```python
a = {1, 2, 3}
b = {2, 3, 4}

common = a.intersection(b)
print(common)  # {2, 3}

# If you ignore the return value:
a.intersection(b)  # a is unchanged!
```

> ⚠️ **Note:** `intersection()` returns a **NEW** set. The original sets are not changed.

---

### isdisjoint()

Returns `True` if two sets share **no** common elements.

```python
a = {"A", "G"}
b = {"C"}

a.isdisjoint(b)  # True
```

---

### Modify vs Return — Key Distinction

| Method | Modifies Original? | Returns New Object? |
|---|---|---|
| `add()` | ✅ Yes | — |
| `remove()` | ✅ Yes | — |
| `update()` | ✅ Yes | — |
| `intersection()` | ❌ No | ✅ New set |
| `isdisjoint()` | ❌ No | ✅ bool |

---

### Exploring Methods

Two built-in tools for discovering what a type can do:

```python
dir(set())  # list all methods
print(set.add.__doc__)  # short description of add()
```

---

## Part 3: Dictionaries

### What is a Dictionary?

A dictionary stores **key → value** pairs. Each key maps to exactly one value.

- Keys must be **unique**. If repeated, the last value overwrites the previous one.
- Values can be duplicated.
- Keys must be **hashable** (for example, `int`, `str`, and tuples containing hashable elements).
- Values can be mutable or immutable.
- Since Python **3.7+**, dictionaries preserve **insertion order**.
- Two dictionaries are equal if they contain the same pairs, **regardless of order**.

```python
d = {"name": "Alex", "age": 30}

len(d)  # 2 — number of key-value pairs
{}  # empty dictionary
set()  # empty set (NOT the same!)
```

---

### Accessing Values

```python
d["name"]  # "Alex"
d["missing"]  # ❌ KeyError

d.get("name")  # "Alex"
d.get("missing")  # None
d.get("missing", 0)  # 0 (custom default)

"name" in d  # True (checks keys only, not values)
```

---

### Adding and Updating

```python
d["city"] = "Cairo"  # add new key
d["age"] = 31  # update existing key
```

---

### Looping Over a Dictionary

Looping with `for` returns **keys** by default.

```python
for key in d:  # same as d.keys()
    print(key, d[key])
```

---

### keys(), values(), items()

These return **view objects**, not lists. Convert if you need list operations.

```python
d.keys()  # dict_keys(["name", "age", "city"])
d.values()  # dict_values(["Alex", 31, "Cairo"])
d.items()  # dict_items([("name", "Alex"), ...])

# Convert to list when needed:
keys = list(d.keys())
keys.sort()  # dict_keys has no sort() method
```

> ℹ️ **Note:** `dict_keys`, `dict_values`, and `dict_items` are view objects. Convert to list only when you need sorting or indexing.

---

### items() and Tuples

Each element returned by `items()` is a `(key, value)` tuple.

```python
for pair in d.items():
    print(pair[0], pair[1])  # key, value

# Or unpack directly:
for key, value in d.items():
    print(key, value)
```

---

### Tuples — Quick Reference

- Syntax: `(1, 2, 3)` — parentheses, not square brackets.
- Similar to a list but **immutable** (cannot be modified after creation).
- Supports indexing, slicing, and iteration.
- A one-element tuple **must** have a trailing comma: `(4,)`

```python
(4)  # int — NOT a tuple
(4,)  # tuple with one element
```

---

## Part 4: Additional Notes

### 1. Fast Input (`sys.stdin.readline`)

Used in competitive programming when input is very large.

```python
import sys

input = sys.stdin.readline

# readline() keeps the newline, so strip it:
word = input().strip()
```

- Faster than the built-in `input()`.
- Rarely needed in backend development.

---

### 2. `ord()` Function

Converts a character to its Unicode code point.

```python
ord("a")  # 97
ord("é")  # 233
ord("A")  # 65

# Convert letter to zero-based index:
index = ord(ch) - ord("a")
# "a" → 0, "b" → 1, ..., "z" → 25
```

---

### 3. Strings as Lookup Tables

A fixed string can replace a dictionary when values follow a predictable order.

```python
KEYS = "22233344455566677778889999"

# Get the T9 key for any letter:
KEYS[ord(ch) - ord("a")]
```

> ℹ️ **Note:** Very fast and common in competitive programming. Prefer a dictionary when readability matters more than performance.

---

### 4. `find()` Method

Searches for a substring inside a string. Returns the **index of the first match**, or **-1** if not found.

```python
text = "hello cow"

text.find("cow")  # 6 — found at index 6
text.find("milk")  # -1 — not found (no crash)
```

- Unlike `index()`, `find()` does **not** raise an error when the substring is missing.

---

### 5. `join()` vs String Concatenation

Repeated string concatenation with `+=` can be inefficient because strings are immutable. Using `join()` is generally the preferred approach when building a string from multiple pieces.

```python
# ❌ Can be inefficient
result = ""
for ch in word:
    result += convert(ch)

# ✅ Preferred approach
result = "".join(convert(ch) for ch in word)
```

---

### 6. Avoid Repeated `replace()` Inside Loops

`replace()` returns a new string because strings are immutable. Repeated `replace()` calls inside a loop can therefore create unnecessary intermediate strings. Process each character once and build with `join()` instead.

```python
# ❌ Creates unnecessary intermediate strings
for ch in letters:
    word = word.replace(ch, value)

# ✅ Process each character exactly once
result = "".join(mapping.get(ch, ch) for ch in word)
```

---

### 7. Generator Expression

A generator expression does not build the entire result list in memory at once.

```python
sum(1 for word in words if len(word) == 4)
```

- Uses less memory than a list comprehension in typical cases.
- Works naturally with `sum()`, `any()`, `all()`, `max()`, and `min()`.

---

### 8. List Comprehension

Builds a list in one readable line.

```python
words = [input().strip() for _ in range(n)]

# Equivalent to:
words = []
for _ in range(n):
    words.append(input().strip())
```

---

### 9. Choosing the Right Data Structure

Ask yourself these questions before writing code:

- Do I care about **order**?
- Do I need **duplicate** values?
- What operation do I perform **most often**?

| Need | Best Structure |
|---|---|
| Fast membership testing / unique values | `set` |
| Key → value mapping | `dict` |
| Ordered collection with duplicates | `list` |
| Immutable ordered sequence | `tuple` |

---

### 10. Readability vs Cleverness

Always prefer code that is easy to understand. A clever one-liner is not always better.

1. Correct
2. Readable
3. Maintainable

*Choose the simplest solution that solves the problem correctly.*

---

### 11. Character Mapping Design

Choose your mapping direction based on what you **search for most often**.

```python
# If you look up by cipher character:
cipher_to_plain = {"U": "T", "I": "H", ...}

# If you look up by plain character:
plain_to_cipher = {"T": "U", "H": "I", ...}
```

*Good mapping design makes code simpler, faster, and easier to read.*


