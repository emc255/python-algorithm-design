"""
1325. Delete Leaves With a Given Value

Given a binary tree root and an integer target,
delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target,
if its parent node becomes a leaf node and has the value target,
zit should also be deleted (you need to continue doing that until you cannot).



Example 1:
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green
with value (target = 2) are removed (Picture in left).
After removing, new nodes become leaf nodes
with value (target = 2) (Picture in center).

Example 2:
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]

Example 3:
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green
with value (target = 2) are removed at each step.

Constraints:
The number of nodes in the tree is in the range [1, 3000].
1 <= Node.val, target <= 1000

"""
from typing import Optional

from shared.commons import TreeNode


def remove_leaf_nodes(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if not root:
        return None

    root.left = remove_leaf_nodes(root.left, target)
    root.right = remove_leaf_nodes(root.right, target)

    if not root.left and not root.right and root.val == target:
        return None

    return root


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(2)
tree.right.left = TreeNode(2)
tree.right.right = TreeNode(4)

remove_leaf_nodes(tree, 2).print()
