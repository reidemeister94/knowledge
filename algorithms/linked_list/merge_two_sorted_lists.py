"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        iter_1 = list1
        iter_2 = list2
        if not iter_1 and not iter_2:
            return None
        if not iter_1:
            return iter_2
        if not iter_2:
            return iter_1

        if iter_1.val <= iter_2.val:
            result = iter_1
            iter_1 = iter_1.next
        else:
            result = iter_2
            iter_2 = iter_2.next
        iter_3 = result

        while iter_1 and iter_2:
            if iter_1.val <= iter_2.val:
                iter_3.next = iter_1
                iter_1 = iter_1.next
            else:
                iter_3.next = iter_2
                iter_2 = iter_2.next
            iter_3 = iter_3.next

        while iter_1:
            iter_3.next = iter_1
            iter_1 = iter_1.next
            iter_3 = iter_3.next

        while iter_2:
            iter_3.next = iter_2
            iter_2 = iter_2.next
            iter_3 = iter_3.next

        return result
