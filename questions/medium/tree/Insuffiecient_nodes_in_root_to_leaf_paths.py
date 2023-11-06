"""
1080. Insufficient Nodes in Root to Leaf Paths

Given the root of a binary tree and an integer limit,
delete all insufficient nodes in the tree simultaneously,
and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]

Example 2:
Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]

Example 3:
Input: root = [1,2,-3,-5,null,4,null], limit = -1
Output: [1,null,-3,4]

Constraints:
The number of nodes in the tree is in the range [1, 5000].
-105 <= Node.val <= 105
-109 <= limit <= 109

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def sufficient_subset(root: Optional['TreeNode'], limit: int) -> Optional['TreeNode']:
    def dfs(node, path_sum):
        if not node:
            return False
        path_sum += node.val
        if not node.left and not node.right:
            return path_sum >= limit
        left = dfs(node.left, path_sum)
        right = dfs(node.right, path_sum)
        if not left:
            node.left = None
        if not right:
            node.right = None
        return left or right

    result = dfs(root, 0)
    return root if result else None


def sufficient_subset_v2(root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
    # if 5 is root, we want to add to 22
    # if 4 is root, we want to add to 22-5=17
    # if 11 is root, we want to add to 6
    #
    # if 7 is root, we want to add to -1 (negative -> keep)
    # if 1 is root, we want to add to 5 (positive -> remove)

    if root is None:
        return root

    if root.left is None and root.right is None:
        return None if root.val < limit else root

    root.left = sufficient_subset_v2(root.left, limit - root.val)
    root.right = sufficient_subset_v2(root.right, limit - root.val)

    if root.left is None and root.right is None:
        return None

    return root


# Input: root = [1, 2, 3, 4, -99, -99, rr7, 8, 9, -99, -99, 12, 13, -99, 14], limit = 1
# Output: [1, 2, 3, 4, null, null, 7, 8, 9, null, 14]
# tree = Tree([1, 2, 3, 4, None, None, 7, 8, 9, None, None, 12, 13, None, 14]).root
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.right.right = TreeNode(7)
tree.right.right.left = TreeNode(8)
tree.right.right.right = TreeNode(9)
tree.right.right.right.left = TreeNode(12)
tree.right.right.right.right = TreeNode(12)
tree.right.right.right.right.right = TreeNode(14)
ic(sufficient_subset(tree, 1).print())
