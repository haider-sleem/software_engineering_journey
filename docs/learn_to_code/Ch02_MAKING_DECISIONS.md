## Chapter 2: Making decisions

## Problem 3 — Winning Team (DMOJ ccc19j1, page 58)

A different way to solve this problem — a more professional approach than the book's solution, with analysis.

```python
def calculate_total(three, two, one):
    return three * 3 + two * 2 + one


def get_team_score(team_name):
    print(f"--- {team_name} ---")
    three = int(input())
    two = int(input())
    one = int(input())
    return calculate_total(three, two, one)


apple = get_team_score("Apples")
banana = get_team_score("Bananas")

if apple > banana:
    print("A")
elif banana > apple:
    print("B")
else:
    print("T")
```

### Analysis

#### 1. Clean Code principles

- **Clear naming**
  - `calculate_total` — clearly describes what it does: calculate the total score.
  - `get_team_score` — collects the team's input and returns the result produced by `calculate_total()`. It does not do the calculation itself.

- **Separation of concerns**
  - `calculate_total` handles the calculation.
  - `get_team_score` handles collecting input, and calls `calculate_total` to get the result.
  - Comparing results and printing the output is a separate final step.
  This makes it easy to change one part without affecting the others.

- **Avoiding repetition (DRY principle)**
  - The calculation logic isn't repeated for each team — it lives in one function, `calculate_total`.
  - Any change to how the score is calculated only needs to happen in one place.

- **Readability**
  - The code is organized logically: input → processing → decision → output.

#### 2. Design notes

- **Modularity & reusability:** each function does one job and can be reused. `calculate_total` works for any set of scores; `get_team_score` can be called for any team without repeating the input code.
- **On scalability:** adding a new score type only needs a small change inside `calculate_total`. But adding a third team would also require updating the final `if`/`elif`/`else` comparison — so this design makes the *calculation* easy to extend, not the *comparison logic*.

#### 3. Comparison with a simpler, quicker approach

- **The quick approach (a loop with direct input)**
  - Mixes input and processing together, which makes it harder to understand, reuse, test, or modify.

- **Why this solution is more professional**
  - Clear, organized, easier to modify and test, and reduces mistakes when editing.

- **When to use each approach**
  - The function-based approach → for projects, larger exercises, tests, and official competitions.
  - The direct approach → for very quick problems or trying out a short idea.

#### 4. Performance

- **Time complexity:** O(1) per team — the operations are fixed and limited.
- In practice, there's no meaningful performance difference from the direct approach here. The real benefit is **flexibility, maintainability, and clarity** — not speed.

#### 5. A general model for similar problems

1. **Identify the required input** — what data will come in?
2. **Separate the calculation/processing logic** — one function per calculation.
3. **Use small, reusable functions** — follow DRY.
4. **Handle the decision or comparison separately** — using `if`/`elif`/`else` or similar logic.
5. **Only produce the final output after all processing is done** — this reduces mistakes.

#### 6. Another example using the same approach

**Problem:** calculate test scores for students in 3 subjects and find who scored higher.

```python
def calculate_total(math, physics, chemistry):
    return math + physics + chemistry


def get_student_score():
    math = int(input())
    physics = int(input())
    chemistry = int(input())
    return calculate_total(math, physics, chemistry)


alice = get_student_score()
bob = get_student_score()

if alice > bob:
    print("Alice")
elif bob > alice:
    print("Bob")
else:
    print("Tie")
```

Same approach: separate functions, reusability, clean code.