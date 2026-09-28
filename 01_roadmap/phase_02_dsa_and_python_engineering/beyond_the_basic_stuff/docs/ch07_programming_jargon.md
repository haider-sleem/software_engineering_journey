# Chapter 7: Programming Jargon

> *Beyond the Basic Stuff with Python — Al Sweigart*

---

## Why Programming Jargon Matters

Programming contains many technical terms that have similar meanings or are commonly confused.

The exact meaning of some terms can vary between programming languages or among programmers, but understanding the distinctions helps you communicate clearly with other developers. The chapter focuses on these terms as they apply to Python.

---

## Python the Language vs. Python the Interpreter

The word **Python** can refer to two different things:

### Python Programming Language

The **Python language** is the set of rules and features used to write Python source code.

### Python Interpreter

The **Python interpreter** is the software that reads Python source code and executes it.

When people say:

> "Python runs this program."

they are usually referring to the interpreter.

### CPython

**CPython** is the reference implementation of Python.

It is:

* written in C
* maintained by the Python Software Foundation
* the implementation whose behavior is considered canonical when differences exist between implementations

Other Python implementations include:

* **Jython** — implemented in Java
* **PyPy** — includes a Just-In-Time (JIT) compiler

Ideally, Python source code should work across implementations, although small incompatibilities can exist.

---

## Garbage Collection

**Garbage collection** is a form of automatic memory management.

In languages with manual memory management, programmers may need to explicitly allocate and free memory. Forgetting to free memory can cause a **memory leak**, while freeing the same memory twice can cause a **double-free bug**.

Python automatically manages memory so programmers normally don't have to explicitly free objects.

You can think of garbage collection as **memory recycling**:

```text
Object no longer needed
        ↓
Memory can be reclaimed
        ↓
Memory becomes available again
```

For example, local objects created inside a function can become eligible for garbage collection after the function returns — though the exact timing depends on the implementation.

---

## Literals

A **literal** is a fixed value written directly in source code.

```python
age = 42 + len("Zophie")
```

Here:

```text
42        → integer literal
"Zophie"  → string literal
```

Examples of commonly called Python literals:

| Example                  | Type       |
| ------------------------ | ---------- |
| `42`                     | `int`      |
| `3.14`                   | `float`    |
| `1.4886191506362924e+36` | `float`    |
| `"Howdy!"`               | `str`      |
| `r"Green\Blue"`          | `str`      |
| `[]`                     | `list`     |
| `{"name": "Zophie"}`     | `dict`     |
| `b"\x41"`                | `bytes`    |
| `True`                   | `bool`     |
| `None`                   | `NoneType` |

### Technical Precision

Some of these examples are technically classified differently by Python's formal language documentation.

For example:

* `-5` consists of the unary `-` operator applied to the literal `5`
* `True`, `False`, and `None` are technically keywords
* `[]` and `{}` have more specific formal classifications

Nevertheless, **literal** is the common practical term programmers use for fixed values written directly in source code.

---

## Keywords

**Keywords** are reserved words that have special meaning in the Python language.

They cannot be used as ordinary identifiers such as variable names.

Examples:

```python
if
else
for
while
def
class
return
try
except
import
```

For example:

```python
while = 10
```

is invalid because `while` is a Python keyword.

Python keywords remain in English even when identifiers are written using another language.

---

## Objects, Values, Instances, and Identities

## Object

An **object** is a representation of data.

Examples include:

```python
42
"hello"
[1, 2, 3]
{"name": "Zophie"}
```

All Python objects have:

1. **Value**
2. **Data type**
3. **Identity**

---

## Value

The **value** is the data represented by the object.

For example:

```python
spam = 42
```

The object's value is:

```text
42
```

---

## Data Type

The **data type** describes what kind of object it is.

```python
42          → int
"hello"     → str
[1, 2, 3]   → list
```

---

## Identity

Every object has an **identity** that uniquely identifies that object during its lifetime.

You can inspect it with:

```python
id(spam)
```

The identity does not change while that object exists.

An object's value can change without its identity changing, for mutable objects such as lists.

---

## Variables Are References

A variable in Python is better understood as a **name/reference to an object**, rather than as a box containing the object.

```python
spam = {"name": "Zophie"}
eggs = spam
```

Now:

