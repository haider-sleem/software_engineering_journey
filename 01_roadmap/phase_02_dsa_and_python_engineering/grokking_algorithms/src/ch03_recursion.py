# Chapter 3 - Recursion
# A small Warehouse Management System story


# Stage 1 - The warehouse has nested storage boxes.
# We want to find a product inside any box.

warehouse = {
    "Aisle 1": {
        "Shelf 1": {
            "box_101": ["barcode_1001", "barcode_1002"],
            "box_102": ["barcode_1003"],
        },
        "Shelf 2": {
            "box_201": ["barcode_1004"],
        },
    },
    "Aisle 2": {
        "Shelf 3": {
            "box_301": ["barcode_1005"],
            "box_302": ["barcode_1006"],
        }
    },
}


# Stage 2 - Recursive search
# A box can contain more boxes, so the function calls itself.


def find_product(storage: dict, target: str) -> str | None:
    """Recursively searches for a target barcode in nested storage.

    Args:
        storage (dict): Nested dicts representing the warehouse structure.
        target (str): The barcode to search for.

    Returns:
        str | None: The name of the box containing the target, or None.
    """
    for name, contents in storage.items():
        if isinstance(contents, dict):
            result = find_product(contents, target)

            if result is not None:
                return result

        elif target in contents:
            return name

    return None


print(find_product(warehouse, "barcode_1005"))


# Stage 3 - Base case and recursive case
# The function must know when to stop.


def countdown(number: int) -> None:
    """Prints numbers from `number` down to 1 using recursion.

    Args:
        number (int): The starting number for the countdown.

    Returns:
        None
    """
    print(number)

    # Base case: stop when we reach 1.
    if number <= 1:
        return

    # Recursive case: call the function with a smaller problem.
    countdown(number - 1)


countdown(5)


# Stage 4 - The call stack
# Each function call waits for the next call to finish.


def greet(name: str) -> None:
    """Greets a person and triggers the manager check.

    Args:
        name (str): The name of the person to greet.

    Returns:
        None
    """
    print(f"Hello, {name}!")

    greet_manager(name)

    print("Returning to the warehouse.")


def greet_manager(name: str) -> None:
    """Prints a manager check message for the given name.

    Args:
        name (str): The name of the person being checked.

    Returns:
        None
    """
    print(f"Manager checking {name}.")

    say_goodbye()


def say_goodbye() -> None:
    """Prints a goodbye message.

    Returns:
        None
    """
    print("Goodbye!")


greet("Haider")


# Stage 5 - Recursion uses the call stack
# Each call gets its own value of number.


def calculate_factorial(number: int) -> int:
    """Calculates the factorial of a number using recursion.

    Args:
        number (int): A positive integer.

    Returns:
        int: The factorial of `number`.
    """
    if number == 1:
        return 1

    return number * calculate_factorial(number - 1)


print(calculate_factorial(5))


# Stage 6 - Following the factorial step by step
#
# calculate_factorial(5)
#     5 * calculate_factorial(4)
#         4 * calculate_factorial(3)
#             3 * calculate_factorial(2)
#                 2 * calculate_factorial(1)
#                     return 1
#
# Then the calls return in reverse order:
#
# 2 * 1 = 2
# 3 * 2 = 6
# 4 * 6 = 24
# 5 * 24 = 120


# Stage 7 - Each recursive call has its own state


def process_orders(order_count: int) -> str:
    """Processes a given number of orders using recursion.

    Args:
        order_count (int): The number of orders to process.

    Returns:
        str: A summary string of all completed orders.
    """
    if order_count == 0:
        return "All orders processed."

    result = process_orders(order_count - 1)

    return f"Order {order_count} completed. {result}"


print(process_orders(3))


# Stage 8 - A recursive search can replace a manually managed pile.
# The call stack keeps track of the unfinished function calls.


def find_barcode(storage: list, target: str) -> str | None:
    """Recursively searches for a target barcode in nested storage.

    Args:
        storage (list): A list containing dicts and lists.
        target (str): The barcode to search for.

    Returns:
        str | None: The barcode if found, or None.
    """
    for item in storage:
        if isinstance(item, dict):
            result = find_barcode(item.values(), target)

            if result:
                return result

        elif isinstance(item, list):
            if target in item:
                return target

    return None


shelf_storage = [
    {"shelf_1": ["barcode_1001", "barcode_1002"]},
    {"shelf_2": ["barcode_1003"]},
]

print(find_barcode(shelf_storage, "barcode_1002"))


# Stage 9 - Recursion has a cost.
# Every recursive call uses memory on the call stack.


def count_boxes(boxes: list[str], index: int = 0) -> int:
    """Counts the number of boxes recursively.

    Args:
        boxes (list[str]): The list of boxes.
        index (int): The current index in the recursion.

    Returns:
        int: The total number of boxes.
    """
    if index == len(boxes):
        return 0

    return 1 + count_boxes(boxes, index + 1)


boxes = ["box_1", "box_2", "box_3", "box_4"]

print(count_boxes(boxes))


# Stage 10 - A loop can sometimes be simpler and use less stack memory.


def count_boxes_with_loop(boxes: list[str]) -> int:
    """Counts the number of boxes using an iterative loop.

    Args:
        boxes (list[str]): The list of boxes.

    Returns:
        int: The total number of boxes.
    """
    count = 0

    for _ in boxes:
        count += 1

    return count


print(count_boxes_with_loop(boxes))


# Stage 11 - Infinite recursion eventually reaches Python's recursion depth limit.
# In Python, this raises a RecursionError.
#
# def broken_countdown(number):
#     print(number)
#     broken_countdown(number - 1)  # No base case — never stops.
#
# broken_countdown(5)  # RecursionError: maximum recursion depth exceeded


# Stage 12 - Final warehouse story
# Use recursion when the structure of the problem naturally
# contains smaller versions of the same problem.


def search_storage(storage: list, target: str) -> str | None:
    """Recursively searches for a target barcode in a nested storage list.

    Args:
        storage (list): A list of dicts and lists representing storage.
        target (str): The barcode to search for.

    Returns:
        str | None: The barcode if found, or None.
    """
    for item in storage:
        if isinstance(item, dict):
            result = search_storage(item.values(), target)

            if result is not None:
                return result

        elif isinstance(item, list):
            for barcode in item:
                if barcode == target:
                    return barcode

    return None


storage = [
    {
        "shelf_1": [
            "barcode_1001",
            "barcode_1002",
        ]
    },
    {
        "shelf_2": [
            "barcode_1003",
            "barcode_1004",
        ]
    },
    {
        "shelf_3": [
            "barcode_1005",
            "barcode_1006",
        ]
    },
]

print(search_storage(storage, "barcode_1005"))
