"""
Grokking Data Structures
Chapter 9 — Queues

This file tells the story of a Queue through code.

Main idea:

    FIFO — First In, First Out

New elements enter from the rear.
Oldest elements leave from the front.
"""


# ============================================================
# 1. The basic idea: FIFO
# ============================================================

"""
Imagine a line of people waiting for service.

    Front                       Rear
      ↓                           ↓
    [Ali] → [Mona] → [Omar] → [Sara]

Ali arrived first, so Ali must be served first.

This is FIFO:

    First In → First Out
"""


# ============================================================
# 2. Queue as an ADT
# ============================================================


class Queue:
    """
    A queue exposes two core operations:

        enqueue(value)
        dequeue()

    The ADT defines what the queue does,
    not how it stores its data.
    """

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass


"""
At the ADT level, we only care about the behavior:

    enqueue(10)
    enqueue(20)
    enqueue(30)

    dequeue() → 10
    dequeue() → 20
    dequeue() → 30

The oldest element always leaves first.
"""


# ============================================================
# 3. A queue needs two ends
# ============================================================

"""
A stack mainly needs one reference:

    top

A queue is different.

Elements enter at one end:

    rear

and leave from the other:

    front

So conceptually:

    Front                         Rear
      ↓                             ↓
    [10] → [20] → [30] → [40]

    dequeue()                enqueue()
"""


# ============================================================
# 4. Queue using a doubly linked list
# ============================================================

"""
A queue needs:

    enqueue → add at the rear
    dequeue → remove from the front

A doubly linked list already supports both ends efficiently.

    Front                         Rear
      ↓                             ↓
    [10] ↔ [20] ↔ [30] ↔ [40]
"""


class Node:
    """A node stores data and links to neighboring nodes."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedQueue:
    """
    Queue implemented using a doubly linked list.

    front → first node
    rear  → last node
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Add a new value at the rear.

        Time: O(1)
        """

        new_node = Node(value)

        # Empty queue:
        # The new node is both front and rear.
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return

        # Connect the new node after the current rear.
        new_node.prev = self.rear
        self.rear.next = new_node

        # Move rear to the new last node.
        self.rear = new_node

    def peek(self):
        """
        Return the front value without removing it.

        Time: O(1)
        """

        if self.front is None:
            raise ValueError("Queue is empty.")

        return self.front.data

    def dequeue(self):
        """
        Remove and return the oldest value.

        Time: O(1)
        """

        if self.front is None:
            raise ValueError("Queue is empty.")

        value = self.front.data

        # Move front to the next node.
        self.front = self.front.next

        # If the queue became empty,
        # rear must also become None.
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None

        return value


# ============================================================
# 5. Using the linked-list queue
# ============================================================

queue = LinkedQueue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

"""
Current state:

    Front                 Rear
      ↓                     ↓
    [10] ↔ [20] ↔ [30]
"""

print(queue.dequeue())  # 10
print(queue.dequeue())  # 20

"""
The queue preserved insertion order.

Remaining:

    Front     Rear
      ↓         ↓
    [30]
"""


# ============================================================
# 6. Why not a simple linear array?
# ============================================================

"""
Suppose we use a fixed-size array:

    [10][20][30][40][  ][  ]

After two dequeues:

    [  ][  ][30][40][  ][  ]

The beginning of the array contains unused space.

If rear keeps moving right, eventually it reaches
the end of the array even though there is free space
at the beginning.

A simple linear queue therefore wastes capacity.
"""


# ============================================================
# 7. Circular Queue
# ============================================================

"""
Instead of treating the array as a straight line,
we can treat it as a circle.

    [0] [1] [2] [3] [4] [5]
     ↑                   ↓
     └────── wrap ───────┘

After index 5, the next position is index 0.

This allows the queue to reuse space freed by dequeue().
"""


# ============================================================
# 8. Virtual indexes and modulo
# ============================================================

"""
For an array of size 6:

    virtual index 6 → physical index 0
    virtual index 7 → physical index 1
    virtual index 8 → physical index 2

