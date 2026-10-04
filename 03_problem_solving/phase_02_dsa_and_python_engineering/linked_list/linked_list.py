from typing import Optional

# 1- Source: https://neetcode.io/problems/reverse-a-linked-list/question?list=neetcode150


def reverseList(head):
    """Reverses a singly linked list in-place.

    Args:
        head: The beginning of the singly linked list.

    Returns:
        The new head of the reversed linked list.
    """
    prev = None
    current = head

    while current is not None:
        # 1. Store the next node to avoid losing the rest of the list
        next_node = current.next

        # 2. Reverse the current node's pointer to point backward
        current.next = prev

        # 3. Move the prev pointer forward to the current node
        prev = current

        # 4. Move the current pointer forward to the saved next node
        current = next_node

    # At the end of the loop, prev points to the new head of the reversed list
    return prev


# 2- Source:https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """
    Merge two sorted linked lists into one sorted linked list.

    Args:
        list1 (Optional[ListNode]): Head of the first sorted linked list.
        list2 (Optional[ListNode]): Head of the second sorted linked list.

    Returns:
        Optional[ListNode]: Head of the merged sorted linked list.

    Complexity:
        Time: O(n + m)
        Space: O(1)
    """
    dummy = ListNode()  # Create a fake node to avoid special cases.
    tail = dummy  # tail always points to the last node in the merged list.

    current1 = list1  # Pointer to traverse list1.
    current2 = list2  # Pointer to traverse list2.

    while (
        current1 is not None and current2 is not None
    ):  # While both lists still have nodes.
        if current1.val <= current2.val:
            tail.next = current1  # Attach list1 node to the merged list.
            current1 = current1.next
        else:
            tail.next = current2  # Attach list2 node to the merged list.
            current2 = current2.next
        tail = tail.next  # Move tail to the newly added node.

    if current1 is not None and current2 is None:  # If list1 still has remaining nodes.
        tail.next = current1  # Attach the rest of list1.
    else:
        tail.next = current2  # Otherwise, attach the rest of list2.

    return dummy.next  # Skip the fake node and return the real head.


# 3- Source: https://neetcode.io/problems/linked-list-cycle-detection/question?list=neetcode150


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Determines if a linked list has a cycle in it.

        Traverses the linked list node by node, keeping track of visited nodes
        using a set to detect if any node is visited more than once.

        Note:
            This approach uses O(n) extra space for the visited set.
            An alternative is Floyd's Cycle Detection (slow/fast pointers),
            which uses O(1) extra space while keeping the same O(n) time.

        Args:
            head (Optional[ListNode]): The head node of the singly-linked list.

        Returns:
            bool: True if there is a cycle in the linked list, False otherwise.
        """
        if head is None:
            return False
        current = head
        visited = set()
        while current is not None:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False


# 4- Source: https://neetcode.io/problems/reorder-linked-list/question?list=neetcode150


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:  # noqa
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorder a linked list from L0 → L1 → ... → Ln
        to L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

        The reordering is done in place by changing the next
        pointers of the nodes. Node values are not modified.

        Note:
            This approach stores all nodes in a Python list,
            which uses O(n) extra space. An alternative with O(1)
            extra space is: find the middle (slow/fast pointers),
            reverse the second half, then merge the two halves
            alternately.

        Args:
            head: The head node of the singly linked list.

        Returns:
            None. The list is modified in place.
        """
        if head is None:
            return

        # Store all nodes in a list so we can access them by index.
        located = []
        current = head
        while current is not None:
            located.append(current)
            current = current.next

        # Use two pointers to pick nodes from both ends.
        # left starts at the first node, right starts at the last.
        n = len(located)
        left = 0
        right = n - 1
        reordered = []

        while left <= right:
            # Always take the node from the left side.
            reordered.append(located[left])

            # Take the node from the right side, but only if it
            # is not the same as the left one. This handles the
            # middle node when the list length is odd.
            if left != right:
                reordered.append(located[right])

            left += 1
            right -= 1

        # Reconnect the nodes in the new order by updating next
        # pointers. The last node must point to None.
        m = len(reordered)
        for i in range(m - 1):
            reordered[i].next = reordered[i + 1]
        reordered[m - 1].next = None


# 5- Source: https://neetcode.io/problems/remove-node-from-end-of-linked-list/question?list=neetcode150


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:  # noqa
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the n-th node from the end of a singly linked list.

        Uses the two-pointer technique: move the fast pointer n steps
        ahead of slow, then move both pointers together until fast
        reaches the last node. At that point, slow is right before
        the node that needs to be removed.

        Args:
            head (Optional[ListNode]): Head of the singly linked list.
            n (int): Position from the end (1-indexed).

        Returns:
            Optional[ListNode]: Head of the modified list.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        if head is None:
            return None

        fast = head
        slow = head

        # Move fast n steps ahead of slow.
        for _ in range(n):
            fast = fast.next

        # If fast is None, n equals the list length.
        # That means the target is the head itself.
        if fast is None:
            return head.next

        # Move both pointers until fast reaches the last node.
        # At that point, slow is right before the target node.
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Skip the target node by linking slow to the node after it.
        slow.next = slow.next.next

        return head
