"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""
from collections import deque
from typing import Optional

from shared.commons import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.pop()
        if node:
            queue.append(node.left)
            queue.append(node.right)

            node.left, node.right = node.right, node.left
    return root


def invert_tree_v2(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is not None:
        root.left, root.right = root.right, root.left
        invert_tree_v2(root.left)
        invert_tree_v2(root.right)

    return root


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)

invert_tree(head).print()
invert_tree_v2(head).print()
