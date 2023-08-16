"""
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.

"""
from typing import Optional

from shared.commons import TreeNode


def sorted_array_to_bst(nums: list) -> Optional[TreeNode]:
    if nums:
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = sorted_array_to_bst(nums[:mid])
        root.right = sorted_array_to_bst(nums[mid + 1:])
        return root

    return None


sorted_array_to_bst([-10, -3, 0, 5, 9]).print()
