"""
1038. Binary Search Tree to Greater Sum Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
such that every key of the original BST is changed to the original key plus
the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

Constraints:
The number of nodes in the tree is in the range [1, 100].
0 <= Node.val <= 100
All the values in the tree are unique.

Note: This question is the same as
538: https://leetcode.com/problems/convert-bst-to-greater-tree/

"""

from icecream import ic

from shared.commons import TreeNode


def bst_to_gst(root: TreeNode) -> TreeNode:
    def dfs(node: TreeNode):
        nonlocal current_sum

        if not node:
            return

        dfs(node.right)
        current_sum += node.val
        node.val = current_sum
        dfs(node.left)

    current_sum = 0
    dfs(root)
    return root


tree = TreeNode(4)
tree.left = TreeNode(1)
tree.right = TreeNode(6)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(2)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(7)
tree.left.right.right = TreeNode(1)
tree.right.right.right = TreeNode(8)

ic(bst_to_gst(tree).print())