```text
spam ──┐
       ├──→ same dictionary object
eggs ──┘
```

Therefore:

```python
spam["name"] = "Al"

print(eggs)
```

produces:

```python
{"name": "Al"}
```

because both names refer to the same object.

The assignment operator `=` copies the **reference** (the name binding), not the object itself.

---

## `is` vs. `==`

### `==`

Checks whether two objects have equal **values**.

```python
spam == bacon
```

### `is`

Checks whether two variables refer to the **same object**.

```python
spam is eggs
```

Conceptually:

```python
x is y
```

is equivalent to:

```python
id(x) == id(y)
```

Example:

```python
spam = {"name": "Zophie"}
eggs = spam
bacon = {"name": "Zophie"}
```

Then:

```python
spam == eggs      # True
spam is eggs      # True

spam == bacon     # True
spam is bacon     # False
```

Same value does not necessarily mean same object.

> **Warning:** Do not use `is` to compare values like integers or strings. Python may cache small integers and interned strings, which can make `is` return `True` unexpectedly. Use `==` for value comparison.

---

## Instances

An **instance** is an object created from a class.

For example:

```python
class Product:
    pass

product1 = Product()
```

`product1` is an **instance** of `Product`.

The terms **object** and **instance** overlap, but "instance" is commonly used when discussing an object's relationship to a class.

---

## Items

An **item** is a value contained inside a container.

For example:

```python
numbers = [10, 20, 30]
```

The list contains three items:

```text
10
20
30
```

Similarly, dictionary entries can be discussed as items.

The term is especially useful when talking about iterating through containers.

---

## Mutable vs. Immutable

## Mutable

A **mutable object** can have its value changed after creation.

Examples:

```python
list
dict
set
```

Example:

```python
spam = ["cat", "dog"]

spam.append("moose")
```

The same list object has been modified.

---

## Immutable

An **immutable object** cannot have its value changed after creation.

Examples include:

```python
int
float
str
tuple
```

For example:

```python
bacon = "Goodbye"
```

Trying to modify a character in-place:

```python
bacon[0] = "J"
```

raises an error.

If you appear to "change" a string:

```python
bacon = "Hello"
```

you are actually making the variable refer to a new string object.

---

## Immutable Tuple Containing Mutable Objects

A tuple itself is immutable:

```python
eggs = ("cat", "dog", [2, 4, 6])
```

You cannot replace the list inside the tuple:

```python
eggs[2] = [8, 10]
```

But the list object itself is mutable:

```python
eggs[2].append(8)
eggs[2].append(10)
```

Result:

```python
("cat", "dog", [2, 4, 6, 8, 10])
```

The tuple still refers to the same list object; the list's value changed.

---

## Indexes, Keys, and Hashes

## Index

An **index** is an integer used to access an element by position in a sequence.

Python uses **zero-based indexing**:

```python
spam = ["cat", "dog", "moose"]

spam[0]   # "cat"
spam[1]   # "dog"
```

Negative indexes count from the end:

```python
spam[-1]  # "moose"
spam[-2]  # "dog"
```

Conceptually:

```text
0      1       2
↓      ↓       ↓
cat   dog    moose

-3    -2      -1
```

Strings can also be indexed:

```python
"Hello"[0]  # "H"
```

---

## Key

A **dictionary** uses keys instead of integer indexes:

```python
spam = {"name": "Zophie"}

spam["name"]
```

The key is:

```text
"name"
```

and the associated value is:

```text
"Zophie"
```

---

## Hash

A **hash** is an integer that acts somewhat like a fingerprint for a value.

The built-in function:

```python
hash(value)
```

returns the object's hash when the object is hashable.

Important properties:

* an object's hash remains stable during its lifetime
* objects with equal values must have equal hashes
* immutable objects such as strings, integers, and floats are hashable. Tuples are hashable only when all of their items are hashable
* mutable objects such as lists are not hashable

Dictionary keys must be hashable.

---

## Containers, Sequences, Mappings, and Sets

These are broader categories of data types.

## Container

A **container** is an object that contains other objects.

Examples:

```python
list
tuple
dict
set
```

---

## Sequence

A **sequence** is an ordered collection whose elements can be accessed by integer indexes.

Examples:

```python
list
tuple
str
range
```

