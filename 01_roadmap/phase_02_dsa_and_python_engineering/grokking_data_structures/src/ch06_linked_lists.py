"""
Grokking Data Structures
Chapter 6 — Linked Lists: A Flexible Dynamic Collection

This file tells the story of linked lists through code.

The main question of the chapter is:

    How can we build a collection that can grow and shrink
    without reallocating and moving all its elements?

The answer is: Linked Lists.

Unlike an array, a linked list does not store all elements
in one contiguous block of memory.

Instead, it is built from Nodes.

Each Node stores:
    1. The actual data.
    2. A link to another Node.

This gives us flexibility, but we give up constant-time
access by index.
"""


# ============================================================
# 1. The basic idea: a Node
# ============================================================


class Node:
    """
    A node is the building block of a Singly Linked List.

    The node does not know where it sits in memory.
    It only knows:

        "Here is my data,
         and here is the next node."
    """

    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    def data(self):
        return self._data

    def next(self):
        return self._next

    def has_next(self):
        return self._next is not None

    def append(self, next_node):
        """
        Connect this node to the next node.
        """
        self._next = next_node


# ============================================================
# 2. Singly Linked List
# ============================================================


class SinglyLinkedList:
    """
    The Linked List is the public wrapper.

    Clients interact with the list,
    while the Nodes remain an internal implementation detail.

    The list only needs one piece of state:

        _head

    If _head is None, the list is empty.

    Example:

        head
         |
         v
        [7] -> [9] -> [4] -> [3] -> None
                                  ^
                                 tail
    """

    def __init__(self):
        self._head = None

    # --------------------------------------------------------
    # Insert at the back
    # --------------------------------------------------------

    def insert_to_back(self, data):
        """
        We want to keep insertion order.

        Unfortunately, an SLL only knows the next node.
        Therefore, to reach the tail, we must walk through
        the entire list.

        Time: O(n)
        """

        current = self._head

        # Empty list:
        # The new node becomes the head.
        if current is None:
            self._head = Node(data)
            return

        # Walk until we find the tail.
        while current.next() is not None:
            current = current.next()

        # The old tail now points to the new node.
        # Note: append() here is a Node method that updates
        # the node's _next link — not Python's list.append().
        current.append(Node(data))

    # --------------------------------------------------------
    # Insert at the front
    # --------------------------------------------------------

    def insert_in_front(self, data):
        """
        Here the linked list becomes much more interesting.

        We already know where the head is.

        We create a new node and make it point to the old head.

        Before:

            head
             |
             v
            [7] -> [9] -> [4]

        After insert_in_front(6):

            head
             |
             v
            [6] -> [7] -> [9] -> [4]

        Time: O(1)
        """

        old_head = self._head
        self._head = Node(data, old_head)

    # --------------------------------------------------------
    # Internal search
    # --------------------------------------------------------

    def _search(self, target):
        """
        There is no index formula like an array has.

        So we start from the head and follow the links.

        Time: O(n)
        Extra space: O(1)

        This method returns the internal Node.

        It is private because clients should not receive
        direct access to the mutable internal Nodes.
        """

        current = self._head

        while current is not None:
            if current.data() == target:
                return current

            current = current.next()

        return None

    # --------------------------------------------------------
    # Public contains operation
    # --------------------------------------------------------

    def contains(self, target):
        """
        Clients usually do not need the Node itself.

        They only need to know whether the value exists.
        """

        return self._search(target) is not None

    # --------------------------------------------------------
    # Delete
    # --------------------------------------------------------

    def delete(self, target):
        """
        To delete a node from an SLL, we must bypass it.

        Example:

            A -> B -> C

        Delete B:

            A -> C

        The problem:

            B knows C,
            but B does NOT know A.

        In an SLL, a direct reference to the target node
        does not let us reach its predecessor.
        Therefore, while traversing, we keep both:

            previous
            current

        Time: O(n)
        Extra space: O(1)
        """

        current = self._head
        previous = None

        while current is not None:
            if current.data() == target:
                # Case 1:
                # We are deleting the head.
                if previous is None:
                    self._head = current.next()

                # Case 2:
                # We are deleting any other node.
                # previous.next -> current.next
                # Achieved via Node.append():
                else:
                    previous.append(current.next())

                return

            previous = current
            current = current.next()

        raise ValueError(f"No element with value {target} was found in the list.")

    # --------------------------------------------------------
    # Delete from front
    # --------------------------------------------------------

    def delete_from_front(self):
        """
        Removing the head is a special case.

        We simply move the head to the next node.

        Time: O(1)
        """

        if self._head is None:
            raise ValueError("Cannot delete from an empty list.")

        removed = self._head
        self._head = self._head.next()

        return removed.data()

    # --------------------------------------------------------
    # Traverse
    # --------------------------------------------------------

    def traverse(self, function):
        """
        Walk through the list and apply a function to each
        element.

        The traversal starts at the head and follows next links.

        Time: O(n)
        Extra space for the returned Python list: O(n)
        """

        result = []
        current = self._head

        while current is not None:
            result.append(function(current.data()))
            current = current.next()

        return result


