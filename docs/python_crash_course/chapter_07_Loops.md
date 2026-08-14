# Chapter 7: User Input and While Loops

> *Python Crash Course*

---

## User Input

`input()` always returns a string. Use `int()` or `float()` to convert when needed.

```python
age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You can vote.")
```

---

## `while` Loop

Runs as long as a condition is `True`. Always make sure the condition eventually becomes `False`.

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### Active Flag

Use a boolean flag to control a loop cleanly, especially when multiple conditions can end it:

```python
active = True

while active:
    message = input("Enter a message ('quit' to exit): ")
    if message == "quit":
        active = False
    else:
        print(message)
```

### `break`

Exits the loop immediately:

```python
while True:
    city = input("Enter a city ('quit' to stop): ")
    if city == "quit":
        break
    print(f"I'd love to visit {city}!")
```

### `continue`

Skips the rest of the current iteration and goes back to the top of the loop:

```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)  # prints odd numbers only
```

---

## Using `while` with Lists

### Moving Items Between Lists

```python
sandwich_orders = ["tuna", "egg", "cheese"]
finished_sandwiches = []

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"Making: {current}")
    finished_sandwiches.append(current)
```

### Removing All Occurrences of a Value

`remove()` only deletes the first match — use `while` to remove all:

```python
pets = ["dog", "cat", "dog", "fish", "dog"]

while "dog" in pets:
    pets.remove("dog")

print(pets)  # ['cat', 'fish']
```

---

## Collecting Input into a Dictionary

```python
responses = {}
active = True

while active:
    name = input("Name: ")
    response = input("Favorite language: ")
    responses[name] = response

    again = input("Another response? (yes/no): ")
    if again != "yes":
        active = False

for name, response in responses.items():
    print(f"{name}: {response}")
```