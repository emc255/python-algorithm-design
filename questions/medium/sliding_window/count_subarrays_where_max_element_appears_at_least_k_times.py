"""
2962. Count Subarrays Where Max Element Appears at Least K Times

You are given an integer array nums and a positive integer k.

Return the number of subarrays
where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain
the element 3 at least 2 times are: [1,3,2,3],
[1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:
Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105

"""

from icecream import ic


def count_sub_arrays(nums: list[int], k: int) -> int:
    max_element = max(nums)
    ans = start = max_elements_in_window = 0

    for end in range(len(nums)):
        if nums[end] == max_element:
            max_elements_in_window += 1
        while max_elements_in_window == k:
            if nums[start] == max_element:
                max_elements_in_window -= 1
            start += 1
        ans += start
    return ans


def count_sub_arrays_v2(nums: list[int], k: int) -> int:
    max_number = max(nums)
    result = 0
    count = 0
    left = 0
    for num in nums:
        if num == max_number:
            count += 1
        while count == k:
            if nums[left] == max_number:
                count -= 1
            left += 1
        result += left

    return result


ic(count_sub_arrays([1, 3, 2, 3, 3], 2))
ic(count_sub_arrays([28, 5, 58, 91, 24, 91, 53, 9, 48, 85, 16, 70, 91, 91, 47, 91, 61, 4, 54, 61, 49], 1))