The modulo operator performs this mapping:

    physical_index = virtual_index % max_size
"""


# ============================================================
# 9. Static array queue
# ============================================================


class CircularQueue:
    """
    Queue implemented using a fixed-size circular array.

    front:
        Index of the next element to dequeue.

    rear:
        Index of the next free position for enqueue.

    size:
        Number of elements currently stored.

    max_size:
        Maximum queue capacity.
    """

    def __init__(self, max_size):
        if max_size < 1:
            raise ValueError("Queue capacity must be at least 1.")

        self._data = [None] * max_size
        self._max_size = max_size

        self._front = 0
        self._rear = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._max_size

    def peek(self):
        """
        Return the front value without removing it.

        Time: O(1)
        """

        if self.is_empty():
            raise ValueError("Queue is empty.")

        return self._data[self._front]

    def enqueue(self, value):
        """
        Add value at rear.

        Time: O(1)
        """

        if self.is_full():
            raise ValueError("Queue is full.")

        self._data[self._rear] = value

        # Move rear forward.
        # If it reaches the end, wrap to 0.
        self._rear = (self._rear + 1) % self._max_size

        self._size += 1

    def dequeue(self):
        """
        Remove and return the oldest value.

        Time: O(1)
        """

        if self.is_empty():
            raise ValueError("Queue is empty.")

        value = self._data[self._front]

        # Clear the old position.
        self._data[self._front] = None

        # Move front forward and wrap if necessary.
        self._front = (self._front + 1) % self._max_size

        self._size -= 1

        return value


# ============================================================
# 10. Circular queue in action
# ============================================================

queue = CircularQueue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

"""
The queue contains:

    Front                 Rear
      ↓                     ↓
    [10][20][30][40][None]
"""


print(queue.dequeue())  # 10
print(queue.dequeue())  # 20

"""
Now there are free cells at the beginning:

    [ ][ ][30][40][ ]

The rear can wrap around and reuse them.
"""

queue.enqueue(50)
queue.enqueue(60)

"""
The physical array can now look like:

    [60][ ][30][40][50]

The logical queue is still:

    Front → 30 → 40 → 50 → 60 → Rear

The physical positions do not need to be
in increasing index order.
"""


# ============================================================
# 11. Why keep a size variable?
# ============================================================

"""
There is an important ambiguity in a circular queue.

At some point:

    front == rear

could mean either:

    1. The queue is empty.
    2. The queue is full.

The size variable removes this ambiguity.

    size == 0
        → empty

    size == max_size
        → full
"""


# ============================================================
# 12. Comparing implementations
# ============================================================

"""
                         enqueue     dequeue     Dynamic size

Static array              O(1)         O(1)          No

Dynamic array             O(n)         O(n)          Yes
                           worst        worst

Dynamic array             O(1)         O(1)          Yes
                         amortized    amortized

Linked list               O(1)         O(1)          Yes
"""


# ============================================================
# 13. The practical tradeoff
# ============================================================

"""
Linked lists:

    + Dynamic size
    + O(1) enqueue
    + O(1) dequeue
    + Simple queue implementation

    - Extra memory for links
    - Less memory locality


Arrays:

    + Memory efficient
    + Good memory locality
    + Often faster in practice
    + O(1) enqueue/dequeue for a fixed circular queue

    - Fixed capacity
    - More complicated implementation

The best choice depends on the requirements.

If the queue size is flexible and simple code matters:

    → Linked list

If the maximum capacity is known and performance
and memory locality matter:

    → Static circular array
"""


# ============================================================
# 14. Final mental model
# ============================================================

"""
A queue is simply a controlled line.

New items enter here:

                enqueue
                   ↓
    Front → [A] → [B] → [C] ← Rear

The oldest item leaves here:

    dequeue
       ↓
    [A] → [B] → [C]

After dequeue():

    Front → [B] → [C] ← Rear


The core rule never changes:

    FIFO
    First In, First Out
"""
