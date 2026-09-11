"""
Grokking Data Structures — Chapter 3
Sorted Arrays: Searching Faster, at a Price

The story of the chapter:

Unsorted Array
       ↓
"What if order matters?"
       ↓
Keep the array sorted
       ↓
Insertion becomes harder
       ↓
Deletion becomes harder
       ↓
But searching can become faster
       ↓
Linear Search with an early stop
       ↓
Binary Search
       ↓
Trade-off:
expensive writes <-> fast reads
"""

from array import array


# ============================================================
# PART 1 — OUR BASIC STATIC ARRAY
# ============================================================


class StaticArray:
    """
    A small fixed-size array abstraction.

    The capacity is fixed after construction.
    """

    def __init__(self, capacity: int, typecode: str = "l"):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")

        self._data = array(typecode, [0]) * capacity

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, index: int):
        self._validate_index(index)
        return self._data[index]

    def __setitem__(self, index: int, value) -> None:
        self._validate_index(index)
        self._data[index] = value

    def _validate_index(self, index: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= len(self._data):
            raise IndexError(f"Index {index} out of range.")

    def __str__(self) -> str:
        return str(self._data.tolist())


# ============================================================
# PART 2 — THE NEW IDEA:
# WHY WOULD WE WANT A SORTED ARRAY?
# ============================================================

"""
Suppose Mario has hundreds of baseball cards.

With an unsorted collection:

    [7, 2, 9, 1, 5, 4, 8, 3]

If he wants card 8, he may need to check many cards.

But if we keep the collection sorted:

    [1, 2, 3, 4, 5, 7, 8, 9]

we can exploit the order to search much more intelligently.

That is the central idea of this chapter:

    Pay a price when modifying the array
    in exchange for faster searching.
"""


# ============================================================
# PART 3 — SORTED ARRAY
# ============================================================


class SortedArray:
    """
    A fixed-capacity array whose meaningful elements are
    always kept in ascending order.

    Important invariant:

        array[0] <= array[1] <= array[2] ...

    Clients should not be allowed to arbitrarily modify
    individual entries because that could break the invariant.
    """

    def __init__(self, max_size: int, typecode: str = "l"):
        self._array = StaticArray(max_size, typecode)
        self._max_size = max_size
        self._size = 0

    def __len__(self) -> int:
        """
        Number of meaningful elements.

        This is different from the capacity.
        """
        return self._size

    def max_size(self) -> int:
        """Return the fixed capacity."""
        return self._max_size

    def __getitem__(self, index: int):
        """
        Read a meaningful element.

        Notice that there is intentionally no public
        __setitem__ method.

        Why?

        Because arbitrary assignment could break sorting.
        """
        self._validate_used_index(index)
        return self._array[index]

    # ========================================================
    # PART 4 — INSERT
    # ========================================================

    def insert(self, value) -> None:
        """
        Insert value while preserving ascending order.

        Example:

            [1, 2, 4, 5, 6]

        insert(3)

            [1, 2, 3, 4, 5, 6]

        Because an array occupies contiguous memory, we cannot
        simply "create a hole" in the middle.

        Therefore, elements are shifted to the right.
        """

        if self._size >= self._max_size:
            raise ValueError(
                f"The array is already full. Maximum size: {self._max_size}"
            )

        # Start from the rightmost meaningful element.
        #
        # We move elements one position to the right
        # until we find the correct location for value.

        for i in range(self._size, 0, -1):
            # If the element to the left is already <= value,
            # then we found the correct position.
            if self._array[i - 1] <= value:
                self._array[i] = value
                self._size += 1

                return

            # Otherwise, move the larger element right.
            self._array[i] = self._array[i - 1]

        # If we reach here, value belongs at index 0.
        self._array[0] = value
        self._size += 1

    # ========================================================
    # PART 5 — DELETE BY VALUE
    # ========================================================

    def delete(self, target) -> None:
        """
        Delete the first occurrence of target.

        Because the array must remain sorted, we cannot replace
        the deleted element with the last element as we did
        with an unsorted array.

        We must shift everything after it one position left.
        """

        index = self.search(target)

        if index is None:
            raise ValueError(
                f"Unable to delete element {target}: the entry is not in the array."
            )

        # Shift elements left.
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._size -= 1

    # ========================================================
    # PART 6 — DELETE BY INDEX
    # ========================================================

    def delete_at(self, index: int) -> None:
        """
        Delete the element at a specific index.

        Again, we shift everything after it left.
        """

        self._validate_used_index(index)

        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._size -= 1

    # ========================================================
    # PART 7 — LINEAR SEARCH
    # ========================================================

    def linear_search(self, target):
        """
        Linear search adapted for a sorted array.

        The important improvement:

            If current_value > target

        then target cannot exist later because everything
        after current_value is >= current_value.

        Therefore we can stop early.
        """

        for i in range(self._size):
            if self._array[i] == target:
                return i

            elif self._array[i] > target:
                return None

        return None

    # ========================================================
    # PART 8 — BINARY SEARCH
    # ========================================================

    def binary_search(self, target):
        """
        Search for target using binary search.

        We maintain two boundaries:

            left
            right

        They delimit the part of the array where the target
        could still exist.

        Each comparison allows us to eliminate roughly half
        of the remaining search space.
        """

        left = 0
        right = self._size - 1

        while left <= right:
            mid_index = (left + right) // 2
            mid_value = self._array[mid_index]

            # We found the target.
            if mid_value == target:
                return mid_index

            # Target must be somewhere to the left.
            elif mid_value > target:
                right = mid_index - 1

            # Target must be somewhere to the right.
            else:
                left = mid_index + 1

        # Search space became empty.
        return None

    # ========================================================
    # PART 9 — SEARCH
    # ========================================================

    def search(self, target):
        """
        The main search interface.

        Here we choose binary search because the data
        structure guarantees that its elements are sorted.
        """

        return self.binary_search(target)

    # ========================================================
    # PART 10 — TRAVERSAL
    # ========================================================

    def traverse(self, callback) -> None:
        """
        Visit every meaningful element.

        Since the array is sorted, traversal naturally produces
        elements in ascending order.
        """

        for i in range(self._size):
            callback(self._array[i])

    # ========================================================
    # PART 11 — INTERNAL VALIDATION
    # ========================================================

    def _validate_used_index(self, index: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} is outside the populated portion.")

    def __str__(self) -> str:
        values = [self._array[i] for i in range(self._size)]

        return str(values)


# ============================================================
# PART 12 — MARIO'S CARDS
# ============================================================

print("========== MARIO'S CARDS ==========")

cards = SortedArray(10)

print("Initially:")
print(cards)

print("\nMario starts adding cards...")

cards.insert(7)
print(cards)

cards.insert(2)
print(cards)

cards.insert(9)
print(cards)

cards.insert(1)
print(cards)

cards.insert(5)
print(cards)

cards.insert(4)
print(cards)

cards.insert(8)
print(cards)

cards.insert(3)
print(cards)


# ============================================================
# PART 13 — WHAT JUST HAPPENED?
# ============================================================

"""
Notice what happened during every insertion.

Suppose we had:

    [1, 2, 4, 5, 6]

and executed:

    insert(3)

We cannot simply do:

    [1, 2, 3, 4, 5, 6]

without moving anything.

The physical array is contiguous, so we must first make room:

    [1, 2, 4, 5, 6, ?]

Move 6:

    [1, 2, 4, 5, 6, 6]

Move 5:

    [1, 2, 4, 5, 5, 6]

Move 4:

    [1, 2, 4, 4, 5, 6]

Now insert 3:

    [1, 2, 3, 4, 5, 6]

This is the price we pay for keeping the array sorted.
"""


# ============================================================
# PART 14 — SEARCHING
# ============================================================

print("\n========== SEARCH ==========")

print("Cards:")
print(cards)

target = 5

print(f"\nSearching for {target}...")

index = cards.search(target)

if index is not None:
    print(f"Found {target} at index {index}.")
else:
    print("Card not found.")


# ============================================================
# PART 15 — LINEAR SEARCH
# ============================================================

print("\n========== LINEAR SEARCH ==========")

print("Search for 8:")
print("Index:", cards.linear_search(8))

print("Search for 100:")
print("Index:", cards.linear_search(100))


# ============================================================
# PART 16 — BINARY SEARCH
# ============================================================

print("\n========== BINARY SEARCH ==========")

print("Search for 8:")
print("Index:", cards.binary_search(8))

print("Search for 100:")
print("Index:", cards.binary_search(100))


# ============================================================
# PART 17 — SEE BINARY SEARCH STEP BY STEP
# ============================================================


def demonstrate_binary_search(values, target):
    """
    A teaching version of binary search.

    It prints every decision so we can see how the search
    space becomes smaller.
    """

    left = 0
    right = len(values) - 1

    step = 1

    while left <= right:
        mid = (left + right) // 2

        print(
            f"Step {step}: left={left}, mid={mid}, right={right}, value={values[mid]}"
        )

        if values[mid] == target:
            print("Target found!")
            return mid

        elif values[mid] > target:
            print("Target must be on the LEFT.")
            right = mid - 1

        else:
            print("Target must be on the RIGHT.")
            left = mid + 1

        step += 1

    print("Target not found.")
    return None


print("\n========== BINARY SEARCH WALKTHROUGH ==========")

values = [1, 2, 3, 4, 5, 7, 8, 9]

demonstrate_binary_search(values, 8)


# ============================================================
# PART 18 — WHY SORTING HELPS SEARCH
# ============================================================

print("\n========== LINEAR VS BINARY ==========")

print(
    """
Sorted data:

[1, 2, 3, 4, 5, 7, 8, 9]

Linear search:
    check one element
    then another
    then another...

Binary search:
    check the middle
    eliminate half
    check the new middle
    eliminate half again
    ...
"""
)


# ============================================================
# PART 19 — DELETE
# ============================================================

print("\n========== DELETE ==========")

print("Before deletion:")
print(cards)

print("\nDelete card 5:")

cards.delete(5)

print("After deletion:")
print(cards)


# ============================================================
# PART 20 — DELETE BY INDEX
# ============================================================

print("\n========== DELETE BY INDEX ==========")

print("Before:")
print(cards)

print("\nDelete element at index 2:")

cards.delete_at(2)

print("After:")
print(cards)


# ============================================================
# PART 21 — TRAVERSAL
# ============================================================

print("\n========== TRAVERSAL ==========")

print("Cards in ascending order:")

cards.traverse(print)


# ============================================================
# PART 22 — INSERTION AGAIN
# ============================================================

print("\n========== INSERTION AGAIN ==========")

print("Before:")
print(cards)

print("\nInsert 6:")

cards.insert(6)

print("After:")
print(cards)


# ============================================================
# PART 23 — CAPACITY VS SIZE
# ============================================================

print("\n========== SIZE VS CAPACITY ==========")

print("Number of meaningful elements:", len(cards))
print("Maximum capacity:", cards.max_size())


# ============================================================
# PART 24 — A REALISTIC USE CASE
# ============================================================

print("\n========== REALISTIC USE CASE ==========")

"""
Imagine a system that receives many read requests:

    "Is product ID 500 available?"
    "Is product ID 820 available?"
    "Is product ID 125 available?"
    ...

If the data changes very rarely but is searched many times,
keeping it sorted can be worthwhile.

The pattern is:

        MANY READS
            +
       FEW WRITES
            ↓
       SORTED ARRAY
            ↓
      BINARY SEARCH
"""

product_ids = SortedArray(20)

for product_id in [
    120,
    450,
    230,
    900,
    150,
    700,
]:
    product_ids.insert(product_id)

print("Sorted product IDs:")
print(product_ids)

print("\nSearch for product 700:")

result = product_ids.binary_search(700)

if result is not None:
    print(f"Product found at index {result}.")
else:
    print("Product not found.")


# ============================================================
# PART 25 — THE TRADE-OFF
# ============================================================

print("\n========== THE TRADE-OFF ==========")

print(
    """
UNSORTED ARRAY

    Insert:
        easy

    Delete:
        can be easy if order doesn't matter

    Search:
        linear

        O(n)


SORTED ARRAY

    Insert:
        expensive because elements may need shifting

    Delete:
        expensive because elements may need shifting

    Search:
        binary search is possible

        O(log n)


Therefore:

    Faster READS
        ⇅
    More expensive WRITES

Sorted arrays make the most sense when there is
a high read-to-write ratio.
"""
)


# ============================================================
# PART 26 — FINAL STORY
# ============================================================

print("\n========== CHAPTER 3 COMPLETE ==========")

print(
    """
Chapter 2:

    We didn't care about order.

    [7, 2, 9, 1, 5]

    Therefore:
        insertion was easy
        deletion could be easy
        search was linear


Chapter 3:

    We decide that order matters.

    [1, 2, 5, 7, 9]

    Now we must maintain an invariant:

        elements are always sorted


    That changes everything:

        INSERT
            ↓
        find correct position
            ↓
        shift elements right
            ↓
        insert value


        DELETE
            ↓
        find value
            ↓
        shift elements left
            ↓
        reduce size


        SEARCH
            ↓
        sorted data
            ↓
        binary search
            ↓
        eliminate half of the search space


Final idea:

    SORTING IS NOT FREE.

    We pay more when modifying the data
    so that we can search it more efficiently.

    This is the fundamental trade-off of
    the Sorted Array.
"""
)







