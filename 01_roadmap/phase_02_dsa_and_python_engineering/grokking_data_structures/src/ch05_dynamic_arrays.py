"""
Grokking Data Structures — Chapter 5
Dynamic Arrays: Handling Dynamically Sized Datasets

The story:

Static Array
     ↓
Fixed capacity becomes a problem
     ↓
Create a larger array when full
     ↓
But when should we resize?
     ↓
Double the capacity
     ↓
What about deletion?
     ↓
Shrink when only 1/4 is occupied
     ↓
Dynamic Array
"""

from array import array


# ============================================================
# PART 1 — THE STATIC ARRAY WE ALREADY KNOW
# ============================================================


class StaticArray:
    """
    A fixed-capacity array.

    Once created, its capacity cannot change.
    """

    def __init__(self, capacity: int, typecode: str = "l"):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")

        self._data = array(typecode, [0]) * capacity

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of range.")

        return self._data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of range.")

        self._data[index] = value

    def __str__(self):
        return str(self._data.tolist())


# ============================================================
# PART 2 — THE PROBLEM WITH STATIC ARRAYS
# ============================================================

print("========== THE STATIC ARRAY PROBLEM ==========")

numbers = StaticArray(4)

numbers[0] = 10
numbers[1] = 20
numbers[2] = 30
numbers[3] = 40

print("Array:", numbers)

print(
    """
The array is full.

What happens if we want to insert another element?

We cannot resize this array.
"""
)

try:
    numbers[4] = 50
except IndexError as error:
    print("Error:", error)


# ============================================================
# PART 3 — THE ONLY WAY TO GROW A STATIC ARRAY
# ============================================================

print("\n========== GROWING A STATIC ARRAY ==========")

"""
There is no magical operation that makes the existing
static array larger.

We must:

    1. Create a new, larger array.
    2. Copy the old elements.
    3. Add the new element.
    4. Throw away the old array.

Example:

Old:

[10, 20, 30, 40]

New:

[10, 20, 30, 40, ?, ?, ?, ?]

Then:

[10, 20, 30, 40, 50, ?, ?, ?]
"""

old_array = StaticArray(4)

for i, value in enumerate([10, 20, 30, 40]):
    old_array[i] = value

new_array = StaticArray(8)

for i in range(len(old_array)):
    new_array[i] = old_array[i]

new_array[4] = 50

print("Old array:", old_array)
print("New array:", new_array)


# ============================================================
# PART 4 — WHY NOT JUST ALLOCATE A HUGE ARRAY?
# ============================================================

print("\n========== THE MEMORY TRADE-OFF ==========")

print(
    """
Suppose we expect:

    usually     → 100 elements
    occasionally → 10,000 elements

If we allocate 10,000 cells from the beginning:

    most of the memory remains unused.

If we allocate only 100:

    we may repeatedly need to resize.

Therefore we have a trade-off:

    Allocate too much
        ↓
    waste memory

    Allocate too little
        ↓
    resize frequently

Dynamic arrays try to find a good compromise.
"""
)


# ============================================================
# PART 5 — WHAT IS A DYNAMIC ARRAY?
# ============================================================

print("\n========== DYNAMIC ARRAY ==========")

"""
A dynamic array is NOT a magical array whose physical
memory changes size.

Instead:

    DynamicArray
         │
         ▼
    StaticArray
         │
         ▼
    resize when necessary

The DynamicArray hides this process from the user.

From the user's point of view:

    insert(10)
    insert(20)
    insert(30)
    ...

just works.

The DynamicArray handles resizing behind the scenes.
"""


# ============================================================
# PART 6 — THE GROWING STRATEGY
# ============================================================

print("\n========== THE DOUBLING STRATEGY ==========")

"""
The chapter chooses:

    When the array becomes full:
        capacity *= 2

Example:

    capacity 1
        ↓
    capacity 2
        ↓
    capacity 4
        ↓
    capacity 8
        ↓
    capacity 16
        ↓
    ...

Why not increase by just one cell every time?

Because that would cause a resize almost every time
we add an element.

Doubling gives us a much better amortized performance.
"""


