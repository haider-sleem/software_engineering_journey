# CS50P — Lecture 1 Notes
> Python & Problem Solving — Organized Study Notes

---

## Table of Contents

1. [Environment & Tools](#1-environment--tools)
2. [Python Files & the Interpreter](#2-python-files--the-interpreter)
3. [CLI vs GUI](#3-cli-vs-gui)
4. [Functions & Arguments](#4-functions--arguments)
5. [Input & Output](#5-input--output)
6. [Variables](#6-variables)
7. [Strings & String Methods](#7-strings--string-methods)
8. [Type Conversion & Numbers](#8-type-conversion--numbers)
9. [Bugs & Debugging](#9-bugs--debugging)
10. [Defining Your Own Functions](#10-defining-your-own-functions)
11. [Problem Solving Mindset](#11-problem-solving-mindset)

---

## 1. Environment & Tools

### Text Editor vs Code Editor

A **text editor** writes and saves plain text only — no fonts, no colors, no formatting.
Programming code is plain text, so a code editor is what you need.

| Program | Type | Use for code? |
|---|---|---|
| VS Code | Code Editor | ✅ Yes |
| Notepad++ | Code Editor | ✅ Yes |
| Vim / Nano | Code Editor | ✅ Yes |
| Microsoft Word | Document Editor | ❌ No — adds hidden formatting |

### Visual Studio Code (VS Code)

Free, lightweight, fast, and highly customizable. One of the most popular editors for Python and Backend development.

**Key features:**

- **Syntax Highlighting** — colors keywords, strings, and numbers for easier reading
- **Auto-completion** — suggests code as you type
- **Integrated Terminal** — run commands without leaving the editor
- **Debugger** — step through code and watch variable values
- **Git Integration** — manage version control inside the editor
- **Extensions** — add support for any language or tool

**Why it matters:** Instead of switching between multiple programs, you write, run, debug, and use Git — all in one place.

**Useful Terminal commands inside VS Code:**

```bash
python hello.py   # run a Python file
git status        # check Git status
pytest            # run tests
```

**Open a file directly from the terminal:**

```bash
code hello.py
```

> If the file does not exist, VS Code creates it automatically.

---

## 2. Python Files & the Interpreter

### Python Files

Python source code is saved in plain text files with the `.py` extension.

```
hello.py
```

The `.py` extension tells both the programmer and the tools that this file contains Python code.

### The Python Interpreter

**Python** means two things:

| Meaning | Description |
|---|---|
| Python Language | The syntax and rules you write |
| Python Interpreter | The program installed on your computer that runs your code |

**A `.py` file is only text — it cannot run by itself.**
The Python Interpreter reads it, translates it into machine instructions, and executes it.

**Execution flow:**

```
hello.py
    ↓
Python Interpreter
    ↓
Read → Translate → Execute
    ↓
Program Output
```

**Run a Python file:**

```bash
python hello.py
```

### Reading Order

Python reads code **top to bottom**, left to right.

```python
print("A")
print("B")
print("C")
```

Output:
```
A
B
C
```

### Binary & Source Code

- Computers understand only binary (`0` and `1`).
- The Interpreter handles the translation from Python source code to machine instructions — you do not need to do this manually.

---

## 3. CLI vs GUI

### Command-Line Interface (CLI)

You interact with the computer by **typing commands**.

```bash
python hello.py
git status
ls
pwd
```

- Professional developers use the CLI every day.
- Faster and more powerful than a mouse for many development tasks.

**The prompt:**

```bash
$ python hello.py
```

> The `$` is the prompt symbol — it is **not** part of the command.

### Graphical User Interface (GUI)

You interact using buttons, menus, windows, and a mouse.

Examples: Google Chrome, Microsoft Word, WhatsApp.

**Key distinction:**

| | Developer | End User |
|---|---|---|
| Interface | Terminal (CLI) | Application (GUI / Browser) |
| Example | `python app.py` | Clicks a button on a website |

> Users never see the Terminal. They only use the final application.

**Terminal shortcut:**

```bash
clear        # clear the screen
Ctrl + L     # same as clear (does not delete files)
```

---

## 4. Functions & Arguments

### What is a Function?

A reusable piece of code that performs a specific task. Think of it as a **verb** — it does something.

```python
print()    # displays text
input()    # reads user input
len()      # returns the length of something
type()     # returns the type of a value
```

### Built-in Functions

Python ships with many built-in functions. You do not need to create them — just call them.

### Arguments

An **argument** is the value you pass into a function to tell it what to work with.

**Syntax:**

```python
function_name(argument)
```

**Examples:**

```python
print("Hello")    # argument: "Hello"
print(100)        # argument: 100
print(True)       # argument: True
```

The **function stays the same**. Only the **argument changes** — this makes functions flexible and reusable.

### Return Values vs Side Effects

| Concept | Description | Example |
|---|---|---|
| **Side Effect** | An action the function performs besides returning a value | `print()` displays text on screen |
| **Return Value** | The value the function sends back to the caller | `input()` returns what the user typed |

Some functions do both. Some do only one.

```python
# side effect only — print() does not return useful data
print("Hello")

# return value — input() returns what the user typed
name = input("Name: ")
```

### Command vs Function

| | Command | Function |
|---|---|---|
| Where | Terminal | Inside a Python program |
| Example | `python hello.py` | `print("Hello")` |
| Purpose | Interact with the OS | Perform a task in Python |

> The programmer **calls** a function. The Python Interpreter **executes** it.
> You do not need to know how a function is implemented to use it.

---

## 5. Input & Output

### print()

Sends data **to** the user (output).

```python
print("Hello, World!")
```

**Multiple arguments:**

```python
print("Hello,", name)    # adds a space between arguments automatically
```

**`sep` and `end` parameters:**

```python
# Default behavior:
# sep = " "   (space between arguments)
# end = "\n"  (new line after printing)

print("Hello", "World", sep="-", end="")
# Output: Hello-World   (no new line)
```

### input()

Receives data **from** the user (input). Pauses execution and waits for the user to press Enter.

```python
name = input("What's your name? ")
```

> Always add a space before the closing quote `"What's your name? "` so the user's text doesn't stick to the prompt.

**`input()` always returns a string**, even if the user types a number.

**Important:** Calling `input()` without storing the result loses the data permanently.

```python
input("Name: ")    # ❌ data is lost
name = input("Name: ")    # ✅ data is saved
```

### print() vs input()

| Function | Direction | Action |
|---|---|---|
| `print()` | Program → User | Sends output |
| `input()` | User → Program | Receives input |

> **Backend note:** Console programs use `input()`. Backend applications receive data from HTTP requests, JSON, forms, and API clients — same concept, different delivery mechanism.

### f-Strings

The modern and recommended way to embed variables inside strings.

```python
print(f"Hello, {name}")
```

### String Concatenation

```python
print("Hello, " + name)    # joins two strings into one
```

### Escape Characters

Use `\` to include special characters inside strings.

```python
print("Hello \"friend\"")    # prints: Hello "friend"
print('Hello "friend"')      # same result using single quotes
```

---

## 6. Variables

A variable is a **named container in memory** that stores a value.

```python
name = input("What's your name? ")
```

**Key rules:**

- `=` is the **assignment operator** — not mathematical equality. It copies the value on the right into the variable on the left.
- Use **descriptive names**: `name`, `age`, `email` — not `x`, `n`, `tmp`.
- Variable names go **without quotes**. Quotes make it a string literal.

```python
print(name)      # prints the value stored in name
print("name")    # prints the word "name"
```

### Comments

```python
# This is a comment — Python ignores it
```

- Start with `#`
- Explain **why**, not **what** (the code already shows what)

### Pseudocode

A way to describe a solution in plain language before writing actual code.

- Not a programming language — just structured thinking.
- Break the problem into small steps, then convert each step into Python.

---

## 7. Strings & String Methods

### Common String Methods

| Method | What it does | Example |
|---|---|---|
| `strip()` | Removes whitespace from both ends | `name.strip()` |
| `lstrip()` | Removes whitespace from the left only | `name.lstrip()` |
| `rstrip()` | Removes whitespace from the right only | `name.rstrip()` |
| `capitalize()` | Capitalizes only the first letter | `name.capitalize()` |
| `title()` | Capitalizes the first letter of every word | `name.title()` |
| `split()` | Splits a string into a list | `name.split(" ")` |

> Methods return a **new value** — they do not modify the original string. Always save the result.

```python
name = name.strip()    # ✅ saves the result
name.strip()           # ❌ result is discarded
```

### Method Chaining

Methods can be chained — Python executes them left to right, each one receiving the output of the previous.

```python
name = name.strip().title()
```

Execution order:
```
name → strip() → title() → result
```

**Benefits:** shorter code, fewer temporary variables, easier to read.

### split()

Splits a string into parts and returns a list. Useful for separating a full name into first and last.

```python
first, last = name.split(" ")
```

```
"Haider Sleem"  →  first = "Haider",  last = "Sleem"
```

> **Watch out:** Multiple consecutive spaces cause a `ValueError: too many values to unpack`. Use `strip()` before `split()` to be safe.

### Python Interactive Mode

A quick way to test ideas without creating a file.

```bash
python3       # start interactive mode
>>>           # the interactive prompt
exit()        # exit   (or Ctrl + D)
```

**Best for experiments and quick tests — not for full projects.**

---

## 8. Type Conversion & Numbers

### Type Conversion

`input()` **always returns a string**. To do math with user input, convert it first.

| Function | Converts to | Example |
|---|---|---|
| `int()` | Integer | `int("42")` → `42` |
| `float()` | Float (decimal) | `float("3.14")` → `3.14` |

**Why it matters:**

```python
"3" + "5"    # → "35"   (string concatenation)
3 + 5        # → 8      (integer addition)
```

**Nested functions** — the innermost executes first:

```python
age = int(input("Age: "))
# 1. input() runs → returns "25"
# 2. int() runs   → returns 25
```

### Float

Represents numbers with decimal points.

```python
price = float(input("Price: "))
```

> Floats have limited precision — computers cannot represent every decimal number exactly.

### round()

```python
round(number)       # rounds to nearest integer
round(number, 2)    # keeps 2 decimal places
```

From the documentation: `round(number[, ndigits])` — `[]` means the argument is optional.

### Numeric Formatting

```python
print(f"{value:,}")    # adds thousands separator: 1,000,000
```

> Formatting changes the **display only** — the actual value is unchanged.

**Common use cases in Backend:** prices, taxes, discounts, ratings, coordinates.

---

## 9. Bugs & Debugging

### Types of Bugs

| Type | Description | Example |
|---|---|---|
| **Syntax Error** | Code violates Python grammar — program won't start | Missing `)` or `"` |
| **Runtime Error** | Program crashes while running | Division by zero |
| **Logic Error** | Program runs but produces wrong results | No error message, wrong output |

**Example Syntax Error:**

```python
print("Hello"
# SyntaxError: '(' was never closed
```

### Debugging Process

1. Read the error message carefully — it tells you the file and line number.
2. Find the root cause.
3. Fix one error at a time.
4. Run the program again and verify.

### Computers Are Literal

```
Humans understand meaning.
Computers understand syntax.
```

- One missing character can stop the entire program.
- There is no "almost correct" — code is either valid or invalid.
- Computers do not guess your intention.

> **Backend note:** Professional developers use linters, unit tests, logging, debuggers, and CI/CD pipelines to catch bugs before users are affected.

---

## 10. Defining Your Own Functions

### Syntax

```python
def function_name(parameter):
    # function body — indentation defines the block
    return value
```

**Key concepts:**

| Term | Meaning |
|---|---|
| `def` | Keyword to define a function |
| **Parameter** | Variable name in the function definition |
| **Argument** | Actual value passed when calling the function |
| **Indentation** | Defines what belongs inside the function |
| `return` | Sends a value back to the caller |

### Parameters & Default Values

```python
def greet(name="stranger"):
    print(f"Hello, {name}")

greet("Haider")    # → Hello, Haider
greet()            # → Hello, stranger
```

### return vs print

| | `return` | `print` |
|---|---|---|
| Purpose | Sends a value back to the caller | Displays output on screen |
| Usable later? | ✅ Yes — store in a variable | ❌ No — only a side effect |

```python
def get_name():
    return input("Name: ")    # ✅ caller can use this value

name = get_name()
```

### main() Convention

`main()` is a **convention**, not a Python requirement. It marks the entry point of the program.

```python
def main():
    name = get_name()
    greet(name)

def get_name():
    return input("What's your name? ")

def greet(name):
    print(f"Hello, {name}")

main()    # call main() at the end
```

### Scope

- A variable exists **only inside the function where it was created**.
- A local variable cannot be accessed outside its function.
- Share values between functions by passing them as **arguments**.

```python
def main():
    name = get_name()    # name lives here
    greet(name)          # passed as argument

def greet(name):         # received as parameter
    print(f"Hello, {name}")
```

### Best Practices

- Keep functions **small** — one function, one task.
- Use **meaningful names** for parameters.
- **Avoid repeating code** — if you write the same logic twice, make it a function.
- Prefer **readability** over clever one-liners.

---

## 11. Problem Solving Mindset

Programming is not only about writing code — it is about **solving problems**.

### Mental Tools

- Break a big problem into smaller steps.
- Read error messages carefully.
- Find the root cause before fixing.
- Think step by step, not all at once.

### Technical Tools

- **VS Code** — write and edit code
- **Python Interpreter** — run the code
- **Debugger** — step through execution
- **Logging** — trace what happened
- **Testing tools** — verify correctness

### How Skills Develop

```
Practice → Make mistakes → Fix mistakes → Experience
```

Mistakes are a normal and necessary part of learning.

> **Backend note:** Backend developers spend a significant part of their time debugging applications, reading logs, fixing production issues, and testing changes. Debugging is one of the most important professional skills.

### Documentation

Reading official documentation is an essential Backend skill. Every major framework — FastAPI, Flask, Django, SQLAlchemy — relies on its docs.

**Read the docs when you need to know:**
- What a function does
- What arguments it accepts
- What it returns

---

## Quick Reference

### Essential Functions

| Function | Purpose |
|---|---|
| `print(value)` | Display output |
| `input(prompt)` | Read user input (returns string) |
| `int(value)` | Convert to integer |
| `float(value)` | Convert to float |
| `round(n, digits)` | Round a number |
| `len(value)` | Return the length |
| `type(value)` | Return the type |

### Essential String Methods

| Method | Purpose |
|---|---|
| `.strip()` | Remove whitespace from both ends |
| `.title()` | Capitalize first letter of each word |
| `.capitalize()` | Capitalize first letter only |
| `.split(sep)` | Split into a list |
| `.lstrip()` | Remove whitespace from left |
| `.rstrip()` | Remove whitespace from right |

### print() Parameters

| Parameter | Default | Purpose |
|---|---|---|
| `sep` | `" "` | Separator between arguments |
| `end` | `"\n"` | What to print after the last argument |

### f-String Formatting

```python
f"{name}"          # insert variable
f"{value:,}"       # thousands separator
f"{value:.2f}"     # 2 decimal places
f"{value:,.2f}"    # both
```