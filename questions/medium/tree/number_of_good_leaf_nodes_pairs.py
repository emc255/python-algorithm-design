"""
1530. Number of Good Leaf Nodes Pairs

You are given the root of a binary tree and an integer distance.
A pair of two different leaf nodes of a binary tree is said to be good if
the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Example 1:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of
the shortest path between them is 3. This is the only good pair.

Example 2:
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2.
The pair [4,6] is not good because the length of ther shortest path between them is 4.

Example 3:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2],
distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Constraints:
The number of nodes in the tree is in the range [1, 210].
1 <= Node.val <= 100
1 <= distance <= 10

"""
from icecream import ic

from shared.commons import TreeNode


def count_pairs(root: TreeNode, distance: int) -> int:
    def dfs(node: TreeNode):
        nonlocal result
        if not node:
            return []
        if not node.left and not node.right:
            return [1]

        left_node = dfs(node.left)
        right_node = dfs(node.right)

        for d1 in left_node:
            for d2 in right_node:
                if d1 + d2 <= distance:
                    result += 1

        levels = left_node + right_node
        return [l + 1 for l in levels]

    result = 0
    dfs(root)
    return result


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(4)
ic(count_pairs(tree, 3))
