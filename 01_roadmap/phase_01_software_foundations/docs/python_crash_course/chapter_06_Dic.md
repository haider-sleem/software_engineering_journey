# Chapter 6: Dictionaries

> *Python Crash Course*

---

## What Is a Dictionary?

A collection of **key-value pairs** — each key is connected to a specific value.

```python
person = {"name": "Haider", "age": 41, "city": "Damietta"}
```

| Part | Rules |
|------|-------|
| **Key** | Must be **immutable** — strings, numbers, or tuples are valid; lists and dictionaries are not |
| **Value** | Can be any Python object — string, number, list, or even another dictionary |

---

## Accessing Values

```python
# Direct access — raises KeyError if key doesn't exist
print(person["name"])  # Haider

# Safe access with get() — returns None or a default if key missing
print(person.get("email"))  # None
print(person.get("email", "not provided"))  # not provided
```

---

## Adding and Modifying

```python
# Add a new key-value pair
person["email"] = "haider@example.com"

# Modify an existing value
person["city"] = "Cairo"
```

Dictionaries are dynamic — they can grow at any time.

---

## Removing

```python
del person["age"]  # permanently removes the key-value pair
```

---

## Looping

```python
user = {"name": "Haider", "role": "developer", "city": "Damietta"}

# Key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")

# Keys only (default behavior)
for key in user.keys():
    print(key)

# Keys in sorted order
for key in sorted(user.keys()):
    print(key)

# Values only
for value in user.values():
    print(value)
```

---

## Unique Values with `set()`

Use `set()` to get the unique values from a dictionary's values:

```python
languages = {"Ali": "Python", "Omar": "Python", "Sara": "JavaScript"}

for language in set(languages.values()):
    print(language)
# Python
# JavaScript
```

---

## Nesting

### List of Dictionaries

```python
users = [
    {"name": "Ali", "role": "admin"},
    {"name": "Omar", "role": "user"},
]

for user in users:
    print(user["name"], "-", user["role"])
```

### List Inside a Dictionary

```python
order = {
    "customer": "Haider",
    "items": ["laptop", "mouse", "keyboard"],
}

print(order["items"][0])  # laptop
```

### Dictionary Inside a Dictionary

```python
users = {
    "ali": {"email": "ali@example.com", "role": "admin"},
    "omar": {"email": "omar@example.com", "role": "user"},
}

print(users["ali"]["role"])  # admin
```