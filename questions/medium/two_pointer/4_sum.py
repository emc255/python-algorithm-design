"""
18. 4Sum

Given an array nums of n integers,
return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

"""


def four_sum(nums: list, target: int) -> list:
    def k_sum(k, start, new_target):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                k_sum(k - 1, i + 1, new_target - nums[i])
                quad.pop()
            return

        left = start
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < new_target:
                left += 1
            elif nums[left] + nums[right] > new_target:
                right -= 1
            else:
                result.append(quad + [nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    result = []
    quad = []
    nums.sort()
    k_sum(4, 0, target)
    return result


print(four_sum([1, 0, -1, 0, -2, 2], 0))
print(four_sum([2, 2, 2, 2, 2, 2], 8))
