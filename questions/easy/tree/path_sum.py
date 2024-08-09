"""
112. Path Sum

Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all
the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    def check_path_sum(node: TreeNode, total: int) -> bool:
        if node is None:
            return False

        total += node.val

        if node.left is None and node.right is None:
            return total == target_sum

        return check_path_sum(node.left, total) or check_path_sum(node.right, total)

    return check_path_sum(root, 0)


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.right.left = TreeNode(2)

ic(has_path_sum(head, 6))
