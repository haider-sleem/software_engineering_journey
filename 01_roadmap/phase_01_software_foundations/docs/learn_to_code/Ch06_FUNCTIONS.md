## Chapter 6: Functions

### 1. Function Basics

- **`def` keyword:** Use it to create (define) a function.
- **Calling a function:** Write its name followed by parentheses: `my_function()`.
- **How it works:** Defining a function stores the code in memory. The code only runs when you **call** the function.

---

### 2. Parameters vs. Arguments

| Term | Meaning | Example |
|---|---|---|
| **Parameter** | The variable name inside the function definition | `def add(x, y):` → `x` and `y` are parameters |
| **Argument** | The actual value you pass when calling the function | `add(3, 5)` → `3` and `5` are arguments |

**Simple rule:** Parameters are placeholders. Arguments are the real values.

---

### 3. Argument Rules

You can pass arguments in two ways:

1. **Positional arguments:** Matched by order.
```python
greet("Ahmed", "Python")  # First argument = name, second = language
```

2. **Keyword arguments:** Matched by name.
```python
greet(language="Python", name="Ahmed")
```

**⚠️ Important rule:** Always put **positional arguments before keyword arguments**.

| Example | Valid? |
|---|---|
| `greet("Ahmed", language="Python")` | ✅ Correct |
| `greet(name="Ahmed", "Python")` | ❌ Wrong |

---

### 4. Local Variables and Scope

- A local variable can be accessed **only inside the function** where it is defined.
- It does **not** affect variables outside the function, even if they have the same name.

**Example:**
```python
x = 10  # Global variable


def my_func():
    x = 5  # Local variable (different from the global one)
    print(x)  # Prints 5


my_func()
print(x)  # Still prints 10 (global unchanged)
```

---

### 5. Mutable Parameters (Lists, Dictionaries, Sets)

When you pass a mutable object to a function, the parameter refers to the same object as the argument. Mutating that object inside the function affects the original object.

**Example:**
```python
numbers = [1, 2, 3]


def add_one(lst):
    lst.append(4)  # This changes the original list


add_one(numbers)
print(numbers)  # [1, 2, 3, 4]  ← changed!
```

---

### 6. Reassignment vs. Mutation

| Operation | Effect on Original | Example |
|---|---|---|
| **Reassignment (`=`)** | ❌ No effect. The original outside stays the same. | `lst = [10, 20, 30]` |
| **Mutation (`.append()`, `.remove()`)** | ✅ Yes. The original is updated. | `lst.append(4)` |

**Example of reassignment (no outside effect):**
```python
numbers = [1, 2, 3]


def change(lst):
    lst = [10, 20, 30]  # Reassigns local variable only


change(numbers)
print(numbers)  # Still [1, 2, 3]  ← unchanged!
```

**Example of mutation (outside effect):**
```python
numbers = [1, 2, 3]


def change(lst):
    lst.append(4)  # Mutates the original list


change(numbers)
print(numbers)  # [1, 2, 3, 4]  ← changed!
```

---

### 7. Return Values

- Use the `return` keyword to send a value back to the caller.
- `return` also **immediately stops** the function (nothing after it runs).
- If you don't write a `return`, the function returns `None`.

**Example:**
```python
def add(a, b):
    return a + b
    print("This never runs")  # ignored


result = add(3, 5)
print(result)  # 8
```

---

### 8. `return` as a "Super-Break"

- `break` only exits a loop.
- `return` exits **the entire function**, even from inside multiple nested loops.

**Example:**
```python
def find_first_negative(numbers):
    for row in numbers:  # outer loop
        for num in row:  # inner loop
            if num < 0:
                return num  # exits both loops AND the function
    return None
```

---

### 9. The `find()` Method

The `find()` method searches for a specific substring within a string.

#### Syntax
```python
string.find(substring, start, end)
```

#### Parameters

| Parameter | Required? | Description |
|---|---|---|
| `substring` | ✅ Required | The text you are looking for |
| `start` | ❌ Optional | The index where the search should begin |
| `end` | ❌ Optional | The index where the search should stop |

#### Return Values

| Case | Return Value |
|---|---|
| Substring found | Index of its first occurrence |
| Substring not found | `-1` |

#### Examples

**1. Basic Search:**
```python
text = "hello world"
print(text.find("world"))  # Output: 6
```

**2. Search with a Start Index:**
```python
text = "banana"
print(text.find("a", 2))  # Output: 3
```

**3. Handling Not Found:**
```python
text = "hello"
print(text.find("z"))  # Output: -1
```

#### Why Use `find()`?

It is useful when you need to know **where** a specific pattern exists in a text, or to check if a pattern exists (by checking if the result is not `-1`).

---

### Programming Concepts: Functions & Top-Down Design

#### 1. The Power of Functions

A function is a self-contained block of code that solves one specific task.

**Three key ideas:**

- **Encapsulation:** A function groups related code into one unit.
- **Independence:** A good function depends mainly on its inputs and produces a clear output, making it easier to reuse and test.
- **Black Box Principle:** You can use a function without needing to know how its internal code works.

---

#### 2. Top-Down Design (How to Solve Big Problems)

This is a method for building programs:

1. **Decomposition:** Break a large problem into smaller, manageable tasks.
2. **Task Management:** Solve each small task directly or write a function for it.
3. **Readability:** Your main program becomes a simple "to-do list" of function calls.

**Example:**
```python
def main():
    get_user_data()
    process_data()
    show_results()
    # Much cleaner than writing all the code here!
```

---

### Key Python Techniques from Practice

| Technique | What it means |
|---|---|
| `split()` | Breaks a string into a list |
| `map()` | Applies a function to every item in a list |
| `pop(0)` | Removes and returns the first element of a list |
| `sort()` | Arranges list items in order |
| **Adjacent Comparison** | Comparing an element with its neighbor (`list[i]` vs `list[i+1]`) |
| **Cumulative Tracking** | Using a variable (like `maximum`) to track progress while looping |

---

### Engineering Mindset: Thinking Like a Programmer

| Old Way | Better Way |
|---|---|
| "Does my code work?" | "Does my code work correctly, and can it be made clearer, simpler, or more maintainable?" |
| Writing isolated lines | Building a structured system |
| One big messy solution | Clean functions with one job each |

**Real progress:** Successfully improved a solution from **5 functions** down to **3 functions** (without losing functionality). That is real engineering.

---

## Quick Summary — One Sentence Each

| Concept | Summary |
|---|---|
| **Function definition** | Use `def` to create a reusable block of code |
| **Parameter vs. Argument** | Parameter = placeholder. Argument = real value |
| **Local variable** | Can only be accessed inside the function where it is defined |
| **Mutable parameter** | Changes inside the function affect the original object |
| **Reassignment (`=`)** | Does NOT affect the original object |
| **Mutation (`.append()`)** | DOES affect the original object |
| **`return`** | Sends a value back and exits the function |
| **Top‑down design** | Break big problems into small tasks, then write functions |
| **`string.find()`** | Searches for a substring and returns its index, or `-1` if not found |