Sequences support concepts such as indexing.

---

## Mapping

A **mapping** associates keys with values.

The main Python example is:

```python
dict
```

Example:

```python
prices = {
    "apple": 1.5,
    "orange": 2.0,
}
```

Mappings don't use positional indexes to access their values; they use keys.

Python dictionaries preserve insertion order starting with Python 3.7 as a language guarantee. This does **not** mean dictionary elements can be accessed using integer indexes such as `spam[0]`.

---

## Set Type

A **set** is a collection designed for unique values.

```python
numbers = {1, 2, 3}
```

Sets do not provide sequence-style indexing.

---

## Built-in vs. User-defined

## Built-in

A **built-in** feature is provided by Python itself.

Examples:

```python
list
dict
str
len()
print()
```

---

## User-defined

A **user-defined** feature is created by the programmer.

Examples:

```python
def calculate_total():
    ...

class Product:
    ...
```

---

## Dunder Methods / Magic Methods

**Dunder** means **double underscore**.

Dunder methods have names beginning and ending with two underscores:

```python
__init__
__str__
__len__
```

They are also called **magic methods**.

The familiar:

```python
__init__()
```

is used when initializing objects.

Dunder methods allow Python objects to participate in language operations such as operators and built-in behavior.

Chapter 17 covers them in much more detail.

---

## Modules and Packages

## Module

A **module** is a Python program/file that another Python program can import.

For example:

```text
spam.py
```

can be imported:

```python
import spam
```

A module can contain:

* functions
* classes
* variables
* other top-level code

The Python Standard Library is a collection of modules that come with Python.

---

## Package

A **package** is a collection of modules organized in a directory.

Traditionally, a Python package is identified by the presence of:

```text
__init__.py
```

inside the directory.

A package can contain:

```text
package/
├── __init__.py
├── module_a.py
├── module_b.py
└── subpackage/
    └── ...
```

Packages can therefore contain modules and other packages.

---

## Callables and First-Class Objects

## Callable

A **callable** is an object that can be called using:

```python
()
```

For example:

```python
def hello():
    print("Hello!")

hello()
```

Functions are callable objects.

Classes are also callable:

```python
datetime.date(2020, 1, 1)
```

Calling a class creates an instance and runs its initialization process.

---

## First-Class Functions

Functions are **first-class objects** in Python.

This means functions can be:

* stored in variables
* passed as arguments
* returned from functions
* treated like other objects

Example:

```python
def spam():
    print("Spam!")


eggs = spam
eggs()
```

`eggs` and `spam` now refer to the same function object.

Such alternative names are called **aliases**.

Functions can also be passed to other functions:

```python
def call_twice(func):
    func()
    func()


call_twice(spam)
```

This is one of the foundations of higher-order functions and functional programming.

---

## Statements vs. Expressions

## Expression

An **expression** is an instruction that evaluates to a single value.

Examples:

```python
2 + 2
```

evaluates to:

```python
4
```

Other expressions:

```python
len(name)
name == "Zophie"
len(name) > 4
name.isupper()
```

A value by itself can also be an expression.

---

## Statement

A **statement** is an instruction that performs an action rather than simply evaluating to a value.

Examples:

```python
if
for
def
return
```

A useful mental distinction:

```text
Expression → produces/evaluates to a value

Statement  → performs an instruction
```

The distinction is important when communicating about Python code, even though beginners often use the terms interchangeably.

---

## Block vs. Body

A **block** is a group of indented code associated with a statement.

Example:

```python
if name == "Zophie":
    print("Hello!")
    print("Nice to see you.")
```

The indented code forms the block/body associated with the `if`.

Python requires indentation to define these groups.

The official Python documentation more precisely uses terms such as **clause**, **suite**, and **body** in different contexts, so "block" is common programmer terminology but isn't always the formal documentation term.

---

## Variable vs. Attribute

## Variable

A **variable** is a name that refers to an object.

```python
spam = 42
```

`spam` is a variable/name referring to an object.

---

## Attribute

An **attribute** is a name associated with an object and accessed using dot notation.

```python
spam.year
spam.month
```

For example:

```python
import datetime

spam = datetime.datetime.now()

spam.year
spam.month
```

Here:

```text
spam → variable
year → attribute
month → attribute
```

