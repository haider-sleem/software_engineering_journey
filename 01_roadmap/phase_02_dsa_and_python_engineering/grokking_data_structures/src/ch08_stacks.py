# Chapter 8 — Stacks: Piling Up Data Before Processing It
# Warehouse story: managing tasks using Last In, First Out (LIFO)


# ============================================================
# Stage 1 — A warehouse receives tasks
# ============================================================

# Tasks arrive over time, but the newest task may need
# to be processed first.

tasks = []


# ============================================================
# Stage 2 — Adding tasks (push)
# ============================================================

# Adding an element to the top of a stack is called push.

tasks.append("Receive shipment")
tasks.append("Check inventory")
tasks.append("Print report")

print(tasks)
# ['Receive shipment', 'Check inventory', 'Print report']


# ============================================================
# Stage 3 — LIFO
# ============================================================

# A stack follows Last In, First Out.
# The last task added is the first task removed.

task = tasks.pop()

print(task)
# Print report


# ============================================================
# Stage 4 — The stack after pop
# ============================================================

print(tasks)
# ['Receive shipment', 'Check inventory']


# ============================================================
# Stage 5 — The top of the stack
# ============================================================

# The last element represents the top of the stack.

print(tasks[-1])
# Check inventory


# ============================================================
# Stage 6 — peek
# ============================================================

# peek reads the top element without removing it.

top_task = tasks[-1]

print(top_task)
# Check inventory

print(tasks)
# The stack is unchanged.


# ============================================================
# Stage 7 — is_empty
# ============================================================

# We need to know whether the stack contains any elements.

print(len(tasks) == 0)
# False


# ============================================================
# Stage 8 — Empty stack
# ============================================================

tasks.clear()

print(len(tasks) == 0)
# True


# ============================================================
# Stage 9 — The Stack ADT
# ============================================================

# The Stack ADT defines the behavior, not the implementation.
#
# push(x)    -> add x to the top
# pop()      -> remove and return the top element
# peek()     -> return the top without removing it
# is_empty() -> check whether the stack is empty


# ============================================================
# Stage 10 — Building a Stack class (incremental)
# ============================================================

# Each stage adds one method to show the construction process.
# The final version (Stage 14) is the one used in the warehouse.


# Stage 10: start with storage only
class Stack:
    def __init__(self):
        self._data = []


# Stage 11: add push
class Stack:  # noqa: F811
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)


# Stage 12: add pop
class Stack:  # noqa: F811
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        return self._data.pop()


# Stage 13: add peek
class Stack:  # noqa: F811
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]


# Stage 14: complete Stack — add is_empty
class Stack:  # noqa: F811
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0


# ============================================================
# Stage 15 — Using the Stack
# ============================================================

stack = Stack()

stack.push("Receive shipment")
stack.push("Check inventory")
stack.push("Print report")

print(stack.peek())
# Print report

print(stack.pop())
# Print report

print(stack.pop())
# Check inventory


# ============================================================
# Stage 16 — Stack and linked lists
# ============================================================

# A stack only needs to modify one side of the data structure.
# With a Singly Linked List, the front is a natural choice for the top.
#
# Top
#  ↓
# [C] → [B] → [A] → None


# ============================================================
# Stage 17 — Stack using a Singly Linked List (structure)
# ============================================================


class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next

    def set_next(self, node):
        self._next = node


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def insert_in_front(self, value):
        new_node = Node(value)
        new_node.set_next(self._head)
        self._head = new_node

    def delete_from_front(self):
        if self._head is None:
            raise IndexError("Stack is empty.")
        value = self._head.value()
        self._head = self._head.next()
        return value

    def peek_front(self):
        if self._head is None:
            raise IndexError("Stack is empty.")
        return self._head.value()

    def is_empty(self):
        return self._head is None


# ============================================================
# Stage 18 — Stack wrapper around SinglyLinkedList
# ============================================================

