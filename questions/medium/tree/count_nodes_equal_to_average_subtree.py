"""
2265. Count Nodes Equal to Average of Subtree

Given the root of a binary tree,
return the number of nodes where
the value of the node is equal to the average of the values in its subtree.

Note:
The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.

Example 1:
Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation:
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

Example 2:
Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000

"""
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def average_of_subtree(root: Optional['TreeNode']) -> int:
    def post_order(head: Optional['TreeNode']):
        if head is None:
            return 0, 0, 0

        left_sum, left_nodes, left_count = post_order(head.left)
        right_sum, right_nodes, right_count = post_order(head.right)

        total_sum = left_sum + head.val + right_sum
        nodes_level = left_nodes + right_nodes + 1
        count = left_count + right_count

        if head.val == total_sum // nodes_level:
            count += 1

        return total_sum, nodes_level, count

    return post_order(root)[2]


# def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
#        def postorder(rt: Optional[TreeNode]) -> Tuple[int, int, int]:
#            """
#            :param rt:
#            :return: for tree rooted at rt:
#                1. sum of values of all the nodes in the tree
#                2. number of nodes in the tree
#                3. number of nodes with value equal to average value
#            """
#            if not rt:
#                return 0, 0, 0
#
#            (l_sum, l_nodes, l_cnt), (r_sum, r_nodes, r_cnt) = postorder(rt.left), postorder(rt.right)
#
#            val = rt.val
#
#            sum_ = l_sum + val + r_sum  # "sum" is python defined keyword, so using "sum_"
#            nodes = l_nodes + 1 + r_nodes
#            cnt = l_cnt + r_cnt
#
#            if sum_ // nodes == val:
#                cnt += 1
#
#            return sum_, nodes, cnt
#
#        return postorder(root)[2]

tree = TreeNode(4)
tree.left = TreeNode(8)
tree.right = TreeNode(5)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(1)
tree.right.right = TreeNode(6)

ic(average_of_subtree(tree))