A useful rule from the chapter:

> An attribute is essentially a name following a dot.

Methods are also considered attributes of the objects they are associated with.

---

## Function vs. Method

## Function

A **function** is callable code that runs when called.

Examples:

```python
len("Hello")
```

and:

```python
math.sqrt(25)
```

---

## Method

A **method** is a function or callable associated with a class/object.

Example:

```python
"Hello".upper()
```

`upper()` is a string method.

Compare:

```python
len("Hello")       # function
"Hello".upper()    # method
```

Important:

> A dot does not automatically mean something is a method.

For example:

```python
math.sqrt(25)
```

uses dot notation, but `sqrt()` is a function associated with the `math` module, not a method associated with a class instance.

---

## Iterable vs. Iterator

## Iterable

An **iterable** is an object that can provide its items one at a time for iteration.

Examples include:

```python
list
tuple
str
range
dict
set
file
```

Example:

```python
for item in ["cat", "dog", "moose"]:
    print(item)
```

---

## Iterator

An **iterator** is the object that keeps track of the current position during iteration.

Python's `for` loop effectively uses:

```python
iter()
```

to obtain an iterator and:

```python
next()
```

to retrieve each next item.

Conceptually:

```text
Iterable
   ↓
iter()
   ↓
Iterator
   ↓
next()
   ↓
next item
```

Example:

```python
items = ["cat", "dog", "moose"]

iterator = iter(items)

next(iterator)  # "cat"
next(iterator)  # "dog"
next(iterator)  # "moose"
```

An iterator can only be exhausted once. To iterate over the iterable again, create another iterator with `iter()`.

---

## Exceptions vs. Errors

The chapter distinguishes several categories of programming errors.

## Syntax Error

A **syntax error** occurs when Python cannot parse the source code as valid Python syntax.

Example:

```python
print("Hello"
```

A missing parenthesis causes a `SyntaxError`.

Syntax errors are also called **parsing errors**.

Normally, they are detected before the program executes.

---

## Runtime Error

A **runtime error** occurs while the program is running.

Example:

```python
10 / 0
```

produces:

```text
ZeroDivisionError
```

Other runtime failures can involve:

* missing files
* invalid operations
* unavailable resources

Runtime errors can often be handled using:

```python
try:
    ...
except:
    ...
```

The traceback shows where Python detected the failure, but that location isn't necessarily the original cause of the bug.

---

## Semantic Error

A **semantic error**, also called a **logical error**, occurs when the program runs successfully but does something different from what the programmer intended.

Example:

```python
print("The sum is", "4" + "2")
```

Output:

```text
The sum is 42
```

The program doesn't crash, but the intended mathematical result was not produced.

So:

```text
Syntax error   → code structure is invalid

Runtime error  → program fails while running

Semantic error → program runs but does the wrong thing
```



---

## Parameters vs. Arguments

## Parameter

A **parameter** is a variable name defined in a function definition.

```python
def greeting(name, species):
    ...
```

Here:

```text
name
species
```

are parameters.

---

## Argument

An **argument** is the actual value supplied when calling the function.

```python
greeting("Zophie", "cat")
```

Here:

```text
"Zophie" → argument for name
"cat"    → argument for species
```

Mental model:

```text
Function definition:
def greeting(name, species):
             ↑       ↑
         parameters


Function call:
greeting("Zophie", "cat")
          ↑          ↑
       arguments
```



---

## Properties vs. Attributes

In Python, **attribute** and **property** are related but not identical terms.

An **attribute** is a name associated with an object.

A **property** is a Python mechanism that allows getter/setter-like behavior while providing attribute-style syntax.

Properties are covered in more detail later in the book, especially Chapter 17.

---

## Bytecode vs. Machine Code

## Machine Code

**Machine code** consists of instructions that the CPU can execute directly.

A compiled program consisting of machine code is called a **binary**.

---

## Bytecode

**Bytecode** is an intermediate form of instructions executed by a software interpreter rather than directly by the CPU.

Python source code in CPython is compiled into Python bytecode.

Bytecode can be stored in:

```text
.pyc
```

files.

Conceptually:

```text
Python source code
        ↓
    CPython
        ↓
   Python bytecode
        ↓
Python interpreter
        ↓
      CPU
```

