"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums,
return the length of the longest consecutive
elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation:
The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore, its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109

"""
from icecream import ic


def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    nums = sorted(set(nums))
    left = 0
    res = 0

    for right in range(len(nums)):
        # check if window breaks
        if right > 0 and nums[right] != nums[right - 1] + 1:
            left = right  # shrink window to current element
        res = max(res, right - left + 1)

    return res


ic(longest_consecutive(nums=[1, 0, 1, 2]))
