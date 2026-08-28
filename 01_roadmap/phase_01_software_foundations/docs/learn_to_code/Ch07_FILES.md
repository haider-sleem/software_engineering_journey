## Chapter 7: Files

### 1. File Modes

When opening a file, you specify a mode to tell Python how you want to use it.

| Mode | Behavior |
|---|---|
| `'r'` (Read) | Opens the file for reading. The file must exist, or Python raises an error. |
| `'w'` (Write) | Opens the file for writing. Creates the file if it does not exist. If it already exists, it overwrites all previous content. |
| `'a'` (Append) | Opens the file for writing. Adds new data to the end of the file without deleting existing content. |

---

### 2. Viewing Raw Content: `repr()`

`repr()` returns a representation of an object that makes special characters and other details visible.

Unlike `print()`, which executes special characters (like `\n` creating a new line), `repr()` displays them explicitly so you can see them.

**Example:**
```python
text = "12 13\n"
print(text)  # Prints: 12 13
# (blank line)
print(repr(text))  # Prints: '12 13\n'
```

**Why it is useful:** `repr()` is a great tool for debugging and verifying exactly what is inside your string.

---

### 3. Best Practice: Open and Close Files

Close files after you finish using them to release the file resource and ensure buffered data is properly handled.

---

### 4. Advanced File Modes (`+` Modes)

Adding a `+` to the file opening mode (`r+`, `w+`, `a+`) enables both reading and writing simultaneously.

| Mode | Behavior |
|---|---|
| `r+` | Opens for reading and writing. Does not clear existing content. The pointer starts at the beginning of the file. |
| `w+` | Opens for reading and writing. **Clears** the entire file content upon opening. |
| `a+` | Opens for reading and writing. Does not clear existing content. Writing always occurs at the end of the file. |

---

### Useful Python Tips for Competitive Programming

#### 1. The `abs()` Function

`abs()` returns the absolute value of a number. It converts negative numbers to their positive equivalent.

**Why it is useful:** In many problems, you need to calculate the distance between two points on a number line. Since distance is always positive, `abs(x - y)` ensures you get the correct result regardless of which number is larger.

**Example:**
```python
abs(3 - 6)  # Output: 3
abs(6 - 3)  # Output: 3
```

#### 2. Using `min()` and `max()` for Comparison

When you need to find the range between two points without using complex `if-else` statements, you can use these built-in functions:

- `min(x, y)` → Returns the smaller of the two numbers
- `max(x, y)` → Returns the larger of the two numbers

**Why it is useful:** It makes your code cleaner and helps you define boundaries without worrying about the order of the variables.

**Example:** Check if a point `target` is between `x` and `y`:
```python
if min(x, y) <= target <= max(x, y):
    # target is between x and y
```

---

### 3. The `all()` Function

`all()` checks if all values in an iterable are `True`.

| Case | Return Value |
|---|---|
| All values are `True` | `True` |
| Any value is `False` | `False` |

**Example:**
```python
all(x > 0 for x in numbers)
```
Meaning: "Are all numbers greater than zero?"

**Important:**
- `all()` stops as soon as it finds the first `False`, making it efficient.
- It is often used in Problem Solving to check whether a condition is true for all items or cases.

---

### Python Collection Methods: Quick Reference

#### 1. List Methods (Ordered & Mutable)

Lists store multiple items in order and allow duplicates.

| Method | Purpose | Example |
|---|---|---|
| `append(item)` | Adds a single element to the end of a list | `[1, 2].append(3)` → `[1, 2, 3]` |
| `extend(iterable)` | Adds multiple elements to the end of a list | `[1, 2].extend([3, 4])` → `[1, 2, 3, 4]` |

---

#### 2. Set Methods (Unordered & Unique)

Sets store unique elements. They are highly optimized for membership testing and mathematical operations.

| Method | Purpose | Example |
|---|---|---|
| `add(item)` | Adds a single element. Does nothing if already present. | `{1, 2}.add(3)` → `{1, 2, 3}` |
| `update(iterable)` | Adds multiple elements. Handles duplicates automatically. | `{1, 2}.update([3, 4])` → `{1, 2, 3, 4}` |
| `isdisjoint(other)` | Returns `True` if two sets share no common elements. | `{1, 2}.isdisjoint({3, 4})` → `True` |

---

#### 3. Pro-Tip: Comprehensions

Instead of using a `for` loop to build a list or set, use **Comprehension** for cleaner and clearer code.

| Type | Syntax |
|---|---|
| List Comprehension | `[x for x in data]` |
| Set Comprehension | `{x for x in data}` |

> **Why use Sets?** Sets are especially useful when you need fast membership testing.

---

## Quick Summary

| Concept | Key Point |
|---|---|
| `'r'` | Read — file must exist |
| `'w'` | Write — creates or overwrites |
| `'a'` | Append — adds to the end |
| `repr()` | Shows raw string content (good for debugging) |
| `abs()` | Returns absolute value |
| `min()` / `max()` | Cleaner comparison without `if-else` |
| `all()` | Checks if all items are `True` |
| Lists | Ordered, allow duplicates |
| Sets | Unordered, unique, fast membership testing |

