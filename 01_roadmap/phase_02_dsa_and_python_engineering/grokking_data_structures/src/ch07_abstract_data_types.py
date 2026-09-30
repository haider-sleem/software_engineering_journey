"""
Chapter 7: Abstract Data Types — The Bag
Grokking Data Structures — Marcello La Rocca

Story:
We want a simple container for collecting data when the order of
the elements does not matter.

The chapter introduces the Bag as the simplest possible container,
then implements it using a singly linked list.
"""


# ============================================================
# 1. The ADT: What do we need?
# ============================================================

"""
Before choosing a data structure, define what the application needs.

For a Bag, the minimum required interface is:

    insert(x)
    iterate()

The Bag interface defined in this chapter:
    - stores a collection of elements
    - allows duplicates
    - does not guarantee insertion order
    - does not include search or remove

This is the ADT.

ADT            = WHAT the client can do and what operations guarantee.
Data Structure = HOW those operations are implemented.
"""


# ============================================================
# 2. The Data Structure: Linked List
# ============================================================


class Node:
    """A node in a singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A simple singly linked list used to implement the Bag."""

    def __init__(self):
        self.head = None

    def insert_in_front(self, value):
        """
        Insert a new node at the beginning of the list.

        Why at the front?

        A singly linked list can insert at the head in O(1).
        Inserting at the end would require O(n) traversal
        because there is no tail pointer.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        """Return all elements in the linked list as a Python list."""
        result = []
        current = self.head

        while current is not None:
            result.append(current.value)
            current = current.next

        return result


# ============================================================
# 3. The Bag
# ============================================================


class Bag:
    """
    A simple Bag ADT implemented using a singly linked list.

    The Bag only guarantees:
        - insert(value)     → O(1)
        - iteration/traversal → O(n)

    The order of elements is NOT guaranteed.
    Duplicate elements are allowed.
    Search and remove are NOT provided.
    """

    def __init__(self):
        self._data = LinkedList()

    def insert(self, value):
        """
        Add one element to the Bag.

        The Bag does not care where the element is stored,
        because insertion order is not part of its contract.

        Time: O(1)
        """
        self._data.insert_in_front(value)

    def traverse(self):
        """
        Return all elements currently stored in the Bag.

        The ADT exposes iterate() as the operation name.
        This implementation provides that behavior through traverse().

        The returned order is NOT guaranteed by the Bag ADT.
        The order may differ between traversals.

        Time: O(n)
        """
        return self._data.traverse()


# ============================================================
# 4. Using the Bag
# ============================================================

"""
Imagine Andrea is collecting daily order statistics.

She only cares about the values themselves.
She does not care about their insertion order.
"""

bag = Bag()

bag.insert(1)
bag.insert(1)
bag.insert(1)
bag.insert(2)
bag.insert(2)
bag.insert(3)
bag.insert(2)
bag.insert(3)
bag.insert(4)
bag.insert(5)
bag.insert(3)
bag.insert(4)

print(bag.traverse())

# Possible output:
#
# [4, 3, 5, 4, 3, 2, 3, 2, 2, 1, 1, 1]
#
# Another implementation or another traversal could produce
# a different order.
#
# The Bag is still correct because it never promised an order.


# ============================================================
# 5. The Important Idea: ADT Abstraction
# ============================================================

"""
The application works with the Bag:

    bag.insert(10)
    bag.insert(20)

It does not need to know that the Bag uses:

    LinkedList
        ↓
      Node
        ↓
      next

This is the benefit of the ADT abstraction.

The client depends on the interface, not the implementation.

We could later change the internal implementation:

    Bag
     |
     +-- Linked List     (current)
     |
     +-- Array           (alternative)

while keeping exactly the same Bag interface.
"""


# ============================================================
# 6. Why Does Order Not Matter?
# ============================================================

"""
Suppose the Bag contains:

    1 1 2 3 3

One traversal might produce:

    1 1 2 3 3

Another might produce:

    3 1 3 2 1

Both are valid.

If we calculate order-independent statistics such as:

    sum
    total count
    count by type

the result does not depend on the order.
The computation depends only on which elements are present,
not the sequence in which they appear.

Therefore, client code must not assume a specific order.
"""


# ============================================================
# 7. Testing the Bag
# ============================================================

"""
Because the Bag does not guarantee order, tests must not
depend on a specific ordering of the elements.

Bad:

    assert bag.traverse() == [1, 1, 2, 3, 3]

A test that depends on order would incorrectly reject a valid
Bag implementation that stores elements in a different order.

Better — when only uniqueness matters:

    assert set(bag.traverse()) == {1, 2, 3}

But this loses information about duplicates.

Best — when duplicates matter, use a frequency-aware comparison:
"""

from collections import Counter  # noqa: E402

bag_for_test = Bag()

for value in [1, 1, 2, 3, 3]:
    bag_for_test.insert(value)

assert Counter(bag_for_test.traverse()) == Counter([1, 1, 2, 3, 3])

print("Bag test passed.")

# Counter compares element frequencies regardless of order.
# Counter([1, 1, 2, 3, 3]) == Counter([3, 1, 3, 2, 1]) → True


# ============================================================
# 8. Complexity
# ============================================================

"""
With the singly linked list implementation:

    insert()   → O(1)
    traverse() → O(n)

Why is insert O(1)?

    The new node is inserted at the head:

        new_node.next = head
        head = new_node

    No traversal required.

Why is traversal O(n)?

    Every element must be visited exactly once.
"""


# ============================================================
# Final Mental Model
# ============================================================

"""
The chapter's main idea:

    Problem
       |
       v
    What do we need?
       |
       v
      Bag (ADT — defines WHAT)
       |
       +-- insert(x)
       +-- iterate()
       |
       v
    Linked List (implementation — defines HOW)
       |
       v
    Node + next

Remember:

    ADT            = WHAT (operations + guarantees)
    Data Structure = HOW  (memory layout + algorithms)

    Bag:
        - simplest container
        - duplicates allowed
        - insertion order does not matter
        - insert()              O(1)
        - iterate()/traverse()  O(n)
        - no search()
        - no remove()

    Linked List implementation:
        - insert at front       O(1)
        - traverse              O(n)
"""