# ============================================================
# 3. Sorted Singly Linked List
# ============================================================


class SortedSinglyLinkedList(SinglyLinkedList):
    """
    Now imagine that the order of the elements matters.

    We cannot simply insert at the front or back.

    The new element must be inserted in the correct position.

    Example:

        [3] -> [4] -> [7] -> [9]

    insert(6)

        [3] -> [4] -> [6] -> [7] -> [9]

    We must first find the correct position.

    Time: O(n)
    """

    def insert(self, new_data):

        current = self._head
        previous = None

        while current is not None:
            # The new value belongs before current.
            if current.data() >= new_data:
                # Insert at the beginning.
                if previous is None:
                    self._head = Node(new_data, current)

                # Insert between previous and current.
                else:
                    previous.append(Node(new_data, current))

                return

            previous = current
            current = current.next()

        # We reached the end.

        # Empty list.
        if previous is None:
            self._head = Node(new_data)

        # Insert at the end.
        else:
            previous.append(Node(new_data))

    def insert_to_back(self, data):
        """
        A sorted list should not use the ordinary
        unsorted insertion operation.
        """

        self.insert(data)

    def insert_in_front(self, data):
        """
        The sorted invariant must always be preserved.

        Therefore, front insertion is also redirected
        to sorted insertion.
        """

        self.insert(data)


# ============================================================
# 4. Why binary search does not help a linked list
# ============================================================


def why_binary_search_is_not_useful():
    """
    Suppose we have:

        [1] -> [3] -> [5] -> [7] -> [9] -> [11]

    An array can jump directly to the middle:

        array[mid]

    A linked list cannot.

    To reach the middle, we must first follow:

        head -> next -> next -> ...

    Therefore, we lose the constant-time random access
    that makes binary search efficient.

    A sorted linked list still generally needs:

        Search: O(n)

    This is one of the important tradeoffs of linked lists.
    """

    pass


# ============================================================
# 5. Doubly Linked List
# ============================================================


class DoublyNode:
    """
    A Doubly Linked List gives every node two links:

        _next -> successor
        _prev -> predecessor

    Example:

        None <- [7] <-> [9] <-> [4] <-> [3] -> None
                  ^                         ^
                 head                      tail

    The additional link costs memory,
    but allows traversal in both directions.
    """

    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    def data(self):
        return self._data

    def next(self):
        return self._next

    def has_next(self):
        return self._next is not None

    def append(self, next_node):
        """
        Connect this node to its successor.

        Because this is a DLL, the successor must also
        know that this node is its predecessor.
        """

        self._next = next_node

        if next_node is not None:
            next_node._prev = self

    def prev(self):
        return self._prev

    def has_prev(self):
        return self._prev is not None

    def prepend(self, prev_node):
        """
        Connect this node to its predecessor.

        The predecessor must also know that this node
        is its successor.
        """

        self._prev = prev_node

        if prev_node is not None:
            prev_node._next = self


