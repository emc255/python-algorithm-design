"""
Binary Subarrays With Sum

Given a binary array nums and an integer goal,
return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:
1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length

"""
from icecream import ic


def num_sub_arrays_with_sum(nums: list[int], goal: int) -> int:
    def helper(new_goal):
        if new_goal < 0:
            return 0

        result = 0
        l = 0
        current_sum = 0
        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum > new_goal:
                current_sum -= nums[l]
                l += 1
            result += (r - l + 1)
        return result

    return helper(goal) - helper(goal - 1)


ic(num_sub_arrays_with_sum([1, 0, 1, 0, 1], 2))
