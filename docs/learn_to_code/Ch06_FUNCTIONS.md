# Chapter 6: Functions – Simple Notes

## 1. Function Basics

- **`def` keyword:** Use it to create (define) a function.
- **Calling a function:** Write its name followed by parentheses: `my_function()`.
- **How it works:** Defining a function stores the code in memory. The code only runs when you **call** the function.

## 2. Parameters vs. Arguments (Important!)

Parameter vs. Argument

1. Parameter: This is the variable name you write inside the function definition.

Example: In def add(x, y): the words x and y are parameters.

2. Argument: This is the actual value you pass when you call the function.

Example: In add(3, 5) the numbers 3 and 5 are arguments.

Simple rule: Parameters are placeholders. Arguments are the real values.

## 3. Argument Rules

You can pass arguments in two ways:

1.  **Positional arguments:** Matched by order.
    ```python
    greet("Ahmed", "Python")  # First argument = name, second = language
    ```

2.  **Keyword arguments:** Matched by name.
    ```python
    greet(language="Python", name="Ahmed")
    ```

**⚠️ Important rule:** Always put **positional arguments before keyword arguments**.  
✅ Correct: `greet("Ahmed", language="Python")`  
❌ Wrong: `greet(name="Ahmed", "Python")`

## 4. Local Variables

- Any variable **created inside a function** is local.
- It **only exists while the function runs**.
- It does **not** affect variables outside the function, even if they have the same name.

**Example:**
```python
x = 10          # Global variable

def my_func():
    x = 5       # Local variable (different from the global one)
    print(x)    # Prints 5

my_func()
print(x)        # Still prints 10 (global unchanged)
```

## 5. Mutable Parameters (Lists, Dictionaries, Sets)

When you pass a **mutable object** (like a list) to a function:

- The function gets a **reference** to the original object.
- Changes **inside** the function (like `.append()` or `.remove()`) **affect the original** outside.

**Example:**
```python
numbers = [1, 2, 3]

def add_one(lst):
    lst.append(4)      # This changes the original list

add_one(numbers)
print(numbers)         # [1, 2, 3, 4]  ← changed!
```

## 6. Reassignment vs. Mutation (Very Important!)

Reassignment vs. Mutation

* Reassignment (=): This changes what the local variable points to.

Does it affect the original outside? ❌ No. The original outside stays the same.

* Mutation (.append(), .remove(), etc.): This changes the internal content of the object.

Does it affect the original outside? ✅ Yes. The original is updated.

**Example of reassignment (no outside effect):**
```python
numbers = [1, 2, 3]

def change(lst):
    lst = [10, 20, 30]   # Reassigns local variable only

change(numbers)
print(numbers)           # Still [1, 2, 3]  ← unchanged!
```

**Example of mutation (outside effect):**
```python
numbers = [1, 2, 3]

def change(lst):
    lst.append(4)        # Mutates the original list

change(numbers)
print(numbers)           # [1, 2, 3, 4]  ← changed!
```

## 7. Return Values

- Use the `return` keyword to send a value back to the caller.
- `return` also **immediately stops** the function (nothing after it runs).
- If you don't write a `return`, the function returns `None`.

**Example:**
```python
def add(a, b):
    return a + b
    print("This never runs")   # ignored

result = add(3, 5)
print(result)                  # 8
```

## 8. `return` as a "Super-Break"

- `break` only exits a loop.
- `return` exits **the entire function**, even from inside multiple nested loops.

**Example:**
```python
def find_first_negative(numbers):
    for row in numbers:           # outer loop
        for num in row:           # inner loop
            if num < 0:
                return num        # exits both loops AND the function
    return None
```

---

# Programming Concepts: Functions & Top-Down Design

## 1. The Power of Functions

A function is a self-contained block of code that solves one specific task.

**Three key ideas:**


* Encapsulation: Functions take inputs (parameters) and produce outputs (return values).

* Independence: Good functions don't rely on global variables. They are reusable and easy to test.

* Black Box Principle: A function should work using only its inputs, not external variables.


## 2. Top-Down Design (How to solve big problems)

This is a method for building programs:

1.  **Decomposition:** Break a large problem into smaller, manageable tasks.
2.  **Task Management:** Solve each small task directly or write a function for it.
3.  **Readability:** Your main program becomes a simple "to-do list" of function calls.

**Example:**
```python
def main():
    get_user_data()
    process_data()
    show_results()
    # Much cleaner than writing all the code here!
```

## 3. Key Python Techniques from Your Practice

| Technique | What it means |
|-----------|----------------|
| `split()` | Breaks a string into a list. |
| `map()` | Applies a function to every item in a list. |
| `pop(0)` | Removes and returns the first element of a list. |
| `sort()` | Arranges list items in order. |
| **Adjacent Comparison** | Comparing an element with its neighbor (`list[i]` vs `list[i+1]`). |
| **Cumulative Tracking** | Using a variable (like `maximum`) to track progress while looping. |

## 4. Engineering Mindset (Thinking Like a Programmer)


**Old Way vs. Better Way**

- **Old Way:** "Does my code work?"
  **Better Way:** "Is my code optimal?"

- **Old Way:** Writing isolated lines
  **Better Way:** Building a structured system

- **Old Way:** One big messy solution
  **Better Way:** Clean functions with one job each

---


**Real progress:** You successfully improved a solution from **5 functions** down to **3 functions** (without losing functionality). That is real engineering.

---

## Quick Summary Table for Review



# Python `find()` Method

The `find()` method is used to search for a specific substring within a string.

### Syntax

```python
string.find(substring, start, end)

```

### Parameters

* **`substring`** (Required): The text you are looking for.
* **`start`** (Optional): The index position where the search should begin.
* **`end`** (Optional): The index position where the search should stop.

### Return Values

* If the substring is **found**, it returns the **index** of its first occurrence.
* If the substring is **not found**, it returns **`-1`**.

---

### Simple Examples

#### 1. Basic Search

```python
text = "hello world"
print(text.find("world"))  # Output: 6

```

#### 2. Search with a Start Index

You can tell Python to skip the beginning of the string:

```python
text = "banana"
# Searching for 'a' starting from index 2
print(text.find("a", 2))  # Output: 3

```

#### 3. Handling Not Found

```python
text = "hello"
print(text.find("z"))      # Output: -1

```

### Why use `find()`?

It is very useful when you need to know **where** a specific pattern exists in a text or to check if a pattern exists at all (by checking if the result is not `-1`).

---

---

**Quick Summary - One Sentence Each**

- **Function definition:** Use `def` to create a reusable block of code.

- **Parameter vs. Argument:** Parameter = placeholder. Argument = real value.

- **Local variable:** Exists only inside the function.

- **Mutable parameter:** Changes inside the function affect the original.

- **Reassignment (`=`):** Does NOT affect the original object.

- **Mutation (`.append()`):** DOES affect the original object.

- **`return`:** Sends a value back and exits the function.

- **Top‑down design:** Break big problems into small tasks, then write functions.

- **`string.find()`:** Searches for a substring and returns its index, or `-1` if not found.

---


