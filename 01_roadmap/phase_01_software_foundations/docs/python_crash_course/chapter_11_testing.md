# Chapter 11: Testing

---

## Why Test?

- Testing verifies that code behaves as expected.
- Tests catch bugs before users encounter them.
- Tests protect existing behavior when code is improved or changed.
- Passing tests give confidence that new changes did not break existing behavior (**regression prevention**).

> **Golden Rule:** When a test fails, fix the implementation — never alter the test to force a pass.

---

## Setup: Installing pytest

pytest is a third-party library, not part of Python's standard library.

```bash
python -m pip install --upgrade pip      # update pip first
python -m pip install --user pytest      # install pytest for current user
```

- `--upgrade` updates an already-installed package.
- `--user` installs for the current user only.

> Do not blindly trust every third-party package.

---

## Unit Tests and Test Cases

| Term | Definition |
|------|-----------|
| **Unit Test** | Checks one specific part of a function's behavior |
| **Test Case** | A group of unit tests that covers a function in different situations |
| **Full Coverage** | Writing tests that cover the full range of situations and behaviors a function is expected to handle |

Full coverage can be difficult for large projects — focus on **critical behavior** first.

---

## Writing a Test

- Test function names must start with `test_`.
- The name should clearly describe what behavior is being tested.
- pytest finds and runs test functions automatically.

**Pattern:**
1. Call the function being tested.
2. Store the result.
3. Use `assert` to check the result.

```python
def test_first_last_name():
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"
```

### Reading pytest Output

- `.` → test passed
- `F` → test failed
- The failure report shows where the problem occurred.
- The short test summary gives a quick overview of failures.

---

## Common Assertions

```python
assert a == b
assert a != b
assert a  # passes if a is truthy
assert not a  # passes if a is falsy
assert element in lst
assert element not in lst
```

> In Python, `''` evaluates to `False`; any non-empty string evaluates to `True`.

---

## Input in Tests

- Tests should use fixed test data instead of `input()`.
- pytest captures standard input by default — interactive input causes an `OSError`.
- Interactive input makes automated tests difficult and unreliable.
- Test functions should provide their own controlled inputs directly.

---

## Optional Parameters

- Parameters with default values must be placed **at the end** of the function signature.
- Making a parameter optional can preserve existing calls that do not provide that argument.

```python
def get_formatted_name(first, last, middle=""):
    if middle:
        return f"{first} {middle} {last}".title()
    return f"{first} {last}".title()
```

---

## Testing Classes

Testing a class follows the same idea as testing a function.

**Pattern:**
1. Create an instance.
2. Perform an action (call a method).
3. Check the resulting state with `assert`.

```python
survey = AnonymousSurvey(question)
survey.store_response("English")
assert "English" in survey.responses
```

- Test one response first, then test multiple responses.
- Use a loop to store several responses, then verify all were stored.

```bash
pytest                  # run all discovered tests
pytest test_survey.py   # run one specific file
```

---

## Fixtures

A **fixture** prepares a shared resource that multiple tests need, avoiding repeated setup code.

- Created with `@pytest.fixture`.
- The fixture's return value is passed to the test through the matching parameter name.
- pytest normally runs the fixture function separately for each test function that uses it.

```python
@pytest.fixture
def survey():
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)


def test_single_response(survey):
    survey.store_response("English")
    assert "English" in survey.responses
```

- Use fixtures when several tests share the same setup.
- You do not need fixtures when tests are still simple — **repeated test code is better than no tests**.