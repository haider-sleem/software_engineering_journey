# Chapter 3: Lists

> *Python Crash Course*

---

## What Is a List?

A list is an ordered, mutable collection that stores multiple values in a single variable.

```python
names = ["Ali", "Omar", "Sara"]
```

| Property | Meaning |
|----------|---------|
| **Ordered** | Each element has an index, starting at `0` |
| **Mutable** | Can be modified after creation |
| **Allows duplicates** | The same value can appear more than once |
| **Mixed types** | Can hold strings, integers, and other types together |

---

## Indexing

- Positive index: `names[0]` → first element
- Negative index: `names[-1]` → last element, `names[-2]` → second to last

```python
names = ["Ali", "Omar", "Sara"]
print(names[0])  # Ali
print(names[-1])  # Sara
```

---

## Adding Elements

| Goal | Method |
|------|--------|
| Add one element at the end | `append(value)` |
| Add one element at a specific position | `insert(index, value)` |
| Add multiple elements | `extend(other_list)` or `+=` |
| Combine two lists into a new list | `list1 + list2` |

```python
names.append("Nour")
names.insert(1, "Khaled")
names.extend(["Mona", "Rami"])
```

---

## Removing Elements

| Goal | Method |
|------|--------|
| Remove by index | `del names[index]` |
| Remove last element (and return it) | `pop()` |
| Remove by index (and return it) | `pop(index)` |
| Remove by value | `remove(value)` |
| Remove a slice | `del names[start:end]` |
| Clear all elements | `clear()` or `del names[:]` |
| Delete the list entirely | `del names` |

```python
names.remove("Ali")
last = names.pop()
del names[0]
```

> `remove()` deletes the **first** occurrence of the value.
> `pop()` returns the removed element — useful if you need it.

---

## Sorting and Ordering

| Method | Modifies original? | Returns |
|--------|--------------------|---------|
| `sort()` | ✅ Yes | `None` |
| `sorted()` | ❌ No | New sorted list |
| `reverse()` | ✅ Yes | `None` |

```python
numbers = [4, 1, 7, 3]

numbers.sort()
print(numbers)  # [1, 3, 4, 7]

print(sorted([4, 1, 7, 3]))  # [1, 3, 4, 7]  — original unchanged

numbers.reverse()
print(numbers)  # [7, 4, 3, 1]
```

---

## Length

```python
numbers = [1, 2, 3]
print(len(numbers))  # 3
```

---

## Combined Example

```python
numbers = [4, 1, 7, 3]

print("Length:", len(numbers))  # 4

numbers.reverse()
print("After reverse:", numbers)  # [3, 7, 1, 4]

numbers.sort()
print("After sort:", numbers)  # [1, 3, 4, 7]

original = [4, 1, 7, 3]
print("Sorted copy:", sorted(original))  # [1, 3, 4, 7]
print("Original:", original)  # [4, 1, 7, 3]
```