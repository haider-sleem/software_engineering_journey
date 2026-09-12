# Chapter 5: Finding Code Smells

> *Beyond the Basic Stuff with Python — Al Sweigart*

---

## What Are Code Smells?

Code smells are patterns that warn about potential problems, unnecessary complexity, or poor readability in code. They are signals that a better way of writing the code may exist — not necessarily a bug or crash waiting to happen.

---

## Code Smell: Duplicate Code

Copying and pasting code creates multiple places to update, which easily leads to inconsistent changes and bugs. Deduplicate logic by organizing it into functions, loops, or parameters.

---

## Code Smell: Magic Numbers and Values

Using raw, unexplained numbers or strings makes code confusing and vulnerable to silent typos. Replace them with descriptive constants. This improves readability and, in some cases, makes typos easier to detect because misspelled constant names can raise errors such as `NameError`.

---

## Code Smell: Commented-Out Code

Leaving old commented-out code in the source creates confusion — its purpose and necessity become unclear over time. Use version control (Git) instead of commenting out code you might want later.

---

## Code Smell: Dead Code

Unreachable or logically impossible-to-run code misleads programmers into thinking it's active. Remove it.

**Exception — Stubs:** placeholders like `pass` or `raise NotImplementedError` are acceptable. They safely outline future code without failing silently.

---

## Code Smell: Variables with Numeric Suffixes

Names like `password1` and `password2` fail to explain what the variables represent or how they differ.

- Use descriptive names instead: `password` and `confirm_password`, or `start_x` and `end_x`.
- If there are more than two related values, use a collection (list or dict) rather than an endless series of numbered variables.

---

## Code Smell: Classes That Should Just Be Functions

Avoid creating classes or static-only methods just to wrap a single function call or to mimic OOP habits from other languages. Python prefers simple functions and modules — no unnecessary boilerplate.

---

## Code Smell: Nested Comprehensions

Python supports list, set, and dictionary comprehensions as concise ways to transform iterables — but use them with caution. Deeply nested comprehensions or multiple `for` expressions crammed into one line pack too much complexity and hurt readability. A standard multi-line `for` loop is often clearer.

---

## Code Smell: Empty `except` Blocks

Leaving an `except` block empty with `pass` hides critical errors and allows the program to continue with invalid data — which can be worse than letting it crash.

**Error messages** should be user-friendly: written for humans, clearly explaining what went wrong and how to fix it.

---

## Code Smell Myths Worth Knowing

### Single Return Statement

The rule requiring exactly one `return` at the end of a function is **outdated**. Multiple `return` statements are fine and often prevent convoluted `if-else` logic.

### Single `try` Statement

Restricting functions to one `try-except` block that wraps everything leads to unnecessary complexity. Multiple localized `try` blocks are cleaner.

### Flag Arguments

Passing a boolean flag to a function is **not inherently bad**. A function should not perform completely opposite tasks based on a flag — but using flags for minor behavioral tweaks (like sort direction) is a valid, practical pattern.

### Global Variables

Mutable global variables complicate debugging by making state tracking difficult across large programs. However, **global constants are fine**, and global variables can still be useful in smaller scripts or for application-wide settings.

### Comments Are Unnecessary

This is a myth. Poorly written or outdated comments can be unhelpful, but claiming all comments are unnecessary goes too far. Comments provide high-level context and intent that code names alone cannot convey. Most codebases suffer from too few comments, not too many.

---

## Print Debugging vs. Professional Alternatives

| Approach | Problem |
|----------|---------|
| `print()` statements | Slow, requires multiple reruns, risks leaving forgotten debug output |
| **Interactive debugger** | Inspect code line by line without modifying it |
| **`logging` module** | Records tracking messages cleanly to separate files, doesn't clutter normal output |