"""
Rotate Array

Given an integer array nums,
rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Follow up:
Try to come up with as many solutions as you can.
There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

"""
from icecream import ic


def rotate(nums: list[int], k: int) -> None:
    """
    instead of nums=, put nums[:]=
    good catch. so if you use the slicing assignment,
    you modify the existing list.
    if you only use nums=, then you're reassigning nums to a newly created list
    """
    k = k % len(nums)  # This handles the case where k > len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    ic(nums)


ic(rotate([1, 2, 3, 4, 5, 6, 7], 5))
ic(rotate([1, 2], 5))
