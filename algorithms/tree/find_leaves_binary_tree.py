"""
https://leetcode.com/problems/find-leaves-of-binary-tree/description/
366. Find Leaves of Binary Tree

Given the root of a binary tree,
collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered
correct answers since per each level it does not matter
the order on which elements are returned.

Example 2:

Input: root = [1]
Output: [[1]]

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_leaves(self, node: TreeNode, leaves: List[int]) -> List[int]:
        if node.left:
            if not node.left.left and not node.left.right:
                leaves.append(node.left.val)
                node.left = None
            else:
                self.find_leaves(node.left, leaves)

        if node.right:
            if not node.right.left and not node.right.right:
                leaves.append(node.right.val)
                node.right = None
            else:
                self.find_leaves(node.right, leaves)

        return leaves

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        while root.left or root.right:
            output.append(self.find_leaves(root, leaves=[]))
        output.append([root.val])
        return output
