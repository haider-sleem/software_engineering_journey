# Chapter 4: Choosing Understandable Names

---

## Introduction to Naming

Naming is considered one of the hardest problems in computer science. Names for variables, functions, and classes (**identifiers**) should be both **concise** and **descriptive**.

**Syntax vs. Semantics:** tools like Black or Ruff can automatically fix spacing (syntax), but they can't choose good variable names (semantics) — that's the programmer's job.

---

## Metasyntactic Variables

Temporary, generic names used only in tutorials and code examples — **never in real programs**.

| Context | Names | Origin |
|---------|-------|--------|
| Python-specific | `spam`, `eggs`, `bacon`, `ham` | Monty Python sketch |
| General programming | `foo`, `bar` | Military slang (FUBAR) |

---

## Casing Styles

Since Python identifiers can't contain spaces, multi-word names use one of these styles:

| Style | Format | Example |
|-------|--------|---------|
| **snake_case** | lowercase, underscore-separated | `my_variable_name` |
| **camelCase** | first word lowercase, rest capitalized | `myVariableName` |
| **PascalCase** | every word capitalized | `MyVariableName` |

Python's style guide recommends `snake_case` for variables — but the most important rule is **consistency** within a project.

---

## PEP 8 Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Modules | short, all lowercase | `utils` |
| Classes | PascalCase | `UserAccount` |
| Constants | UPPER_SNAKE_CASE | `MAX_SPEED` |
| Functions, methods, variables | lowercase_snake_case | `get_user_name` |
| Instance method's first argument | `self` | |
| Class method's first argument | `cls` | |
| Private attributes | leading underscore | `_password` |
| Public attributes | no leading underscore | `password` |

- Prefer ASCII letters for identifiers (PEP 8 recommendation).
- Python itself allows Unicode identifiers (e.g., `コンピューター` is syntactically valid) — but ASCII remains the convention for readability across teams.

---

## Name Length and Clarity

### Too Short

Avoid names that seem clear today but will confuse you (or others) in a few weeks:

| Problem | Example |
|---------|---------|
| Single letters | `g` — meaningless |
| Vague abbreviations | `mon` — monitor? month? monster? |
| Vague single words | `start` — start what? |

**Exceptions:** `i`, `j`, `k` for loop indexes; `x`, `y` for math coordinates.

### Don't Drop Letters

Never remove vowels or letters just to shorten a name.

| Bad | Good |
|-----|------|
| `memcpy` | `memory_copy` |
| `strcmp` | `string_compare` |
| `usr_nm` | `user_name` |

> **Rule of thumb:** if you can't pronounce it easily, it's not a good name. Prefer short English phrases: `number_of_trials` instead of `number_trials`.

### Too Long

- **Scope matters:** a global variable used across 10,000 lines needs a descriptive name (`annual_electric_bill_payment`); a local variable in a 5-line function can be short (`payment`).
- **Avoid redundant prefixes:** inside a `Cat` class, use `weight` instead of `catWeight`.
- **Avoid Hungarian Notation** — don't encode the data type in the name (`strName`, `iDays`). Modern IDEs already show you the type.

---

## Useful Prefixes and Suffixes

### Booleans — `is` / `has`

```python
is_vehicle = True
has_key()
```

Makes code read like plain English: `if item.has_key(): is_vehicle = True`.

### Units

Include the unit in the name to prevent dangerous bugs:

```python
weight_kg = 75  # not just "weight"
```

> NASA lost a $125 million spacecraft (Mars Climate Orbiter) due to a metric/imperial unit mix-up in the code.

---

## Avoid Unnecessary Sequential Numeric Suffixes

**Bad:** `payment1`, `payment2`, `payment3`

**Better (same thing repeated):** group into a list — `payments`

**Better (different things):** use descriptive words — `make_high_priority_payment()` instead of `make_payment1()`

---

## Make Names Searchable

Generic names like `email` or `num` produce too many false matches with `Ctrl-F` in large projects. Use specific names like `email_address` or `reply_to_address` for accurate, instant search results.

---

## Avoid Jokes, Puns, and Cultural References

Code is read by programmers worldwide, including non-native English speakers. A joke like naming a function `goose_download()` (to make it "go faster") stops being funny quickly and adds confusion.

> **Rule:** write names that are polite, direct, and humorless.

---

## Don't Overwrite Built-in Names

Avoid overwriting Python's built-in names. Python keywords (`if`, `for`, `class`, `return`, etc.) cannot be used as identifiers in the first place — Python raises a `SyntaxError`. The real risk discussed here is **overwriting built-in names** like `list`, `str`, `open`, `id`, `sum`, which are valid identifiers but shadow essential built-in functionality.

**Common names to avoid:** `list`, `set`, `str`, `max`, `min`, `open`, `type`, `id`, `sum`, `file`

```python
list = [1, 2, 3]  # breaks the built-in list() function for the rest of the scope
```

**File names:** don't name a `.py` file after an external library (e.g., `pyperclip.py`) — Python will import your file instead of the real library.

**How to test a name:** open the Python shell and type it.
- Returns `<built-in function ...>` → don't use it.
- Raises `NameError` → safe to use.

---

## The Worst Possible Variable Names

| Name | Why It's Bad |
|------|--------------|
| `data` | Literally all variables hold data |
| `var` | Like naming your dog "Dog" |
| `temp` | All variables are temporary |

Instead of `tempVarData`, name it for what it actually represents — e.g., `temperature_variance`.

---

## Why Does Naming Matter?

Computers don't care about variable names — they just run the code. **Names are for humans.**

```
Good names → Readable code → Easy to understand → Easy to change, update, fix
```

Choosing understandable names is a foundation of quality software engineering.