# ============================================================
# PART 7 — DYNAMIC ARRAY IMPLEMENTATION
# ============================================================


class DynamicArray:
    """
    An unsorted dynamic array.

    Important properties:

        _array
            underlying static array

        _capacity
            physical capacity

        _size
            number of meaningful elements

        _typecode
            required when creating a new underlying array
    """

    def __init__(self, initial_capacity: int = 1, typecode: str = "l"):
        if initial_capacity < 1:
            raise ValueError("Initial capacity must be at least 1.")

        self._array = StaticArray(initial_capacity, typecode)

        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def __len__(self):
        """
        Return the number of meaningful elements.
        """
        return self._size

    def capacity(self):
        """
        Return the physical capacity.
        """
        return self._capacity

    # ========================================================
    # PART 8 — RESIZE / DOUBLE
    # ========================================================

    def _double_size(self):
        """
        Create a new array with twice the capacity
        and copy all existing elements.
        """

        new_capacity = self._capacity * 2

        new_array = StaticArray(new_capacity, self._typecode)

        for i in range(self._size):
            new_array[i] = self._array[i]

        self._array = new_array
        self._capacity = new_capacity

    # ========================================================
    # PART 9 — INSERT
    # ========================================================

    def insert(self, value):
        """
        Insert at the end of the meaningful portion.

        If the array is full, double its capacity first.
        """

        if self._size == self._capacity:
            self._double_size()

        self._array[self._size] = value
        self._size += 1

    # ========================================================
    # PART 10 — ACCESS
    # ========================================================

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index outside the populated portion.")

        return self._array[index]

    # ========================================================
    # PART 11 — LINEAR SEARCH
    # ========================================================

    def find(self, target):
        """
        Dynamic array is unsorted.

        Therefore we use linear search.
        """

        for index in range(self._size):
            if self._array[index] == target:
                return index

        return None

    # ========================================================
    # PART 12 — DELETE
    # ========================================================

    def delete(self, target):
        """
        Delete the first occurrence of target.

        We preserve insertion order.

        Therefore, after finding the target, we shift all
        following elements one position to the left.
        """

        index = self.find(target)

        if index is None:
            raise ValueError(f"Unable to delete {target}: element not found.")

        # Shift elements left.
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._size -= 1

        # After deletion, check whether we should shrink.
        if self._capacity > 1 and self._size <= self._capacity / 4:
            self._halve_size()

    # ========================================================
    # PART 13 — RESIZE / HALVE
    # ========================================================

    def _halve_size(self):
        """
        Reduce capacity by half.

        This is triggered only when the array is at most
        one-quarter full.

        Example:

            capacity = 16
            size <= 4

        Then:

            new capacity = 8
        """

        new_capacity = self._capacity // 2

        # Never shrink below 1.
        new_capacity = max(1, new_capacity)

        # We must ensure the new capacity can still contain
        # all meaningful elements.
        if new_capacity < self._size:
            new_capacity = self._size

        new_array = StaticArray(new_capacity, self._typecode)

        for i in range(self._size):
            new_array[i] = self._array[i]

        self._array = new_array
        self._capacity = new_capacity

    # ========================================================
    # PART 14 — TRAVERSE
    # ========================================================

    def traverse(self, callback):
        """
        Visit every meaningful element.
        """

        for i in range(self._size):
            callback(self._array[i])

    # ========================================================
    # PART 15 — STRING REPRESENTATION
    # ========================================================

    def __str__(self):
        values = [self._array[i] for i in range(self._size)]

        return str(values)


# ============================================================
# PART 16 — WATCH THE ARRAY GROW
# ============================================================

print("\n========== WATCH THE ARRAY GROW ==========")

numbers = DynamicArray()

for value in [10, 20, 30, 40, 50, 60, 70, 80]:
    numbers.insert(value)

    print(
        f"Inserted {value:>2} | "
        f"size={len(numbers):>2} | "
        f"capacity={numbers.capacity():>2} | "
        f"data={numbers}"
    )


