"""
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100

"""
from collections import defaultdict

from icecream import ic


def number_identical_pairs(nums: list) -> int:
    pairs = defaultdict(int)
    result = 0

    for num in nums:
        if num in pairs:
            result += pairs[num]
        pairs[num] += 1

    return result


def number_identical_pairs_v2(nums: list) -> int:
    pairs = set()
    left = 0
    right = 1
    n = len(nums) - 1
    while left <= n:
        while right <= n:
            if nums[left] == nums[right] and left < right:
                pairs.add((left, right))
            right += 1
        left += 1
        right = left + 1

    return len(pairs)


ic(number_identical_pairs([1, 2, 3, 1, 1, 3]))
ic(number_identical_pairs([1, 1, 1, 1]))
ic(number_identical_pairs([1, 2, 3]))

ic(number_identical_pairs_v2([1, 2, 3, 1, 1, 3]))
ic(number_identical_pairs_v2([1, 1, 1, 1]))
ic(number_identical_pairs_v2([1, 2, 3]))
