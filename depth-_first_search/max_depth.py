"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

"""
from collections import deque
from typing import Optional

from shared.commons import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    stack = deque([(root, 1)])
    depth = 0
    while stack:
        node, current_depth = stack.pop()
        depth = max(depth, current_depth)
        current_depth += 1
        
        if node.left:
            stack.append((node.left, current_depth))
        if node.right:
            stack.append((node.right, current_depth))

    return depth


nodes = TreeNode(1)
nodes.left = TreeNode(10)
nodes.right = TreeNode(20)
nodes.right.left = TreeNode(15)
nodes.right.right = TreeNode(7)
print(max_depth(nodes))

print(max_depth(None))

nodes = TreeNode(1)
nodes.left = TreeNode(10)
nodes.right = TreeNode(20)
nodes.left.left = TreeNode(11)
nodes.right.left = TreeNode(15)
nodes.right.right = TreeNode(7)
print(max_depth(nodes))
