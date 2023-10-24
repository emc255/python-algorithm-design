"""
1793. Maximum Score of a Good Subarray

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i],
nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

Example 1:
Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.

Example 2:
Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length

"""
from icecream import ic


def maximum_score(nums: list, k: int) -> int:
    left, right, n = k, k, len(nums) - 1
    min_value = nums[k]
    max_score = min_value

    while left > 0 or right < n:
        left_value = nums[left - 1] if left > 0 else 0
        right_value = nums[right + 1] if right < n else 0
        if left_value > right_value:
            left -= 1
            min_value = min(min_value, left_value)
        else:
            right += 1
            min_value = min(min_value, right_value)
        max_score = max(max_score, min_value * (right - left + 1))

    return max_score


def maximum_score_v2(nums: list, k: int) -> int:
    left, right, n = k, k, len(nums) - 1
    min_value = nums[k]
    max_score = min_value

    while left > 0 or right < n:
        if left == 0 or (right < n and nums[right + 1] > nums[left - 1]):
            right += 1
        else:
            left -= 1
        min_value = min(min_value, nums[left], nums[right])
        max_score = max(max_score, min_value * (right - left + 1))
    return max_score


ic(maximum_score([1, 4, 3, 7, 4, 5], 2))
