"""
Grokking Data Structures — Chapter 2
Static Arrays: Building Your First Data Structure

A complete learning implementation that follows the conceptual story
of Chapter 2:

1. Static arrays
2. Indexing
3. Fixed capacity
4. Left-justified arrays
5. Encapsulation
6. Unsorted arrays
7. Insert
8. Delete
9. Search
10. Traversal
11. Arrays in action: statistics
12. Collections
13. Multidimensional arrays
"""

from array import array


# ============================================================
# PART 1 — BUILDING A STATIC ARRAY
# ============================================================


class StaticArray:
    """
    A small wrapper that behaves like a fixed-size array.

    The underlying Python array is created with a fixed capacity.
    Once created, the capacity cannot be changed.
    """

    def __init__(self, capacity: int, typecode: str = "l"):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")

        self._data = array(typecode, [0]) * capacity

    def __len__(self) -> int:
        """Return the fixed capacity of the array."""
        return len(self._data)

    def __getitem__(self, index: int):
        """Access an element by index."""
        self._validate_index(index)
        return self._data[index]

    def __setitem__(self, index: int, value):
        """Assign a value to an index."""
        self._validate_index(index)
        self._data[index] = value

    def _validate_index(self, index: int) -> None:
        """
        Validate an index.

        Unlike normal Python lists, we deliberately don't allow
        negative indexes because this is meant to demonstrate
        a traditional static array.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= len(self._data):
            raise IndexError(f"Index {index} out of range.")

    def __str__(self) -> str:
        return str(self._data.tolist())


# ============================================================
# PART 2 — UNDERSTANDING INDEXING
# ============================================================

print("========== STATIC ARRAY ==========")

numbers = StaticArray(5)

print("Capacity:", len(numbers))

numbers[0] = 10
numbers[1] = 20
numbers[2] = 30
numbers[3] = 40
numbers[4] = 50

print("Array:", numbers)

print("Element at index 0:", numbers[0])
print("Element at index 2:", numbers[2])
print("Element at index 4:", numbers[4])


# ============================================================
# PART 3 — WHY DO WE NEED TO KNOW WHICH CELLS ARE MEANINGFUL?
# ============================================================

"""
Suppose the array has capacity 10 but currently contains only
3 meaningful elements.

We don't want to confuse the unused cells with actual data.

Therefore, we maintain a separate "size" representing the
number of meaningful elements.

The chapter uses a left-justified representation:

[10, 20, 30, ?, ?, ?, ?, ?, ?, ?]
  ^^^^^^^^^
  meaningful data

