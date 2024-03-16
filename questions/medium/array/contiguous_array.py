"""
Contiguous Array

Given a binary array nums,
return the maximum length of a contiguous subarray
with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray
with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray
with equal number of 0 and 1.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""
from icecream import ic


def find_max_length(nums: list[int]) -> int:
    one = 0
    zero = 0
    result = 0
    difference_index = {}
    for i, n in enumerate(nums):
        if n == 0:
            zero += 1
        else:
            one += 1

        difference = one - zero
        if difference not in difference_index:
            difference_index[difference] = i

        if one == zero:
            result = one + zero
        else:
            result = max(result, i - difference_index[difference])

    return result


ic(find_max_length([0, 1, 0]))
