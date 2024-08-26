"""
145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?

"""
from collections import deque
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result = []
    nodes = deque([(root, False)])
    while nodes:
        node, visited = nodes.pop()
        if node:
            if visited:
                result.append(node.val)
            else:
                nodes.append((node, True))
                nodes.append((node.right, False))
                nodes.append((node.left, False))
    return result


head = TreeNode(1)
head.right = TreeNode(2)
head.right.left = TreeNode(3)

ic(postorder_traversal(head))
