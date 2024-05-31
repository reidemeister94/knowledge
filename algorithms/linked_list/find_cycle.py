"""

141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's
next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail
connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail
connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.


Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# approach 1: hash table
# O(n) time, O(n) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        current = head

        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False


# approach 2: two pointers - Floyd's Cycle Finding Algorithm
# https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare
# O(n) time, O(1) space
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        current_fast = head.next if head else None

        while current and current_fast and current_fast.next:
            if current == current_fast:
                return True
            current = current.next
            current_fast = current_fast.next.next
        return False
