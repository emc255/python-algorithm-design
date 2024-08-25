"""
1457. Pseudo-Palindromic Paths in a Binary Tree

Given a binary tree where node values are digits from 1 to 9.
A path in the binary tree is said to be pseudo-palindromic
if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:
Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree.
There are three paths going from the root node to leaf nodes:
the red path [2,3,3], the green path [2,1,1], and the path [2,3,1].
Among these paths only red path and green path are
pseudo-palindromic paths since the red path [2,3,3]
can be rearranged in [3,2,3] (palindrome) and
the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree.
There are three paths going from the root node to leaf nodes:
the green path [2,1,1], the path [2,1,3,1], and the path [2,1].
Among these paths only the green path is pseudo-palindromic
since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
Input: root = [9]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 9

"""
from collections import defaultdict
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def pseudo_palindromic_paths(root: Optional[TreeNode]) -> int:
    def dfs(nodes):
        nonlocal odd
        if not nodes:
            return 0
        count[nodes.val] += 1
        odd_change = -1 if count[nodes.val] % 2 == 0 else 1
        odd += odd_change
        if not nodes.left and not nodes.right:
            result = 1 if odd <= 1 else 0
        else:
            result = dfs(nodes.left) + dfs(nodes.right)
        odd -= odd_change
        count[nodes.val] -= 1

        return result

    count = defaultdict(int)
    odd = 0
    return dfs(root)


tree = TreeNode(2)
tree.left = TreeNode(3)
tree.right = TreeNode(1)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(1)
tree.right.right = TreeNode(1)

ic(pseudo_palindromic_paths(tree))
