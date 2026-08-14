# Chapter 4: Lists — Part 2

> *Python Crash Course*

---

## List Comprehension

A concise way to build a list in one line:

```python
# Syntax
result = [expression for item in iterable]

# Example
squares = [value**2 for value in range(1, 11)]
```

- The output is always a list (note the square brackets).
- Cleaner and more readable than writing a full `for` loop.

---

## `range()` and Memory

`range()` does not store all values in memory at once — it generates each value only when needed. This makes it efficient for large sequences.

```python
# No memory wasted on 1,000,000 numbers
for i in range(1_000_000):
    process(i)

# Only now are all values stored in memory
numbers = list(range(1_000_000))
```

> `range()` is an **iterable object**, not a generator — but both share the idea of producing values on demand rather than storing them all at once.

---

## Slicing

Extract a portion of a list using `:` inside the brackets.

```python
players = ["Ali", "Omar", "Sara", "Nour", "Rami"]

print(players[0:3])  # first 3 → ['Ali', 'Omar', 'Sara']
print(players[1:4])  # index 1 to 3 → ['Omar', 'Sara', 'Nour']
print(players[:3])  # from start → ['Ali', 'Omar', 'Sara']
print(players[2:])  # to end → ['Sara', 'Nour', 'Rami']
print(players[-2:])  # last 2 → ['Nour', 'Rami']
```

### Looping Over a Slice

```python
for player in players[:3]:
    print(player)  # prints first 3 only
```

---

## Copying a List

Assigning a list with `=` creates a reference, not a copy — both variables point to the same list.

```python
# Wrong — both variables share the same list
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]  ← a was also changed
```

Use an empty slice `[:]` to create an independent copy:

```python
# Correct — independent copy
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)  # [1, 2, 3]  ← a unchanged
print(b)  # [1, 2, 3, 4]
```

---

## Tuples

A tuple is an **immutable** sequence — its elements cannot be changed after creation.

```python
dimensions = (200, 50)
print(dimensions[0])  # 200
```

- Written with `()` instead of `[]`.
- Trying to modify an element raises a `TypeError`.
- To "update" a tuple, reassign the variable entirely:

```python
dimensions = (400, 100)  # new tuple, not a modification
```

> Use tuples when a set of values should stay constant throughout the program.

---

## Personal Research Notes

> The following concepts are not covered in PCC Chapter 4 — added from external reading for broader context.

**Generators** — objects that produce values one at a time on demand, without storing them all in memory. Different from `range()`, which is a built-in iterable object.

**I/O Operations** — interactions with external devices (screen, keyboard, disk). CPU computations are thousands of times faster than I/O, which is why printing inside a large loop is slow.

**Scientific Notation** — Python represents very large floats using exponent notation: `5e11` = 500,000,000,000.

---

*Notes last updated: 2026-03-03*