"""
988. Smallest String Starting From Leaf

You are given the root of a binary tree
where each node has a value in the range [0, 25]
representing the letters 'a' to 'z'.

Return the lexicographically smallest string
that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

Example 1:
Input: root = [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
Input: root = [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"

Constraints:
The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def smallest_from_leaf(root: Optional[TreeNode]) -> str:
    def dfs(node, current_sum):
        if not node:
            return ""
        current_sum = chr(97 + node.val) + current_sum
        if not node.left and not node.right:
            return current_sum
        left_smallest = dfs(node.left, current_sum)
        right_smallest = dfs(node.right, current_sum)
        if left_smallest == "" or (right_smallest != "" and left_smallest > right_smallest):
            return right_smallest
        else:
            return left_smallest

    return dfs(root, "")


def smallest_from_leaf_v2(root: Optional[TreeNode]) -> str:
    def dfs(node, current):
        if not node:
            return

        current = chr(ord('a') + node.val) + current
        if node.left and node.right:
            return min(dfs(node.left, current), dfs(node.right, current))
        elif node.left:
            return dfs(node.left, current)
        elif node.right:
            return dfs(node.right, current)
        else:
            return current

    return dfs(root, "")


tree = TreeNode(0)
tree.left = TreeNode(1)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(3)
tree.right.right = TreeNode(4)

ic(smallest_from_leaf(tree))
ic(smallest_from_leaf_v2(tree))
