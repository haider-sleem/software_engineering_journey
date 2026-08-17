# Chapter 10: Files and Exceptions

## Reading File Contents

### `read_text()`

- Reads the entire contents of a file and returns a single string.
- Files often end with `\n`, which can create an extra blank line when printing.

### `rstrip()`

- Removes trailing whitespace (including the final newline).
- Does not alter the main content.

### Method Chaining

```python
contents = path.read_text().rstrip()
```

Calls multiple methods in one statement — shorter and cleaner.

---

## Working with File Contents

### Combining Lines

- Read the entire file → split into lines → combine into one string for processing.

### Useful String Methods

- `lstrip()` — removes leading whitespace.
- `strip()` — removes both leading and trailing whitespace.
- `len()` — returns the number of characters in a string.

> **Important:** Data read from a file is always a string. Use `int()` or `float()` when numeric values are needed.

---

## Large Files

The same code works for any file size — only the filename changes.

```python
pi_string[:52]  # display only the first 52 characters
```

Python has no fixed file-size limit; the only constraint is available system memory.

---

## Searching File Contents

```python
if birthday in pi_string:
```

- The `in` keyword checks whether a substring exists inside a string.
- Returns `True` or `False`.

---

## Writing to a File

```python
path.write_text("Hello")
```

- Creates the file if it does not exist.
- **Overwrites** the file if it already exists — it does not append.
- Accepts strings only — use `str()` to convert other types first.

### Writing Multiple Lines

Build one string first, then write it once:

```python
contents = "Line 1\n"
contents += "Line 2\n"
contents += "Line 3\n"
path.write_text(contents)
```

---

## `try-except`

| Block | Purpose |
|-------|---------|
| `try` | Code that might raise an exception — keep it small |
| `except` | Handles a specific error; prevents a crash |
| `else` | Runs only if `try` succeeded |

```python
try:
    risky_operation()
except SomeError:
    handle_error()
else:
    use_result()
```

---

## Text Analysis with Files

```python
words = text.split()  # split on whitespace by default
num_words = len(words)  # count the words
```

**Best practices:**
- Wrap repeated logic in a function: `def count_words(path): ...`
- Use loops to process multiple files.
- Handle missing files with `try-except`.

---

## Failing Silently

Use `pass` to ignore non-critical errors and keep the program running:

```python
except FileNotFoundError:
    pass
```

- Show users only useful messages — hide tracebacks.
- Log important errors internally when needed.

---

## Storing Data with JSON

| Function / Method | What it does |
|-------------------|-------------|
| `json.dumps(obj)` | Converts a Python object → JSON string |
| `json.loads(s)` | Converts a JSON string → Python object |
| `Path.exists()` | Checks whether a file exists before reading |

- JSON is supported by most programming languages — a common format for sharing data.
- Use `exists()` before reading a file when the file might not be there yet.

---

## Refactoring

Refactoring means breaking working code into smaller functions, each with one clear job. This makes code easier to read, test, and extend.

### Step 1 — Move all logic into one function

```python
from pathlib import Path
import json


def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
```

This is cleaner, but `greet_user()` is still doing too many things at once.

### Step 2 — Extract `get_stored_username()`

```python
from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_username(path)

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
```

`get_stored_username()` has one job: retrieve a stored username or return `None`. This is good practice — a function should either return the expected value or `None`.

### Step 3 — Extract `get_new_username()`

```python
from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_username(path)

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
```

Each function now has a single, clear purpose. `greet_user()` only decides which message to print. `get_stored_username()` only reads. `get_new_username()` only writes. This compartmentalization is an essential part of writing clean, maintainable code.