# ============================================================
# PART 17 — SEE THE DOUBLING
# ============================================================

print("\n========== CAPACITY GROWTH ==========")

numbers = DynamicArray()

for value in range(1, 17):
    previous_capacity = numbers.capacity()

    numbers.insert(value)

    current_capacity = numbers.capacity()

    if current_capacity != previous_capacity:
        print(f"Resize happened: {previous_capacity} -> {current_capacity}")


# ============================================================
# PART 18 — WHY NOT DOUBLE ON EVERY INSERT?
# ============================================================

print("\n========== WHY DOUBLE? ==========")

print(
    """
Suppose we have capacity 8.

If we increase by 1 every time:

    8 → 9 → 10 → 11 → 12 → ...

We repeatedly allocate a new array
and copy all existing elements.

That is expensive.

With doubling:

    8 → 16 → 32 → 64 → ...

There are fewer expensive resize operations.

The individual resize can still cost O(n),
but over many insertions the amortized cost
of insertion is O(1).
"""
)


# ============================================================
# PART 19 — THE SHRINKING PROBLEM
# ============================================================

print("\n========== THE SHRINKING PROBLEM ==========")

print(
    """
Now imagine:

    capacity = 8
    size     = 8

We add one element:

    capacity = 16
    size     = 9

Now suppose we immediately delete elements.

If we shrink as soon as the array becomes half empty:

    16 → 8

Then one more insertion could cause:

    8 → 16

Then deletion:

    16 → 8

Then insertion:

    8 → 16

...

We could get constant back-and-forth resizing.

This is called thrashing.
"""
)


# ============================================================
# PART 20 — SMARTER SHRINKING
# ============================================================

print("\n========== THE QUARTER RULE ==========")

print(
    """
Instead of shrinking when the array becomes half empty,
we wait until only ONE QUARTER of the capacity is used.

Example:

    capacity = 16

Shrink only when:

    size <= 4

Then:

    16 → 8

The new array is still half empty.

That gives us room for more insertions before another resize.
"""
)


# ============================================================
# PART 21 — WATCH THE ARRAY SHRINK
# ============================================================

print("\n========== WATCH THE ARRAY SHRINK ==========")

numbers = DynamicArray()

for value in range(1, 17):
    numbers.insert(value)

print(
    f"Before deletions: "
    f"size={len(numbers)}, "
    f"capacity={numbers.capacity()}, "
    f"data={numbers}"
)

while len(numbers) > 2:
    old_capacity = numbers.capacity()

    numbers.delete(numbers[len(numbers) - 1])

    new_capacity = numbers.capacity()

    if old_capacity != new_capacity:
        print(f"Shrink happened: {old_capacity} -> {new_capacity}")


# ============================================================
# PART 22 — SEARCH
# ============================================================

print("\n========== SEARCH ==========")

numbers = DynamicArray()

for value in [10, 20, 30, 40, 50]:
    numbers.insert(value)

print("Array:", numbers)

index = numbers.find(30)

print("Index of 30:", index)

index = numbers.find(999)

print("Index of 999:", index)


# ============================================================
# PART 23 — DELETE WHILE PRESERVING ORDER
# ============================================================

print("\n========== DELETE ==========")

numbers = DynamicArray()

for value in [10, 20, 30, 40, 50]:
    numbers.insert(value)

print("Before:", numbers)

numbers.delete(30)

print("After deleting 30:", numbers)

"""
Before:

[10, 20, 30, 40, 50]

After:

[10, 20, 40, 50]

The elements after 30 were shifted left.

This is different from the unsorted-array optimization
where we could replace the deleted element with the last one.

Here we deliberately preserve insertion order.
"""


# ============================================================
# PART 24 — WHAT IF WE DON'T CARE ABOUT ORDER?
# ============================================================

print("\n========== DELETE-BY-INDEX WITHOUT PRESERVING ORDER ==========")


