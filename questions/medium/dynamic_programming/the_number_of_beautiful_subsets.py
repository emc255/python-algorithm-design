"""
2597. The Number of Beautiful Subsets

You are given an array nums of positive integers and a positive integer k.
A subset of nums is beautiful if it does not contain two integers
with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained
by deleting some (possibly none) elements from nums.
Two subsets are different if and only if the chosen indices to delete are different.

Example 1:
Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

Example 2:
Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

Constraints:
1 <= nums.length <= 20
1 <= nums[i], k <= 1000

"""
from icecream import ic


def beautiful_subsets(nums: list[int], k: int) -> int:
    def dp(start, current_subset):
        nonlocal result

        if current_subset:
            result += 1  # Count the current subset if it's non-empty

        for i in range(start, len(nums)):
            # Check if the current element can be added to the subset
            if all(abs(nums[i] - num) != k for num in current_subset):
                current_subset.append(nums[i])
                dp(i + 1, current_subset)
                current_subset.pop()  # Backtrack to explore other possibilities

    result = 0
    nums.sort()  # Sort the nums array to handle subsets in a systematic way
    dp(0, [])
    return result


ic(beautiful_subsets([2, 4, 6, 8], 2))
ic(beautiful_subsets([2], 2))
