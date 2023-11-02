"""
501. Find Mode in Binary Search Tree

Given the root of a binary search tree (BST) with duplicates,
return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105


Follow up: Could you do that without using any extra space?
(Assume that the implicit stack space incurred due to recursion does not count).

"""
from collections import deque, defaultdict
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def find_mode(root: Optional[TreeNode]) -> list:
    stack = deque()
    stack.append(root)
    tree_values = defaultdict(int)
    max_frequency = 0
    while stack:
        node = stack.pop()
        if node:
            tree_values[node.val] = tree_values[node.val] + 1
            max_frequency = max(max_frequency, tree_values[node.val])
            stack.append(node.left)
            stack.append(node.right)
    result = []
    for k, v in tree_values.items():
        if v == max_frequency:
            result.append(k)
    return result


head = TreeNode(1)
head.left = TreeNode(2)
head.left.left = TreeNode(2)

ic(find_mode(head))