class UnorderedDynamicArray(DynamicArray):
    def delete_at(self, index):
        """
        Delete by index without preserving order.

        Replace the deleted element with the last element.

        This can make deletion much cheaper.
        """

        if index < 0 or index >= self._size:
            raise IndexError("Index out of range.")

        # Replace deleted element with the last element.
        self._array[index] = self._array[self._size - 1]

        self._size -= 1

        if self._capacity > 1 and self._size <= self._capacity / 4:
            self._halve_size()


numbers = UnorderedDynamicArray()

for value in [10, 20, 30, 40, 50]:
    numbers.insert(value)

print("Before:", numbers)

numbers.delete_at(1)

print("After deleting index 1:", numbers)

print(
    """
Notice:

    [10, 20, 30, 40, 50]

could become:

    [10, 50, 30, 40]

The order changed.

But deletion did not require shifting
all the elements after index 1.

This is a DESIGN DECISION.

The better version depends on the application's requirements.
"""
)


# ============================================================
# PART 25 — TRAVERSAL
# ============================================================

print("\n========== TRAVERSAL ==========")

numbers = DynamicArray()

for value in [100, 200, 300, 400]:
    numbers.insert(value)

numbers.traverse(print)


# ============================================================
# PART 26 — REALISTIC EXAMPLE
# ============================================================

print("\n========== REALISTIC EXAMPLE ==========")

"""
Imagine a warehouse receiving product IDs.

We don't know in advance how many products will exist.

A static array would force us to choose a maximum.

A DynamicArray lets the structure grow automatically.
"""

warehouse_products = DynamicArray()

for product_id in [
    1001,
    1002,
    1003,
    1004,
    1005,
    1006,
    1007,
]:
    warehouse_products.insert(product_id)

print("Products:")
print(warehouse_products)

print("\nCapacity:")
print(warehouse_products.capacity())

print("\nSearch for product 1005:")

index = warehouse_products.find(1005)

if index is not None:
    print(f"Product found at index {index}.")

print("\nDelete product 1005:")

warehouse_products.delete(1005)

print(warehouse_products)


# ============================================================
# PART 27 — MANY INSERTIONS
# ============================================================

print("\n========== MANY INSERTIONS ==========")

products = DynamicArray()

for product_id in range(1, 33):
    old_capacity = products.capacity()

    products.insert(product_id)

    new_capacity = products.capacity()

    if old_capacity != new_capacity:
        print(f"Resize: {old_capacity} -> {new_capacity}")

print(f"\nFinal size={len(products)}, capacity={products.capacity()}")


# ============================================================
# PART 28 — THE COMPLETE STORY
# ============================================================

print("\n========== CHAPTER 5 COMPLETE ==========")

print(
    """
STATIC ARRAY
     │
     │ fixed capacity becomes a problem
     ▼
ARRAY IS FULL
     │
     ▼
Create a new larger static array
     │
     ├── allocate memory
     ├── copy elements
     ├── insert new element
     └── discard old array
     │
     ▼
DYNAMIC ARRAY
     │
     │ hides resizing from the user
     │
     ├── INSERT
     │      │
     │      └── if full → DOUBLE capacity
     │
     ├── FIND
     │      │
     │      └── linear search
     │
     ├── DELETE
     │      │
     │      ├── find element
     │      ├── shift elements left
     │      └── maybe shrink
     │
     └── SHRINK
            │
            └── if size <= capacity / 4
                    ↓
                 HALF capacity


The central idea:

    Dynamic Array = Static Array
                    +
                    resizing strategy

It does NOT remove the cost of resizing.

It makes resizing INFREQUENT enough
to obtain good amortized performance.
"""
)


# ============================================================
# PART 29 — COMPLEXITY SUMMARY
# ============================================================

print("\n========== COMPLEXITY SUMMARY ==========")

print(
    """
Dynamic Array:

Access by index:
    O(1)

Find:
    O(n)

Insert:
    O(1) amortized
    O(n) when resizing occurs

Delete by value while preserving order:
    O(n) worst case

Resize:
    O(n)

Extra space:
    O(n) for the underlying storage
"""
)
