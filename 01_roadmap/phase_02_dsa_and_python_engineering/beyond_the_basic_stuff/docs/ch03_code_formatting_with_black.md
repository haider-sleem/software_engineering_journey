# Chapter 3: Code Formatting With Black

---

## Philosophy and the Black Formatter

**Purpose of formatting:** improves readability, making code easier to maintain, debug, and extend.

**Black:** automatically formats code into a consistent style, saving time and ending arguments over style preferences. Described as *"the uncompromising code formatter"* — inspired by Henry Ford's line: *"You can have any color you want, as long as it's black."*

**PEP 8:** Python's widely used official style guide — Black's style is largely based on PEP 8.

> **Golden Rule:** Consistency within a project matters more than strictly following every single rule.

---

## Horizontal Spacing

### Indentation

- Use spaces instead of tabs for indentation. Mixing tabs and spaces inconsistently in the same indentation block can cause `TabError`.
- Standard: **4 spaces** per indentation level.

### Spacing Within a Line

| Rule | Correct | Incorrect |
|------|---------|-----------|
| Space around operators | `blanks = a + b` | `blanks=a+b` |
| No space before comma, one space after | `def spam(eggs, bacon, ham):` | `def spam(eggs , bacon , ham):` |
| No space around periods | `'Hello'.upper()` | `'Hello' . upper()` |
| No space before brackets/parentheses | `print('Hello')`, `spam[2]` | `print ('Hello')`, `spam [2]` |
| No space just inside brackets | `weights = [42.0, 3.14]` | `weights = [ 42.0, 3.14 ]` |

**Inline comments:** leave at least **two spaces** between the end of the code and `#`.

---

## Vertical Spacing

Blank lines organize code into logical blocks — like paragraphs in writing.

| Context | Blank Lines |
|---------|------------|
| Between top-level functions/classes | 2 |
| Between methods inside a class | 1 |
| Inside a function | Black doesn't enforce this — use your judgment to separate logical steps |

### Best Practices

- **Avoid semicolons** — don't combine multiple statements on one line.
- **Avoid single-line blocks** — don't put `if`/`for`/`while` bodies on the same line as the header.
- **One import per line** — keeps Git diffs clean.
- **Group imports into three sections**, separated by a blank line — this is a **PEP 8 recommendation; Black does not enforce import grouping**:
  1. Standard library (`math`, `os`, `sys`)
  2. Third-party packages (`requests`, `django`)
  3. Local project modules

---

## Installation and Execution

```bash
# Install
python -m pip install --user black      # Windows
python3 -m pip install --user black     # macOS/Linux/WSL

# Verify installation
python -m black
# Output: "No paths given. Nothing to do."
```

### Running Black

```bash
python -m black script.py               # single file
python -m black my_project_folder/      # whole directory, recursively
```

---

## Command-Line Options

### Line Length (`-l`)

Default: **88 characters** (10% more than the historical 80-character standard).

```bash
python -m black -l 120 script.py
```

### Preserving String Quotes (`-S`)

By default, Black converts `'` to `"`, except when that would require escaping quotes inside the string.

```bash
python -m black -S script.py            # skip quote conversion
python -m black -l 120 -S script.py     # combine options
```

---

## Safety and Advanced Controls

### Preview Changes (`--diff`)

Shows the changes Black would make without modifying the file:

```bash
python -m black --diff script.py
```

### Disabling Formatting for a Block

Use `# fmt: off` / `# fmt: on` to preserve intentional formatting (e.g., aligned constants):

```python
# fmt: off
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR   = 60 * SECONDS_PER_MINUTE
SECONDS_PER_DAY    = 24 * SECONDS_PER_HOUR
# fmt: on
```

---

## Key Takeaway: Syntax vs. Semantics

| Type | Examples | Who Handles It |
|------|---------|----------------|
| **Syntactic decisions** | Spacing, line limits, quote style | Automated — Black (formatter); Ruff (linting + formatter) |
| **Semantic decisions** | Meaningful naming, logic design, structure | Developer judgment — cannot be automated |