class DoublyLinkedList:
    """
    The DLL keeps both:

        _head
        _tail

    Having _tail is important because it gives us
    constant-time access to the last node.
    """

    def __init__(self):
        self._head = None
        self._tail = None

    # --------------------------------------------------------
    # Insert at front
    # --------------------------------------------------------

    def insert_in_front(self, data):
        """
        Time: O(1)
        """

        # Empty list:
        # Both head and tail become the new node.
        if self._head is None:
            self._tail = self._head = DoublyNode(data)
            return

        old_head = self._head

        self._head = DoublyNode(data)

        # Connect new head <-> old head.
        self._head.append(old_head)

    # --------------------------------------------------------
    # Insert at back
    # --------------------------------------------------------

    def insert_to_back(self, data):
        """
        Unlike an SLL, the DLL already knows its tail.

        Time: O(1)
        """

        # Empty list.
        if self._tail is None:
            self._tail = self._head = DoublyNode(data)
            return

        old_tail = self._tail

        self._tail = DoublyNode(data)

        # Connect old tail <-> new tail.
        self._tail.prepend(old_tail)

    # --------------------------------------------------------
    # Search
    # --------------------------------------------------------

    def _search(self, target):
        """
        The previous links do not make ordinary searching
        faster.

        We still normally start from the head.

        Time: O(n)
        """

        current = self._head

        while current is not None:
            if current.data() == target:
                return current

            current = current.next()

        return None

    # --------------------------------------------------------
    # Delete
    # --------------------------------------------------------

    def delete(self, target):
        """
        DLL deletion is easier than SLL deletion.

        Why?

        Because the node knows its predecessor.

        Once we find the target node, we can update
        both neighboring links in O(1).

        Delete by value:
            Search -> O(n)
            Delete -> O(1)
            Total  -> O(n)

        Delete given a node reference:
            O(1) — no search needed, prev and next are accessible.
        """

        node = self._search(target)

        if node is None:
            raise ValueError(f"{target} not found in the list.")

        # ----------------------------------------------------
        # Case 1: delete the head
        # ----------------------------------------------------

        if node.prev() is None:
            self._head = node.next()

            # The list contained only one node.
            if self._head is None:
                self._tail = None

            else:
                self._head.prepend(None)

        # ----------------------------------------------------
        # Case 2: delete the tail
        # ----------------------------------------------------

        elif node.next() is None:
            self._tail = node.prev()
            self._tail.append(None)

        # ----------------------------------------------------
        # Case 3: delete from the middle
        # ----------------------------------------------------

        else:
            node.prev().append(node.next())

        # The node is no longer part of the list.
        del node

    # --------------------------------------------------------
    # Traverse forward
    # --------------------------------------------------------

    def traverse(self, function):
        """
        Walk from head to tail.

        Time: O(n)
        """

        result = []
        current = self._head

        while current is not None:
            result.append(function(current.data()))
            current = current.next()

        return result

    # --------------------------------------------------------
    # Traverse backward
    # --------------------------------------------------------

    def traverse_reverse(self, function):
        """
        DLLs can also move in the opposite direction.

        Start at tail and follow prev links.

        Time: O(n)
        """

        result = []
        current = self._tail

        while current is not None:
            result.append(function(current.data()))
            current = current.prev()

        return result

    # --------------------------------------------------------
    # Insert after a known node
    # --------------------------------------------------------

    def insert_after(self, node, data):
        """
        If we already have a reference to the node after which
        we want to insert, no traversal is necessary.

        Example:

            A <-> B <-> C

        Insert X after B:

            A <-> B <-> X <-> C

        Only a constant number of links need updating.

        Time: O(1)

        This is one of the situations where a DLL is especially
        useful.
        """

        new_node = DoublyNode(data)
        next_node = node.next()

        node.append(new_node)
        new_node.append(next_node)

        if next_node is None:
            self._tail = new_node


# ============================================================
# 6. Concatenating two Doubly Linked Lists
# ============================================================


def concatenate(first, second):
    """
    Suppose we have:

        First:
        A <-> B <-> C

        Second:
        D <-> E <-> F

    We can connect:

        C <-> D

    and obtain:

        A <-> B <-> C <-> D <-> E <-> F

    For a DLL with _tail references, concatenation is O(1).

    For an SLL without a _tail reference, we must first
    traverse to the tail — making concatenation O(n).

    With arrays, combining two collections normally
    requires allocating space and moving elements.
    """

    if first._head is None:
        return second

    if second._head is None:
        return first

    # This links the existing nodes; it does not copy them.
    # After this call, both `first` and `second` share the
    # same underlying nodes. `second` should not be used
    # independently afterwards.
    first._tail.append(second._head)
    first._tail = second._tail

    return first


# ============================================================
# 7. Circular Linked Lists
# ============================================================


class CircularSinglyLinkedList(SinglyLinkedList):
    """
    A normal linked list has a clear end:

        A -> B -> C -> None

    A circular linked list removes that end:

        A -> B -> C
        ^         |
        |_________|

    The tail points back to the head.

    This is useful when the data naturally repeats:

        A -> B -> C -> A -> B -> C -> ...

    Examples from the chapter include:

        - slideshows
        - carousels
        - cyclic processes
        - repeatedly using resources
        - routing work through servers

    The chapter emphasizes that circular lists require
    careful traversal because there is no None at the end.

    IMPORTANT — inherited methods are unsafe after make_circular():

        Methods inherited from SinglyLinkedList such as
        _search(), insert_to_back(), and contains() all use:

            while current is not None:
                ...

        After make_circular() removes the None sentinel,
        these methods will loop forever if the target is
        not found. Use only traverse_once() after the list
        has been made circular.
    """

    def make_circular(self):
        """
        Convert the current SLL into a circular list.

        The tail now points to the head.
        """

        if self._head is None:
            return

        current = self._head

        while current.next() is not None:
            current = current.next()

        current.append(self._head)

    def traverse_once(self, function):
        """
        A normal traversal cannot be used because there is
        no None to signal the end.

        Instead, we remember where we started and stop
        when we return to that node.

        This is an example of a step-by-step traversal
        mechanism that avoids infinite looping.
        """

        result = []

        if self._head is None:
            return result

        current = self._head

        while True:
            result.append(function(current.data()))
            current = current.next()

            if current is self._head:
                break

        return result


