# Chapter 9 — Classes
> Object-Oriented Programming in Python — Organized Study Notes

---

## Table of Contents

1. [Core Concepts](#1-core-concepts)
2. [Creating a Class](#2-creating-a-class)
3. [Attributes](#3-attributes)
4. [Methods](#4-methods)
5. [Inheritance](#5-inheritance)
6. [Method Overriding](#6-method-overriding)
7. [Composition](#7-composition)
8. [Modules & Code Organization](#8-modules--code-organization)
9. [Import Styles](#9-import-styles)
10. [Standard Library](#10-standard-library)
11. [Style Guide](#11-style-guide)
12. [Quick Reference](#12-quick-reference)

---

## 1. Core Concepts

OOP organizes programs around **classes** and **objects** instead of functions and procedures.

| Term | Definition |
|---|---|
| **Class** | A blueprint for creating objects |
| **Object (Instance)** | A specific object created from a class |
| **Instantiation** | The act of creating an object from a class |
| **Attribute** | Data stored inside an instance |
| **Method** | A function defined inside a class |
| **Behavior** | Actions an object can perform |

**Why OOP?**
- Better organization of related data and behavior
- Code reuse — one class, many instances
- Easier to maintain and extend

---

## 2. Creating a Class

```python
class Dog:
    """A simple model of a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting.")
```

### `__init__()`

- Runs **automatically** when a new object is created.
- Receives `self` as the first parameter (always).
- Additional parameters become the instance's attributes.

### `self`

- Refers to the **current instance**.
- Used to access or set attributes inside any method.
- Python passes it automatically — you never include it when calling a method.

### Creating instances

```python
my_dog = Dog("Rex", 3)
your_dog = Dog("Max", 5)
```

- Each instance is **independent** — creating one does not affect others.
- One class can create **many** independent instances.

### Accessing attributes and calling methods

```python
print(my_dog.name)  # Rex
my_dog.sit()  # Rex is sitting.
```

> Use **dot notation** to access attributes and call methods.

---

## 3. Attributes

### Instance attributes

Set inside `__init__()` — each instance gets its own copy.

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

### Default values

Not every attribute must be passed as a parameter. Assign defaults directly inside `__init__()`.

```python
def __init__(self, make, model):
    self.make = make
    self.model = model
    self.odometer = 0  # default value — no parameter needed
```

Every new instance automatically gets `odometer = 0`.

### Modifying attributes

**Three approaches:**

```python
# 1. Direct modification — simple but no validation
my_car.odometer = 100


# 2. Setter method — allows validation
def update_odometer(self, mileage):
    if mileage >= self.odometer:
        self.odometer = mileage


# 3. Increment method — adds to the current value
def increment_odometer(self, miles):
    self.odometer += miles
```

> Methods allow **controlled updates** and **validation** — prefer them over direct modification when data integrity matters.

---

## 4. Methods

- Defined inside the class with `def`.
- Always receive `self` as the first parameter.
- Can **print** results or **return** values.

```python
# Printing — works but less reusable
def describe(self):
    print(f"{self.make} {self.model}")


# Returning — more flexible and reusable
def get_description(self):
    return f"{self.make} {self.model}"
```

> Prefer `return` over `print` inside methods — the caller can decide what to do with the value.

---

## 5. Inheritance

A **child class** inherits all attributes and methods from a **parent class**, and can add its own.

### Rules

- Define the parent class first.
- Pass the parent class name in parentheses.
- Call `super().__init__()` to initialize parent attributes.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)  # initialize parent
        self.battery_size = battery_size  # new child attribute

    def describe_battery(self):
        print(f"Battery: {self.battery_size} kWh")
```

### What the child gets automatically

- All parent **attributes** (via `super().__init__()`)
- All parent **methods** (inherited automatically)

### What the child can add

- New attributes specific to the child
- New methods specific to the child

> **Principle:** Put **common** behavior in the parent. Put **specialized** behavior in the child. Avoid duplicating code.

---

## 6. Method Overriding

A child class can **replace** a parent method by defining a method with the **same name**.

```python
class Car:
    def fuel_type(self):
        return "Gasoline"


class ElectricCar(Car):
    def fuel_type(self):  # overrides parent method
        return "Electric"
```

- Python always uses the **child's version** first.
- Override behavior that doesn't fit the child class.
- Inheritance allows reuse with customization.

---

## 7. Composition

**Composition** means one class contains an instance of another class as an attribute.

> Use composition when an object **"has a"** another object.
> (`ElectricCar` **has a** `Battery`)

```python
class Battery:
    def __init__(self, size=75):
        self.size = size

    def describe(self):
        return f"{self.size} kWh battery"


class ElectricCar(Car):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.battery = Battery()  # composition
```

### Accessing nested objects

```python
my_car = ElectricCar("Tesla", "Model S")
print(my_car.battery.describe())  # dot notation through levels
```

### Inheritance vs Composition

| | Inheritance | Composition |
|---|---|---|
| Relationship | "is a" | "has a" |
| Example | `ElectricCar` is a `Car` | `ElectricCar` has a `Battery` |
| Use when | Child is a specialized version of parent | Object contains another object |

> **Design note:** There is often more than one valid design. Focus on **responsibilities**, not only syntax. Refactoring classes is a normal part of development.

---

## 8. Modules & Code Organization

A Python file (`.py`) is called a **module**. Storing classes in separate modules keeps projects clean.

### Single class per module

```python
# car.py
class Car: ...
```

```python
# main.py
from car import Car

my_car = Car("Toyota", "Camry")
```

> Write a **module-level docstring** at the top of every module file.

### Multiple classes in one module

Group classes by **responsibility**.

```python
# vehicles.py
class Car: ...


class ElectricCar(Car): ...
```

A module can also import another module when needed.

```python
# electric_car.py
from car import Car  # import dependency


class ElectricCar(Car): ...
```

> Keep **class definitions** in separate files.
> Keep **business logic** in the main program.

---

## 9. Import Styles

### Import a specific class (recommended)

```python
from car import Car
from vehicles import Car, ElectricCar
```

- Import only what you need.
- Keeps code concise and readable.

### Import the whole module

```python
import car

my_car = car.Car("Toyota", "Camry")  # module.ClassName
```

- Avoids naming conflicts.
- Makes it clear where each class comes from.
- Common in professional Python codebases.

### Using aliases

```python
from electric_car import ElectricCar as EC
import vehicles as v
```

- Makes long names shorter.
- Use only when it genuinely improves readability.

### Wildcard import — avoid

```python
from car import *  # ❌ avoid
```

| Problem | Reason |
|---|---|
| Reduces readability | Unclear where names come from |
| Causes naming conflicts | Overwrites existing names silently |

> **Rule:** Import specific classes. If many are needed, import the whole module.

---

## 10. Standard Library

Python ships with a rich standard library — use `import` to access any module.

```python
import random

random.randint(1, 6)  # random integer between 1 and 6 (inclusive)
random.choice([1, 2, 3])  # random element from a sequence
```

> `random` is not suitable for security-sensitive applications (passwords, tokens). Use `secrets` instead.

---

## 11. Style Guide

| Rule | Detail |
|---|---|
| **Class names** | `CamelCase` → `ElectricCar`, `BankAccount` |
| **Instance & module names** | `snake_case` → `my_car`, `electric_car.py` |
| **Docstrings** | Every class and module should have one |
| **Blank lines between methods** | 1 blank line |
| **Blank lines between classes** | 2 blank lines |
| **Import order** | Standard library first, then local modules |

```python
# ✅ Correct import order
import random  # standard library
from car import Car  # local module
```

---

## 12. Quick Reference

### Minimal class template

```python
class ClassName:
    """One-line description."""

    def __init__(self, param):
        self.param = param

    def method(self):
        return self.param
```

### Inheritance template

```python
class Child(Parent):
    def __init__(self, param, extra):
        super().__init__(param)
        self.extra = extra
```

### Composition template

```python
class Engine:
    def start(self):
        return "Running"


class Car:
    def __init__(self):
        self.engine = Engine()  # "has a" relationship
```

### Key rules to remember

1. `__init__()` runs automatically on instantiation — use it to set attributes.
2. `self` always refers to the current instance — never skip it in method definitions.
3. Use `return` in methods instead of `print` — makes them reusable.
4. Use `super().__init__()` in every child class to initialize parent attributes.
5. Override only methods that don't fit the child — inherit the rest.
6. Use **composition** when the relationship is "has a", not "is a".
7. Store classes in **modules** — one responsibility per file.
8. Import **specific classes**, not wildcards.