"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent t
he color red, white, and blue, respectively.

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
    start, end = 0, len(nums) - 1
    i = 0
    while i <= end:
        if nums[i] == 0:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1
        if nums[i] == 2:
            nums[end], nums[i] = nums[i], nums[end]
            end -= 1
            i -= 1
        i += 1

    ic(nums)


sort_colors(nums=[1, 0, 2, 1, 1, 0])
