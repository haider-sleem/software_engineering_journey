## Chapter 3: Repeating Code


## Technical Note: Using Multiple Arguments in `print()`

When calling `print()`, using commas to separate multiple arguments is more convenient than string concatenation (using the `+` operator).

**Key benefits:**
- **Handles different data types:** `print()` can print a string and an integer as separate arguments without manually converting the integer with `str()`.
- **Automatic spacing:** Python inserts a space between arguments by default, which keeps the code cleaner and avoids manual formatting inside string literals.

**Example:**
```python
print(len(secret_word), "iterations, coming right up!")
````

This is preferred over `print(str(len(secret_word)) + " iterations...")` because it's more readable and less likely to cause type errors.

---

## "Pythonic" Swap: Tuple Unpacking

To swap two values, Python uses tuple unpacking. This lets you exchange the contents of two variables (or list elements) at the same time, without needing a temporary "helper" variable.

**Syntax:** `a, b = b, a`

**Example with numbers:**

If we have:

```python
cups = [1, 0, 0]
```

This means:

* `cups[0]` is `1`
* `cups[1]` is `0`

When we run this line:

```python
cups[0], cups[1] = cups[1], cups[0]
```

1. Python first looks at the right side: `(0, 1)`.
2. Then it assigns these values to the left side, in order:

   * `0` goes into `cups[0]`
   * `1` goes into `cups[1]`

**Result:** `cups = [0, 1, 0]`

---

## Logic Note: Substring vs. Subsequence

When working with text, it's important to tell apart two ways of searching for a word inside a string:

* **Substring:** letters that are exactly next to each other, with no gaps (example: `HONI` inside `XXHONIYY`).
* **Subsequence:** letters that appear in the same order, but don't have to be next to each other (example: `HONI` inside `H-X-O-X-N-X-I`).

**Rule for the Magnus problem:**
The problem asks for a **subsequence**. This means we look for the letters of `HONI` in order, from left to right, and ignore any other letters in between.

---

## The "Greedy" Selection & Pattern Matching

To solve this problem efficiently, we use a **greedy algorithm** combined with **pattern matching**.

**The idea:**

* **Greedy:** take the first correct match as soon as you see it. As soon as you find `H`, take it right away and start looking for the next letter (`O`). Waiting doesn't help here — it only wastes opportunities.
* **Pattern matching:** we watch for a specific pattern (`H → O → N → I`) and ignore any letter that doesn't fit the pattern.

---

## State Tracking

To make the code "remember" how far it has gone through the word, we use a variable often called `target` — the letter we're currently looking for.

**Example:**

If the word is: `PROHODNIHODNIK`

We start with `target = "H"`:

1. We go letter by letter. As soon as we find `H`, we change the target: `target = "O"`.
2. We ignore other letters until we find `O`, then change the target: `target = "N"`.
3. As soon as we find `N`, we change the target: `target = "I"`.
4. As soon as we find `I`, we've completed one full word (Block 1):

   * `honi_count += 1`
   * Reset the target back to `target = "H"` to start looking for the next word.

**Result:** the code only goes through the word once (`O(n)`), which makes it fast and well suited for programming contests.

---

## Input Management (Handling Data)

* **`input()`:** reads only one line at a time, and stops when it hits a newline (`\n`). If the input spans multiple lines, there are a few ways to read it — for example, using a `for` loop, or reading everything at once with `sys.stdin.read()`.

* **`sys.stdin.read()`:** a tool from the `sys` library that reads all the input at once, as one large block of text. When the input is large, this can be faster than calling `input()` repeatedly, because it reduces the overhead of reading the input line by line.

---

## Variable Scope After Loops

In Python, a variable used in a `for` loop (like `i`) does not disappear when the loop ends. It keeps the last value it had during the final iteration.

**Note:** The loop variable remains available after the loop and keeps its last assigned value, as long as the loop ran at least once.

---

## Iterating: By Element vs. By Index

There are two ways to loop through a string or a list, and each has its own use:

1. **`for item in sequence` (by element)**

   * Use it when: you only care about the value of each item.
   * Pros: simple, clean code.

2. **`for i in range(len(sequence))` (by index)**

   * Use it when: you need the position (index) of the item.
   * Pros: lets you "look around" the current item, like checking the previous character (`sequence[i-1]`) or the next one (`sequence[i+1]`).

---

## Processing a String Directly vs. Using `.split()`

Going through a string directly (character by character) can avoid creating a new list with `.split()`, which may reduce memory use — especially with large input.

* **Data splitting (the `.split()` method):** creates a new list in memory and copies parts of the string into it. This uses extra memory and extra time to "cut" the data.

* **Index-based processing (`range(len())`):** uses the string's indices to access its characters without creating a new list with `.split()`. This can use less memory and be faster, especially with very large inputs.

> **Note:** review the two solutions for **DMOJ problem coci12c5p1 (Ljestvica)** in `Ch03_REPEATING_CODE.py`.

```

