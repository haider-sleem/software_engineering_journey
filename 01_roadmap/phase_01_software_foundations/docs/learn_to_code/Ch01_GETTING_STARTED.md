## Chapter 1: Getting Started

### Notes
- Started studying this book on: 2026-03-04
- Goal: master problem solving using Python.

---

## Problem 1 — 15c7p2

The task is to count the words in a text. Here are the tools needed to solve this problem:

- **`.upper()`**
  Used to make all letters in the text the same case (uppercase).
- **`.strip()`**
  Removes whitespace (spaces) only from the **beginning and end** of the text, not from inside it.
  Example: `"  hello world  ".strip()` → `"hello world"` (the space between the words stays).
- **`.count()`**
  `text.count(" ")` counts the number of spaces in the text, not the number of words directly.
  In this problem, `text.count(" ")` can be used to count the gaps between words, and from that we can work out the number of words, based on the assumptions of the problem about the shape of the input (keeping in mind the result will be one less than the number of words, since the last word has no space after it).
- **`.bit_length()`**
  Calculates how many **bits** an integer needs to be represented in binary.
  Example: `(5).bit_length()` → the result is `3`, because `5` in binary is `101` (3 bits).
- **Variables**
  Used to store values and reuse them.

---

## Problem 2 — dmopc14c5p1

Technical notes for the Core Drill problem (dmopc14c5p1):

- **Math formula:** The problem is a direct application of the cone volume formula: $V = \frac{1}{3} \pi r^2 h$.
- **Using `math.pi`:** Use `math.pi` instead of manually writing `3.14` to use Python's built-in approximation of π.
- **Translating the formula to code:** The formula translates directly into Python like this: `(math.pi * r**2 * h) / 3`.
- **Handling input:**
  Use `int(input())` to convert the text from `input` into an integer, so it can be used in calculations.
  `int()` accepts numbers even with extra spaces around them (like `int(" 42 ")`), but it raises a `ValueError` if the text contains non-numeric characters (like `int("42abc")`).
- **Decimal precision:** In Python, the `/` operator returns a `float`.
- **Code priority:** It's always better to write clear, readable code (Clean Code) instead of trying to "shorten" lines in search of performance gains that aren't necessary at this level.

---

## Chapter Exercises (page 57)

Completed the Chapter 1 problem solving exercises.