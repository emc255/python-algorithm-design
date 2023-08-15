"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?

"""
from collections import deque
from typing import Optional

from shared.commons import TreeNode


def inorder_traversal(root: Optional[TreeNode]) -> list:
    stack = deque([(root, False)])
    ans = []
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                ans.append(node.val)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

    return ans


head = TreeNode(1)
head.right = TreeNode(2)
head.right.left = TreeNode(3)
head.right.right = TreeNode(5)
print(inorder_traversal(head))
