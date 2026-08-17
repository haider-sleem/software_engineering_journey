# Chapter 5: If Statements

> *Python Crash Course*

---

## if / elif / else

Use this chain when conditions are **mutually exclusive** — only the first matching condition runs, and the rest are skipped:

```python
age = 25

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

### When to skip `else`

`else` catches anything that didn't match — including invalid or unexpected input. If you have a specific final condition, use a final `elif` instead and leave out `else`. This way the code only runs when conditions are explicitly met.

```python
# Explicit — only known conditions are handled
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age >= 18:
    print("Adult")
```

---

## Independent `if` Statements

When **more than one condition** can be true at the same time and you want to act on each one, use separate `if` statements instead of `elif`:

```python
toppings = ["mushrooms", "pepperoni", "extra cheese"]

if "mushrooms" in toppings:
    print("Adding mushrooms")
if "pepperoni" in toppings:
    print("Adding pepperoni")
if "extra cheese" in toppings:
    print("Adding extra cheese")
```

Using `elif` here would stop after the first match — all three toppings would never be added.

**Rule:**
- One block should run → `if / elif / else`
- Multiple blocks may run → series of independent `if` statements

---

## Checking Lists in Conditions

```python
users = ["Ali", "Omar", "Sara"]

if "Ali" in users:
    print("Welcome, Ali!")

if "Nour" not in users:
    print("Nour is not registered.")
```

---

## Conditional Inside a Loop

Conditions work naturally inside `for` loops to handle specific items differently:

```python
players = ["ali", "omar", "admin", "sara"]

for player in players:
    if player == "admin":
        print(f"Welcome back, {player}! Ready to manage the system.")
    else:
        print(f"Hello, {player}!")
```

---

## Checking if a List Is Empty

```python
players = []

if players:
    for player in players:
        print(f"Hello, {player}!")
else:
    print("No players found.")
```

An empty list evaluates to `False` — a list with at least one element evaluates to `True`.