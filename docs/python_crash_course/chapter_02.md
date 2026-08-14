# Chapter 2: Strings & Numbers

> *Python Crash Course*

---

## Strings

### Updating Variables

- Any variable can be reassigned to a new value at any time.
- Each `print()` statement uses the current value of the variable at the moment it runs.

### Text Formatting Methods

| Method | Effect |
|--------|--------|
| `.title()` | Capitalizes the first letter of each word |
| `.upper()` | Converts all characters to uppercase |
| `.lower()` | Converts all characters to lowercase |

### Concatenation

Use `+` to combine strings. Add `" "` between words when needed:

```python
full_name = first_name + " " + last_name
```

### Whitespace

- `\t` — horizontal tab
- `\n` — new line

| Method | Effect |
|--------|--------|
| `.strip()` | Removes leading and trailing whitespace |
| `.lstrip()` | Removes leading whitespace only |
| `.rstrip()` | Removes trailing whitespace only |

```python
favorite_language = favorite_language.strip()
```

### Quotes Inside Strings

Use double quotes `"` to include apostrophes, or single quotes `'` to include double quotes:

```python
message = "It's a great day."
```

---

## Numbers

### Underscores in Large Numbers

Use `_` as a visual separator — Python ignores it:

```python
population = 14_000_000_000  # same as 14000000000
```

### Arithmetic Operators

| Operator | Meaning | Note |
|----------|---------|------|
| `+` | Addition | — |
| `-` | Subtraction | — |
| `*` | Multiplication | — |
| `/` | Division | always returns `float` |
| `//` | Integer division | drops the remainder |
| `**` | Exponentiation | — |

### Multiple Assignment

Assign multiple variables in one line:

```python
x, y, z = 0, 0, 0
first_name, last_name, country = "Haider", "Sleem", "Egypt"
```

### Constants

By convention, write constants in all caps:

```python
MAX_CONNECTIONS = 5000
```

Python does not enforce constants — this is a naming convention only.

---

## Additional String & Path Utilities

> **Note:** These are string and path methods — not file reading or writing operations.

### Removing Extensions

```python
import os

name = os.path.splitext("report.pdf")[0]  # → "report"
```

### Removing Prefixes and Suffixes

```python
url = "https://example.com/"
clean = url.removeprefix("https://").removesuffix("/")  # → "example.com"
```

- `.removeprefix("prefix")` — removes a specific string from the start.
- `.removesuffix("suffix")` — removes a specific string from the end.
- Both can be chained in one line.