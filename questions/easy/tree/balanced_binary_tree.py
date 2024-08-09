"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def is_balanced(root: Optional[TreeNode]) -> bool:
    def depth(node: TreeNode) -> int:
        if node is None:
            return 0

        left_node_depth = depth(node.left)
        right_node_depth = depth(node.right)

        if left_node_depth < 0 or right_node_depth < 0 or abs(left_node_depth - right_node_depth) > 1:
            return -1

        return max(left_node_depth, right_node_depth) + 1

    return depth(root) >= 0


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(2)
head.left.left = TreeNode(3)
head.left.right = TreeNode(3)
head.left.left.left = TreeNode(4)
head.left.left.right = TreeNode(4)
ic(is_balanced(head))
