"""Write a function that takes in a Binary Tree and returns its diameter. 
The diameter of a binary tree is defined as the length of its longest path, 
even if that path doesn't pass through the root of the tree.
A path is a collection of connected nodes in a tree, where no node is connected
to more than two other nodes. The length of a path is the number of edges between
the path's first node and its last node.
Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null."""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return get_tree_info(tree).diameter


def get_tree_info(tree):
    if tree is None:
        return TreeInfo(0, 0)

    left_tree_info = get_tree_info(tree.left)
    right_tree_info = get_tree_info(tree.right)

    longest_path_through_root = left_tree_info.height + right_tree_info.height
    max_diameter_so_far = max(left_tree_info.diameter, right_tree_info.diameter)
    curr_diameter = max(longest_path_through_root, max_diameter_so_far)
    curr_height = 1 + max(left_tree_info.height, right_tree_info.height)

    return TreeInfo(curr_diameter, curr_height)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