# The Stack exposes only the operations that belong to the ADT.
# The underlying linked list remains an implementation detail.


class LinkedStack:
    """A Stack implemented using a Singly Linked List."""

    def __init__(self):
        self._data = SinglyLinkedList()

    def push(self, value):
        # insert_in_front is O(1) — no traversal needed.
        self._data.insert_in_front(value)

    def pop(self):
        # delete_from_front is O(1).
        return self._data.delete_from_front()

    def peek(self):
        return self._data.peek_front()

    def is_empty(self):
        return self._data.is_empty()


# ============================================================
# Stage 19 — Why the front?
# ============================================================

# Singly Linked List:
#
# insert at front  -> O(1)
# delete from front -> O(1)
#
# No traversal is required.
# We never need to traverse backward, so SLL is enough.
# A Doubly Linked List would add unnecessary overhead.


# ============================================================
# Stage 20 — Stack growth (SLL)
# ============================================================

# push("A")
#
# Top
#  ↓
# [A]
#
# push("B")
#
# Top
#  ↓
# [B] → [A]
#
# push("C")
#
# Top
#  ↓
# [C] → [B] → [A]
#
# pop():
#
# Top
#  ↓
# [B] → [A]


# ============================================================
# Stage 21 — Static Array implementation
# ============================================================

# push -> O(1)
# pop  -> O(1)
#
# Limitation: the capacity is fixed.
#
# [A][B][C][D]
#             ↑
#            Top
#
# If there is no free cell, push fails or requires resizing.


# ============================================================
# Stage 22 — Dynamic Array implementation
# ============================================================

# A dynamic array grows when it becomes full.
#
# push:
#   O(n) worst case when resizing occurs
#   O(1) amortized across n pushes
#
# pop:
#   O(n) worst case when shrinking occurs
#   O(1) amortized across n pops
#
# n pushes into an empty dynamic array -> O(n) total
# n pops from a stack of n elements   -> O(n) total


# ============================================================
# Stage 23 — Memory considerations
# ============================================================

# Resizing a dynamic array may require a larger contiguous
# block of memory.
#
# A very large stack can therefore make allocation harder.
#
# A linked-list stack can grow node by node, without
# requiring contiguous memory.
#
# Linked-list tradeoff:
#   flexible growth, but extra memory per node for links.


# ============================================================
# Stage 24 — Big-O vs actual performance
# ============================================================

# Big-O describes how performance grows as n grows.
# Profiling measures the actual implementation.
#
# Two implementations can have similar asymptotic behavior
# but different real-world running times.
#
# Python's built-in list is highly optimized:
#   - contiguous memory, good cache behavior
#   - no Node object creation/destruction
#
# A linked-list Stack must allocate and garbage-collect
# a Node object for every push and pop.
#
# Result: Python's list-based Stack is often faster in practice
# even though both are O(1) amortized.


# ============================================================
# Stage 25 — Final warehouse example
# ============================================================

# A warehouse receives tasks and always processes
# the most recently added task first.

warehouse_stack = Stack()  # list-based Stack from Stage 14

warehouse_stack.push("Receive shipment")
warehouse_stack.push("Update inventory")
warehouse_stack.push("Prepare order")

while not warehouse_stack.is_empty():
    current_task = warehouse_stack.pop()
    print(f"Processing: {current_task}")

# Processing order:
# Prepare order
# Update inventory
# Receive shipment


# ============================================================
# Chapter 8 complete
# ============================================================

# Core idea:
#   Stack = LIFO
#   push  = add to top
#   pop   = remove from top
#   peek  = inspect top without removing
#
# Implementations:
#   Static Array   -> O(1), fixed capacity
#   Dynamic Array  -> O(1) amortized, flexible capacity
#   Singly Linked List -> O(1), flexible, extra memory per node
#
# ADT defines behavior.
# Data structure determines implementation tradeoffs.
