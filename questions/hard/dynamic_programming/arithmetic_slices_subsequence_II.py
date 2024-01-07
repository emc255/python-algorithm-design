"""
Arithmetic Slices II - Subsequence

Given an integer array nums,
return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic
if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that
can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

Example 1:
Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

Example 2:
Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.

Constraints:
1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1

"""
from collections import defaultdict

from icecream import ic


def number_of_arithmetic_slices(nums: list[int]) -> int:
    result = 0
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    #  dp[i][difference] -> # of subsequence ending at i, with difference
    for i in range(n):
        for j in range(i):
            difference = nums[i] - nums[j]
            dp[i][difference] += 1 + dp[j][difference]
            result += 1 + dp[j][difference]
    return result - (n * (n - 1) // 2)


def number_of_arithmetic_slices_v2(nums: list[int]) -> int:
    n = len(nums)
    count = 0
    subsequences = {}

    for i in range(n):
        subsequences[i] = {}
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in subsequences[j]:
                subsequences[i][diff] = subsequences[i].get(diff, 0) + subsequences[j][diff] + 1
                count += subsequences[j][diff]
            else:
                subsequences[i][diff] = subsequences[i].get(diff, 0) + 1

    return count


ic(number_of_arithmetic_slices([2, 4, 6, 8, 10]))
