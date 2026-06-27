## Notes on File Handling and Debugging
1. File Modes: open(filename, mode)

'r' (Read): Used to open a file for reading. The file must exist, or Python will throw an error.

'w' (Write): Used to open a file for writing. If the file doesn't exist, Python creates it. If it already exists, it overwrites (deletes) all its previous content.

'a' (Append): Used to add new data to the end of an existing file without deleting its current content.

2. Viewing Raw Content: repr()

repr(string): This function returns the "raw" or "internal" representation of a string.

Unlike print(), which executes special characters (like \n creating a new line), repr() displays them explicitly so you can see them (e.g., it shows '12 13\n' instead of just printing the numbers and jumping to a new line). It is a great tool for debugging and verifying exactly what is inside your string.


3. Open files when needed and close them immediately to ensure data safety and efficient memory usage.

---

4. Advanced File Modes (`+` Modes)

Adding a `+` to the file opening mode (`r+`, `w+`, `a+`) enables both reading and writing simultaneously. The core behavior still depends on the original mode:

* **`r+`**: Opens for reading and writing without clearing the file content. The pointer starts at the beginning of the file.
* **`w+`**: Opens for reading and writing but clears the entire file content upon opening.
* **`a+`**: Opens for reading and writing without clearing the content. Writing always occurs at the end of the file.

The `+` sign does not change the original mode's behavior regarding clearing content or pointer position; it simply adds the missing capability (either reading or writing).

---


### Useful Python Tips for Competitive Programming

#### 1. The `abs()` Function

The `abs()` function stands for **absolute value**. It converts any negative number into its positive counterpart and leaves positive numbers unchanged.

* **Why it's useful:** In many problems, you need to calculate the distance between two points on a number line. Since distance is always positive, `abs(x - y)` ensures you get the correct result regardless of which number is larger.
* **Example:** `abs(3 - 6)` returns `3`, and `abs(6 - 3)` also returns `3`.

#### 2. Using `min()` and `max()` for Comparison

When you need to find the range between two points (`x` and `y`) without using complex `if-else` statements to check which one is larger, you can use these built-in functions:

* **`min(x, y)`:** Returns the smaller of the two numbers.
* **`max(x, y)`:** Returns the larger of the two numbers.
* **Why it's useful:** It makes your code cleaner and helps you define boundaries (like checking if a value lies between two points) without worrying about the order of the variables.
* **Example:** If you want to check if a point `target` is between `x` and `y` and you don't know which one is bigger, you can simply write: `if min(x, y) <= target <= max(x, y):`.

---

### `all()` Function

* `all()` checks if all values in an iterable are `True`.
* It returns `True` if every value is `True`.
* It returns `False` if it finds any `False` value.

Example:

```python
all(x > 0 for x in numbers)
```

Meaning:
"Are all numbers greater than zero?"

Important:

* `all()` stops as soon as it finds the first `False`.
* This makes it efficient.
* It is often used in Problem Solving to check if a condition is true for all items, sessions, or cases.


---
# Python Collection Methods: Quick Reference

This guide covers essential methods for Python **Lists** and **Sets**, focusing on how to manipulate data efficiently.

## 1. List Methods (Ordered & Mutable)

Lists are used to store multiple items in a single variable. They maintain order and allow duplicates.

### `append(item)`

Adds a single element to the **end** of a list.

* **Example:**
```python
my_list = [1, 2]
my_list.append(3)  # Result: [1, 2, 3]

```



### `extend(iterable)`

Adds multiple elements (from a list, set, etc.) to the end of a list.

* **Example:**
```python
my_list = [1, 2]
my_list.extend([3, 4])  # Result: [1, 2, 3, 4]

```



---

## 2. Set Methods (Unordered & Unique)

Sets are collections of unique elements. They are highly optimized for membership testing and mathematical operations.

### `add(item)`

Adds a single element to the set. If the element already exists, nothing happens.

* **Example:**
```python
my_set = {1, 2}
my_set.add(3)  # Result: {1, 2, 3}

```



### `update(iterable)`

Adds multiple elements to the set. It automatically handles duplicates.

* **Example:**
```python
my_set = {1, 2}
my_set.update([3, 4, 5])  # Result: {1, 2, 3, 4, 5}

```



### `isdisjoint(other_set)`

Returns `True` if two sets have **zero elements in common**. It is the most efficient way to check for intersection.

* **Example:**
```python
set_a = {1, 2}
set_b = {3, 4}
print(set_a.isdisjoint(set_b))  # Result: True (No common items)

```



---

## 3. Pro-Tip: Comprehensions

Instead of using a `for` loop to build a list or set, you can use **Comprehension** for cleaner and faster code.

* **List Comprehension:** `[x for x in data]`
* **Set Comprehension:** `{x for x in data}`

> **Why use Sets?** Sets use hash tables, making operations like `isdisjoint` or checking `if item in my_set` extremely fast compared to searching through a list.

---

 