size = 3
capacity = 10
"""


# ============================================================
# PART 4 — UNSORTED ARRAY
# ============================================================


class UnsortedArray:
    """
    An unsorted array built on top of StaticArray.

    Important distinction:

        capacity -> total space available
        size     -> number of meaningful elements

    The array is left-justified:

        [data, data, data, ?, ?, ?, ...]

    We don't care about the order of elements.
    """

    def __init__(self, max_size: int, typecode: str = "l"):
        self._array = StaticArray(max_size, typecode)
        self._max_size = max_size
        self._size = 0

    def __len__(self) -> int:
        """
        Return the number of meaningful elements,
        not the total capacity.
        """
        return self._size

    def capacity(self) -> int:
        """Return the maximum number of elements."""
        return self._max_size

    def __getitem__(self, index: int):
        """Access only meaningful elements."""
        self._validate_used_index(index)
        return self._array[index]

    def __setitem__(self, index: int, value):
        """Modify only meaningful elements."""
        self._validate_used_index(index)
        self._array[index] = value

    def insert(self, value) -> None:
        """
        Add an element at the first unused position.

        Because order doesn't matter, we simply append it
        to the logical end of the array.
        """
        if self._size >= self._max_size:
            raise ValueError("The array is already full.")

        self._array[self._size] = value
        self._size += 1

    def delete_at(self, index: int) -> None:
        """
        Delete an element by index.

        Because this is an UNSORTED array, we don't care about
        preserving order.

        Therefore:

            target <- last element
            size--

        This avoids shifting all following elements.
        """

        if self._size == 0:
            raise ValueError("Cannot delete from an empty array.")

        self._validate_used_index(index)

        # Move the last meaningful element into the deleted position.
        self._array[index] = self._array[self._size - 1]

        # The logical size decreases.
        self._size -= 1

    def find(self, target):
        """
        Linear search.

        Return the index of the first occurrence.
        Return None if the value doesn't exist.
        """

        for index in range(self._size):
            if self._array[index] == target:
                return index

        return None

    def delete(self, target) -> None:
        """
        Delete the first occurrence of a value.

        First:
            search for the value

        Then:
            delete it by index
        """

        index = self.find(target)

        if index is None:
            raise ValueError(f"Value {target} was not found.")

        self.delete_at(index)

    def traverse(self, callback) -> None:
        """
        Apply callback to every meaningful element.
        """

        for index in range(self._size):
            callback(self._array[index])

    def _validate_used_index(self, index: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} is outside the populated portion.")

    def __str__(self) -> str:
        values = [self._array[index] for index in range(self._size)]

        return str(values)


# ============================================================
# PART 5 — LET'S ACTUALLY USE OUR UNSORTED ARRAY
# ============================================================

print("\n========== UNSORTED ARRAY ==========")

products = UnsortedArray(5)

print("Capacity:", products.capacity())
print("Current size:", len(products))

products.insert(100)
products.insert(200)
products.insert(300)

print("After inserting 3 elements:")
print(products)

print("Size:", len(products))
print("Capacity:", products.capacity())


# ============================================================
# PART 6 — INSERTION
# ============================================================

print("\n========== INSERTION ==========")

products.insert(400)

print("After inserting 400:")
print(products)

products.insert(500)

print("After inserting 500:")
print(products)

print("Size:", len(products))
print("Capacity:", products.capacity())


# ============================================================
# PART 7 — WHAT HAPPENS WHEN THE ARRAY IS FULL?
# ============================================================

print("\n========== FULL ARRAY ==========")

try:
    products.insert(600)
except ValueError as error:
    print("Error:", error)


# ============================================================
# PART 8 — DELETE
# ============================================================

print("\n========== DELETE ==========")

numbers = UnsortedArray(10)

for number in [10, 20, 30, 40, 50]:
    numbers.insert(number)

print("Before deletion:")
print(numbers)

print("\nDelete index 1 (value 20):")

numbers.delete_at(1)

print("After deletion:")
print(numbers)

"""
Notice what happened:

Before:

[10, 20, 30, 40, 50]

Delete index 1.

Instead of shifting:

[10, 30, 40, 50]

we use the last element:

[10, 50, 30, 40, 50]

and then reduce size to 4.

Logical array:

[10, 50, 30, 40]

The order changed.

But that's completely fine because this is an
UNSORTED array and order doesn't matter.
"""


# ============================================================
# PART 9 — SEARCH
# ============================================================

print("\n========== SEARCH ==========")

print("Current array:")
print(numbers)

index = numbers.find(30)

print("Index of 30:", index)

index = numbers.find(999)

print("Index of 999:", index)


# ============================================================
# PART 10 — DELETE BY VALUE
# ============================================================

print("\n========== DELETE BY VALUE ==========")

print("Before:", numbers)

numbers.delete(30)

print("After deleting 30:", numbers)


# ============================================================
# PART 11 — TRAVERSAL
# ============================================================

print("\n========== TRAVERSAL ==========")

print("Printing every element:")

numbers.traverse(print)


print("\nSquaring every element:")


def print_square(value):
    print(value * value)


numbers.traverse(print_square)


# ============================================================
# PART 12 — ARRAY ACCESS IS DIRECT
# ============================================================

print("\n========== DIRECT ACCESS ==========")

print("numbers[0] =", numbers[0])
print("numbers[1] =", numbers[1])

"""
This is one of the fundamental strengths of arrays:

Given an index, we can directly access the corresponding element.

Conceptually:

index
  ↓
[10][50][40]
 0   1   2

numbers[2] -> 40
"""


# ============================================================
# PART 13 — STATISTICS: COUNTING DIE ROLLS
# ============================================================

print("\n========== DICE STATISTICS ==========")

"""
Suppose we roll a die many times.

Possible values:

1 2 3 4 5 6

We create six counters:

index:      0  1  2  3  4  5
die face:   1  2  3  4  5  6
counter:    0  0  0  0  0  0

Because arrays use zero-based indexing:

