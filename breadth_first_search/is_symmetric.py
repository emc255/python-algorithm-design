"""
101. Symmetric Tree

Given the root of a binary tree,
check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

"""
from typing import Optional

from shared.commons import TreeNode


def is_symmetrical(root: Optional[TreeNode]) -> bool:
    def is_mirror(p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        return is_mirror(p.left, q.right) and is_mirror(p.right, q.left)

    return is_mirror(root.left, root.right)


nodes = TreeNode(1)
nodes.left = TreeNode(2)
nodes.right = TreeNode(2)
nodes.left.left = TreeNode(3)
nodes.right.left = TreeNode(3)
print(is_symmetrical(nodes))

nodes = TreeNode(1)
nodes.left = TreeNode(2)
nodes.right = TreeNode(2)
nodes.left.left = TreeNode(3)
nodes.left.right = TreeNode(4)
nodes.right.left = TreeNode(4)
nodes.right.right = TreeNode(3)
print(is_symmetrical(nodes))