This is different from compiling directly to CPU machine code.

---

## Script vs. Program

The distinction between **script** and **program** is not strict.

A script is generally a program intended to automate a task or be executed directly, but the terms overlap.

The distinction is partly historical and contextual.

---

## Scripting Language vs. Programming Language

The distinction is also vague.

A common historical distinction is:

* scripting languages are often interpreted or used for automation
* programming languages are sometimes associated with compiled programs

But this distinction doesn't accurately describe Python.

Python is commonly called a **scripting language**, even though CPython performs a compilation step to bytecode when running Python code.

Therefore:

> All scripts are programs, and scripting languages are programming languages.

---

## Library vs. Framework vs. SDK vs. Engine vs. API

These terms are related but describe different concepts.

## Library

A **library** is reusable code that your program calls to perform specific tasks.

Conceptually:

```text
Your program
     ↓
calls
     ↓
Library
```

The flow is primarily controlled by your application.

---

## Framework

A **framework** provides a larger structure for building an application.

A key idea is **Inversion of Control (IoC)**:

> "Don't call us, we'll call you."

Instead of your application controlling everything, the framework calls parts of your code at appropriate times.

For example, a web framework can call your request-handling function when an HTTP request arrives.

---

## SDK

**SDK** = **Software Development Kit**

An SDK is a collection of tools, libraries, and documentation designed to help developers build applications for a particular platform or system.

Examples from the chapter include:

```text
Android SDK
iOS SDK
Java Development Kit (JDK)
```

---

## Engine

An **engine** is a relatively large, self-contained system that performs complex tasks and can be controlled by external software.

Examples:

```text
Game engine
Physics engine
Recommendation engine
Database engine
Search engine
```

Your program generally calls the engine to perform substantial functionality.

---

## API

**API** = **Application Programming Interface**

An API is the public-facing interface through which software interacts with a library, SDK, framework, engine, or service.

It specifies things such as:

* what operations are available
* how to call them
* what inputs they expect
* what results they provide

For example, an HTTP API can allow programs to interact with an online service without a human using its web interface.

---

## Relationship

A useful mental model:

```text
Library
   │
   └── reusable code you call

Framework
   │
   └── application structure that can call your code

SDK
   │
   └── toolkit for developing for a platform/system

Engine
   │
   └── large system performing complex operations

API
   │
   └── public interface used to interact with software
```

These concepts can overlap; the chapter specifically notes that their distinctions are subtle.

---

## Commonly Confused Terms — Quick Reference

| Term 1        | Term 2         | Main distinction                                                             |
| ------------- | -------------- | ---------------------------------------------------------------------------- |
| Statement     | Expression     | Statement performs an instruction; expression evaluates to a value           |
| Function      | Method         | Method is associated with a class/object                                     |
| Parameter     | Argument       | Parameter is in function definition; argument is supplied in call            |
| Variable      | Attribute      | Variable is a name; attribute is a name accessed through an object           |
| Attribute     | Property       | Property is a mechanism for controlled attribute-style access                |
| Iterable      | Iterator       | Iterable can provide items; iterator tracks iteration state                  |
| Syntax error  | Runtime error  | Syntax invalid before/while parsing; runtime failure occurs during execution |
| Runtime error | Semantic error | Runtime failure vs. program runs but does the wrong thing                    |
| Bytecode      | Machine code   | Bytecode is executed by software; machine code by CPU                        |
| Library       | Framework      | Application calls library; framework can call application code               |
| Script        | Program        | Overlapping terms; distinction is contextual                                 |
| Object        | Instance       | Instance emphasizes an object's relationship to a class                      |
| Index         | Key            | Index identifies a sequence position; key identifies a mapping value         |

---

## Mental Model of Python Terms

A Python program can be viewed roughly like this:

```text
Python Program
│
├── Identifiers
│   ├── Variables
│   ├── Functions
│   ├── Classes
│   └── Attributes
│
├── Keywords
│
├── Literals
│
├── Statements
│
└── Expressions
```

The program operates on **objects**:

```text
Object
├── Value
├── Data Type
└── Identity
```

Objects can be organized into broader categories:

```text
Objects
├── Built-in
├── User-defined
├── Containers
│   ├── Sequences
│   ├── Mappings
│   └── Sets
└── ...