# ============================================================
# 8. Circular Doubly Linked List
# ============================================================


class CircularDoublyLinkedList:
    """
    A circular DLL has both properties:

        next links move forward
        prev links move backward

    Example:

             ┌──────────────────────────────┐
             │                              │
             v                              │
        A <-> B <-> C <-> D
        ^                 |
        └─────────────────┘

    The tail's next points to the head.
    The head's prev points to the tail.

    Therefore:

        head.prev == tail

    A separate tail reference is not strictly necessary
    in a circular DLL because the tail can be reached as:

        head.prev
    """

    def __init__(self):
        self._head = None
        self._current = None

    def make_circular(self, head):
        """
        This method illustrates the important relationship
        of a circular DLL.

        The actual implementation can reuse the DLL node
        structure with only minimal changes.

        WARNING: call this only once, on a linear (non-circular)
        DLL head. Calling it again after the list is already
        circular will cause an infinite loop because the while
        loop below looks for tail.next() == None, which no
        longer exists.
        """

        self._head = head

        if self._head is None:
            self._current = None
            return

        # Find the current tail.
        tail = self._head

        while tail.next() is not None:
            tail = tail.next()

        # Close the circle.
        tail.append(self._head)
        self._head.prepend(tail)

        self._current = self._head

    def current_data_and_advance(self):
        """
        Circular lists commonly provide step-by-step traversal.

        Instead of asking:

            "Where is the end?"

        we ask:

            "Give me the current element,
             then move to the next one."

        This makes cyclic traversal natural and avoids
        the danger of infinite looping.
        """

        if self._current is None:
            raise ValueError("The list is empty.")

        data = self._current.data()
        self._current = self._current.next()

        return data


# ============================================================
# 9. The central tradeoff
# ============================================================


def chapter_summary():
    """
    The whole chapter can be remembered as a tradeoff.

    ARRAY
    -----

        Fast random access:

            array[index] -> O(1)

        But structural changes can require moving elements.


    SINGLY LINKED LIST
    ------------------

        Flexible growth and shrinkage.

        Fast at the head:

            insert front -> O(1)
            delete front  -> O(1)

        But:

            search        -> O(n)
            access        -> O(n)
            insert back   -> O(n)
            delete        -> O(n)

        Each node only knows its successor.
        A direct reference to a node does not reach its predecessor.


    DOUBLY LINKED LIST
    ------------------

        Each node knows:

            successor
            predecessor

        Therefore:

            forward traversal  -> possible
            backward traversal -> possible

        With a tail reference:

            insert back              -> O(1)
            delete given node ref    -> O(1)

        The price:

            more memory (two links per node instead of one)
            more link maintenance
            more implementation complexity


    CIRCULAR LINKED LIST
    --------------------

        The tail points back to the head.

        This is useful when the data is naturally cyclic.

        But traversal must be controlled carefully,
        otherwise the program can loop forever.


    THE BIG IDEA
    ------------

        Linked lists exchange random access
        for flexible structural changes.

        A DLL is useful when you need bidirectional traversal,
        efficient operations at both ends, or the ability to
        delete a node in O(1) when you already hold a reference
        to it — without needing to find its predecessor first.
    """

    pass


# ============================================================
# 10. Complexity at a glance
# ============================================================

"""
                    SLL                     DLL

Access              O(n)                    O(n)
Search              O(n)                    O(n)

Insert front        O(1)                    O(1)
Insert back         O(n)                    O(1)
Insert middle*      O(1)                    O(1)

Delete by value     O(n)                    O(n)
Delete known node*  O(n) — needs pred.      O(1)

Concatenate         O(n) — no tail ref.     O(1)

Forward traversal   O(n)                    O(n)
Backward traversal  --                      O(n)

* The O(1) result assumes that the relevant node/reference
  is already known. Finding that position may still require
  O(n) traversal.
"""


# ============================================================
# 11. Mental model
# ============================================================

"""
Think of an SLL as people standing in a line.

Each person knows only:

    "Who is the person after me?"

So:

    Alice -> Bob -> Charlie -> David

If you know Alice, you can eventually reach David.

But if you are given Charlie, Charlie cannot tell you
who was standing before him.

That is exactly why SLL deletion needs a `previous` variable.

Now give everyone another piece of information:

    "Who is before me?"

You get:

    Alice <-> Bob <-> Charlie <-> David

That is a Doubly Linked List.

Now connect David back to Alice:

    Alice -> Bob -> Charlie -> David
      ^                         |
      |_________________________|

Now the line has become a cycle.

That is a Circular Linked List.
"""
