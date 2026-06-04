 : الترتيب 

 دالة المستخدمين

 --------------------------------------------

# 1) DATA
products = {...}

# 2) HELPERS (أدوات مساعدة)
def select_product(): ...

# 3) VIEW (عرض)
def view_products(): ...

# 4) UPDATE LOGIC
def update_price(): ...
def update_quantity(): ...
def update_existing_product(): ...

# 5) CREATE
def add_new_product(): ...

# 6) MAIN FLOW
def adding_product(): ...

# 7) ENTRY POINT
if __name__ == "__main__":
    adding_product()
-----

### 💡 Backend Note: Returns vs. Exceptions

* **The Rule:** In professional backend development, `return` statements should only be used for successful operations.
* **Handling Cancellations or Exits:** If a process is cancelled, stopped, or encounters an issue, we should raise an **Exception** instead of returning different types (like `None` or `False`).
* **Why?** This keeps the function predictable, ensures it returns only one clean data type for success, and prevents messy `if-else` conditions for the caller.

-----

## 📌 Upcoming Fix for get_positive_number()
When I finish studying Error Handling, I will add this check inside the function to protect the converter:

```python
if converter not in (int, float):
    raise TypeError("converter must be int or float")

-----