"""
257. Binary Tree Paths

Given the root of a binary tree,
return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def binary_tree_paths(root: Optional[TreeNode]) -> list[str]:
    def dfs(node, path):
        if node:
            # Append the current node's value to the path
            path += str(node.val)
            # If it's a leaf node, add the path to result
            if not node.left and not node.right:
                result.append(path)
            else:
                # If not a leaf, add '->' and recurse
                path += '->'
                dfs(node.left, path)
                dfs(node.right, path)

    result = []
    dfs(root, '')
    return result


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.right = TreeNode(5)

ic(binary_tree_paths(head))
