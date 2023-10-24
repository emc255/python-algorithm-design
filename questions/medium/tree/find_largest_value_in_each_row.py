"""
515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def largest_values(root: Optional['TreeNode']) -> list:
    result = {}
    stack = [(root, 0)]
    while stack:
        node, level = stack.pop()
        if node:
            if level in result:
                result[level] = max(result[level], node.val)
            else:
                result[level] = node.val
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))

    return list(result.values())


tree = TreeNode(1)
tree.left = TreeNode(3)
tree.right = TreeNode(2)
tree.left.left = TreeNode(5)
tree.left.right = TreeNode(3)
tree.right.right = TreeNode(9)

ic(largest_values(tree))
