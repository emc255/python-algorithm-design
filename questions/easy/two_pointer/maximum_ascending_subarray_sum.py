"""
1800. Maximum Ascending Subarray Sum

Given an array of positive integers nums,
return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending
if for all i where l <= i < r, numsi  < numsi+1.
Note that a subarray of size 1 is ascending.

Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100

"""
from icecream import ic


def max_ascending_sum(nums: list[int]) -> int:
    result = 0
    r = 0
    l = 1
    while r < len(nums) - 1:
        temp = 0
        temp += nums[r]
        while l < len(nums) and nums[r] < nums[l]:
            temp += nums[l]
            r += 1
            l += 1
        r = l
        l += 1
        result = max(result, temp)

    return result


ic(max_ascending_sum(nums=[10, 20, 30, 5, 10, 50]))
ic(max_ascending_sum(nums=[12, 17, 15, 13, 10, 11, 12]))
