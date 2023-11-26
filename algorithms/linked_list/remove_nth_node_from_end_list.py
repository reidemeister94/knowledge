"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list,
remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0

        while current:
            length += 1
            current = current.next

        idx_stop = length - n - 1
        if idx_stop < 0:
            return head.next
        idx_curr = 0
        current = head
        while idx_curr < idx_stop:
            current = current.next
            idx_curr += 1

        elem_to_remove = current.next
        new_next = elem_to_remove.next
        current.next = new_next

        return head


# approach 2: use stack and only one pass
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        stack = []

        while current:
            stack.append(current)
            current = current.next

        idx_stop = len(stack) - n - 1
        if idx_stop < 0:
            return head.next

        elem_to_remove = stack[idx_stop].next
        new_next = elem_to_remove.next
        stack[idx_stop].next = new_next

        return head
