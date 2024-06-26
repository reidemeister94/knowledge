"""
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/description/


A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list.
The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes
in the copied list such that the pointers in the original list and copied list represent
the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y,
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to,
or null if it does not point to any node.
Your code will only be given the head of the original linked list.



Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        old_map = {}
        idx = 0
        new_list = []
        current = head
        prev = None

        while current:
            old_map[current] = idx
            idx += 1
            new_node = Node(current.val)
            new_list.append(new_node)
            if prev:
                prev.next = new_node
            prev = new_node
            current = current.next

        current = head
        idx = 0
        while current:
            random_node = current.random
            if random_node:
                random_node_idx = old_map[random_node]
                new_list[idx].random = new_list[random_node_idx]
            idx += 1
            current = current.next

        return new_list[0]


# Approach 2: O(1) space
class Solution2:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # Step 1: Interweaving original and copied nodes
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next

        # Step 2: Assigning random pointers to the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Restoring the original list and separating the copied list
        current = head
        new_head = head.next
        while current:
            temp = current.next
            current.next = temp.next
            current = current.next
            if temp.next:
                temp.next = temp.next.next
            temp = temp.next

        return new_head
