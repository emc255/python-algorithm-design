"""
951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows:
choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only
if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2,
return true if the two trees are flip equivalent or false otherwise.



Example 1:
Flipped Trees Diagram
Input:
root1 = [1,2,3,4,5,6,null,null,null,7,8],
root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation:
We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false

Constraints:
The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def flip_equivalent(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    # Base case: If both are None, they are flip equivalent
    if not root1 and not root2:
        return True
    # If only one is None, they are not equivalent
    if not root1 or not root2:
        return False
    # If the values of root nodes are different, they are not equivalent
    if root1.val != root2.val:
        return False

    # Check if trees are flip equivalent without flipping or with flipping
    return (flip_equivalent(root1.left, root2.left) and flip_equivalent(root1.right, root2.right)) or \
        (flip_equivalent(root1.left, root2.right) and flip_equivalent(root1.right, root2.left))


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)
tree1.right.left = TreeNode(6)
tree1.left.right.left = TreeNode(7)
tree1.left.right.right = TreeNode(8)

tree2 = TreeNode(1)
tree2.left = TreeNode(3)
tree2.right = TreeNode(2)

tree2.left.right = TreeNode(6)
tree2.right.left = TreeNode(4)
tree2.right.right = TreeNode(5)
tree2.right.right.left = TreeNode(8)
tree2.right.right.right = TreeNode(7)

ic(flip_equivalent(tree1, tree2))
