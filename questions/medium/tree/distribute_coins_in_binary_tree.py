"""
Distribute Coins in Binary Tree

You are given the root of a binary tree
with n nodes where each node in the tree has node.val coins.
There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes
and move one coin from one node to another.
A move may be from parent to child, or from child to parent.

Return the minimum number of moves required
to make every node have exactly one coin.

Example 1:
Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree,
we move one coin to its left child,
and one coin to its right child.

Example 2:
Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root,
we move two coins to the root [taking two moves].
Then, we move one coin from the root of the tree to the right child.

Constraints:
The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def distribute_coins(root: Optional[TreeNode]) -> int:
    result = 0

    def dfs(node: Optional[TreeNode]):
        nonlocal result

        if not node:
            return [0, 0]

        l_size, l_coins = dfs(node.left)
        r_size, r_coins = dfs(node.right)

        size = 1 + l_size + r_size
        coins = node.val + l_coins + r_coins
        result += abs(size - coins)

        return [size, coins]

    dfs(root)
    return result


tree = TreeNode(0)
tree.left = TreeNode(3)
tree.right = TreeNode(0)

ic(distribute_coins(tree))
