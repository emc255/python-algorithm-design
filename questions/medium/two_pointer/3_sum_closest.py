"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

"""


def three_sum_closest(nums: list, target: int) -> int:
    result = 2 ** 31 - 1
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            total_sum = nums[i] + nums[left] + nums[right]
            if target == total_sum:
                return target

            if abs(total_sum - target) < abs(result - target):
                result = total_sum

            if total_sum < target:
                left += 1
            elif total_sum > target:
                right -= 1

    return result


print(three_sum_closest([-1, 2, 1, -4], 1))
print(three_sum_closest([0, 0, 0], 1))

print(three_sum_closest([0, 1, 2], 3))
