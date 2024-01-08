"""
Range Sum of BST

Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:
The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

"""
from collections import deque
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
    stack = deque([root])
    result = 0
    while stack:
        node = stack.pop()
        if node:
            stack.append(node.left)
            stack.append(node.right)
            if low <= node.val <= high:
                result += node.val

    return result


tree = TreeNode(10)
tree.left = TreeNode(5)
tree.right = TreeNode(15)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(7)
tree.right.right = TreeNode(18)

ic(range_sum_bst(tree, 7, 15))
