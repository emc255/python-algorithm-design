"""
222. Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.

"""
from typing import Optional

from shared.commons import TreeNode


def count_nodes(root: Optional[TreeNode]) -> int:
    count = 0
    stack = []

    stack.append(root)
    while stack:
        node = stack.pop()
        if node:
            count += 1
            stack.append(node.left)
            stack.append(node.right)

    return count


def count_nodes_v2(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)

print(count_nodes(head))
print(count_nodes_v2(head))
