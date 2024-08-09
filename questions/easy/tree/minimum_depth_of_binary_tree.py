"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from
the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def minimum_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return 1 + minimum_depth(root.right)
    if root.right is None:
        return 1 + minimum_depth(root.left)

    return min(minimum_depth(root.left), minimum_depth(root.right)) + 1


head = TreeNode(2)
head.right = TreeNode(3)
head.right.right = TreeNode(4)
head.right.right.right = TreeNode(5)
head.right.right.right.right = TreeNode(6)
head.right.right.right.right = TreeNode(6)

ic(minimum_depth(head))