face k -> counters[k - 1]
"""

counters = StaticArray(6)

rolls = [
    1,
    5,
    4,
    2,
    3,
    4,
    4,
    6,
    2,
    4,
    1,
    3,
    4,
    5,
    4,
]

for roll in rolls:
    counters[roll - 1] += 1

print("Counters:")

for index in range(len(counters)):
    print(f"Die face {index + 1}: {counters[index]} times")


# ============================================================
# PART 14 — FIND THE MOST FREQUENT VALUE
# ============================================================


def max_in_array(array_data):
    """
    Return:

        (index, maximum_value)

    Assumes the array is not empty.
    """

    if len(array_data) == 0:
        raise ValueError("Cannot find maximum of an empty array.")

    max_index = 0

    for index in range(1, len(array_data)):
        if array_data[index] > array_data[max_index]:
            max_index = index

    return max_index, array_data[max_index]


max_index, max_count = max_in_array(counters)

print("\nMost frequent die face:")
print("Face:", max_index + 1)
print("Frequency:", max_count)


# ============================================================
# PART 15 — FIND THE LEAST FREQUENT VALUE
# ============================================================


def min_in_array(array_data):
    """
    Return:

        (index, minimum_value)
    """

    if len(array_data) == 0:
        raise ValueError("Cannot find minimum of an empty array.")

    min_index = 0

    for index in range(1, len(array_data)):
        if array_data[index] < array_data[min_index]:
            min_index = index

    return min_index, array_data[min_index]


min_index, min_count = min_in_array(counters)

print("\nLeast frequent die face:")
print("Face:", min_index + 1)
print("Frequency:", min_count)


# ============================================================
# PART 16 — COLLECTIONS
# ============================================================

print("\n========== COLLECTION ==========")

"""
Imagine Mario has a binder that can hold a limited number
of baseball cards.

The order doesn't matter.

That makes an unsorted array a natural model.
"""

cards = UnsortedArray(5)

cards.insert(101)
cards.insert(102)
cards.insert(103)

print("Cards:")
cards.traverse(print)

print("\nFind Card B:")

card_index = cards.find("Card B")

print("Index:", card_index)

print("\nRemove Card B:")

cards.delete("Card B")

print(cards)


# ============================================================
# PART 17 — TRAVERSING OBJECTS (Standalone Example)
# ============================================================
#
# NOTE:
# Our UnsortedArray is built on array.array with a numeric
# typecode, so it can only hold numbers — that's the whole
# point of a "typed array".
#
# To demonstrate object traversal, we use a plain Python list
# here. This is a separate illustration, not part of the
# typed-array implementation.
#
# ============================================================

print("\n========== OBJECT COLLECTION ==========")


class Player:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} — age {self.age}")


players = [
    Player("Ali", 25),
    Player("Omar", 30),
    Player("Adam", 22),
]


def print_player(player):
    player.describe()


for player in players:
    print_player(player)

# ============================================================
# PART 18 — MULTIDIMENSIONAL ARRAYS
# ============================================================

print("\n========== MULTIDIMENSIONAL ARRAY ==========")

"""
An array can contain other arrays.

Conceptually:

[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

This is a 2D array / matrix.

Note:
    This example uses Python lists to represent a 2D array.
    It is a separate illustration and is not built on top of
    the StaticArray implementation above.
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Matrix:")

for row in matrix:
    print(row)

print("\nElement at row 1, column 2:")

print(matrix[1][2])

# ============================================================
# PART 19 — A SMALL REALISTIC EXAMPLE
# ============================================================

print("\n========== FINAL EXAMPLE ==========")

inventory = UnsortedArray(6)

inventory.insert(120)
inventory.insert(450)
inventory.insert(230)
inventory.insert(900)

print("Initial inventory:")
print(inventory)

print("\nSearching for product 230:")

product_index = inventory.find(230)

if product_index is not None:
    print(f"Product found at index {product_index}.")
else:
    print("Product not found.")


print("\nRemoving product 230:")

inventory.delete(230)

print("Inventory after deletion:")
print(inventory)

print("\nAdding new product 700:")

inventory.insert(700)

print(inventory)

print("\nTraversing inventory:")

inventory.traverse(print)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n========== CHAPTER 2 COMPLETE ==========")

print(
    """
The story:

Memory
   ↓
Static Array
   ↓
Indexing
   ↓
Fixed Capacity
   ↓
Track meaningful elements with size
   ↓
Left-justified representation
   ↓
Encapsulation
   ↓
UnsortedArray
   ↓
Insert
   ↓
Delete using the last element
   ↓
Linear Search
   ↓
Traversal
   ↓
Real applications
   ├── Statistics
   ├── Collections
   └── Multidimensional Arrays
"""
)
