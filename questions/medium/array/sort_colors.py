"""
Sort Colors

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent
the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
Follow up: Could you come up with a one-pass algorithm using only constant extra space?

"""
from icecream import ic


def sort_colors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero = 0
    one = 0
    two = 0
    for num in nums:
        if num == 0:
            zero += 1
        elif num == 1:
            one += 1
        elif num == 2:
            two += 1
    index = 0
    for i in range(zero):
        nums[index] = 0
        index += 1
    for i in range(one):
        nums[index] = 1
        index += 1
    for i in range(two):
        nums[index] = 2
        index += 1
    ic(nums)


sort_colors([2, 0, 2, 1, 1, 0])
