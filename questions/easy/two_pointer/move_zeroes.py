"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?

"""
from icecream import ic


def move_zero(numbers: list) -> list:
    left, right = 0, 0

    while right < len(numbers):
        if numbers[right] != 0:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
        right += 1

    return numbers


ic(move_zero([1, 0, 2, 0, 3]))
ic(move_zero([0, 1, 0, 3, 12]))
