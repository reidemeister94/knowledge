"""
143. Reorder List
https://leetcode.com/problems/reorder-list/description/

You are given the head of a singly linked-list.
The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes.
Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# first approach:
# 1. create a stack to store the nodes
# 2. reorder the list
# 3. ensure the next of last node is None
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Create a stack to store the nodes
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next

        # Step 2: Reorder the list
        current = head
        for _ in range((len(stack) - 1) // 2):  # Iterate half the length of the list
            next_elem = stack.pop()  # Get the last element
            next_elem.next, current.next = current.next, next_elem
            current = next_elem.next

        # Step 3: Ensure the next of last node is None
        if stack:
            stack[-1].next = None


# second approach:
# 1. find the middle of the list
# 2. reverse the second half of the list
# 3. merge the two lists
class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # Step 3: Merge the two lists
        current = head
        while prev.next:
            next_elem = prev.next
            prev.next, current.next = current.next, prev
            current = current.next.next
            prev = next_elem
        prev.next = None
