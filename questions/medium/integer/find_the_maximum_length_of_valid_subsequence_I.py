"""
3201. Find the Maximum Length of Valid Subsequence I

You are given an integer array nums.
A subsequence sub of nums with length x is called valid
if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 ==
... == (sub[x - 2] + sub[x - 1]) % 2.

Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another
array by deleting some or no elements without changing the
order of the remaining elements.

Example 1:
Input: nums = [1,2,3,4]
Output: 4
Explanation:
The longest valid subsequence is [1, 2, 3, 4].

Example 2:
Input: nums = [1,2,1,1,2,1,2]
Output: 6
Explanation:
The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:
Input: nums = [1,3]
Output: 2
Explanation:
The longest valid subsequence is [1, 3].

Constraints:
2 <= nums.length <= 2 * 105
1 <= nums[i] <= 107

"""

from icecream import ic


def maximum_length(nums: list[int]) -> int:
    odd_prev_p = 0
    odd_prev_q = 0
    even_prev_p = 0
    even_prev_q = 0
    for num in nums:
        if num % 2 == 1:
            odd_prev_p += 1
            odd_prev_q = 1 + even_prev_q
        else:
            even_prev_p += 1
            even_prev_q = 1 + odd_prev_q
    return max(odd_prev_p, odd_prev_q, even_prev_p, even_prev_q)


ic(maximum_length(nums=[1, 1, 1, 1, 2, 1, 2]))
