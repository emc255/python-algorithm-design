"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

Follow up: Could you solve the problem in linear time and in O(1) space?

"""
from collections import defaultdict
from itertools import groupby

from icecream import ic


def majority_element(nums: list) -> list:
    result = []
    n = len(nums) / 3
    for k, v in groupby(sorted(nums)):
        if len(list(v)) > n:
            result.append(k)

    return result


def majority_element_v2(nums: list) -> list:
    count = defaultdict(int)
    result = []

    for n in nums:
        count[n] += 1

        if len(count) <= 2:
            continue

        new_count = defaultdict(int)
        for k, v in count.items():
            if v > 1:
                new_count[k] = v - 1
        count = new_count

    for n in count:
        if nums.count(n) > len(nums) // 3:
            result.append(n)

    return result


ic(majority_element([3, 2, 3]))
ic(majority_element_v2([3, 2, 3]))
