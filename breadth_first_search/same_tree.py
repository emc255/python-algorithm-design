"""
100. Same Tree

Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

"""
from typing import Optional

from shared.commons import TreeNode


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True

    if p is None or q is None or p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


nodes_1 = TreeNode(1)
nodes_1.left = TreeNode(2)

nodes_2 = TreeNode(1)
nodes_2.right = TreeNode(2)

print(is_same_tree(nodes_1, nodes_2))
