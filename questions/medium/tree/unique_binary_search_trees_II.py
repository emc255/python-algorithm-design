"""
95. Unique Binary Search Trees II

Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output:
[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 8

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def generate_trees(n: int) -> list[Optional[TreeNode]]:
    def all_possible_BST(start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        if (start, end) in memo:
            return memo[(start, end)]

        # Iterate through all values from start to end to construct left and right subtree recursively.
        for i in range(start, end + 1):
            leftSubTrees = all_possible_BST(start, i - 1)
            rightSubTrees = all_possible_BST(i + 1, end)

            # Loop through all left and right subtrees and connect them to ith root.
            for left in leftSubTrees:
                for right in rightSubTrees:
                    root = TreeNode(i, left, right)
                    res.append(root)

        memo[(start, end)] = res
        return res

    memo = {}
    return all_possible_BST(1, n)


ic(generate_trees(3))
