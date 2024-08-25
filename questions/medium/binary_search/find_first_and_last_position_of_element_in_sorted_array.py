"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""
from icecream import ic


def search_range(nums: list, target: int) -> list:
    result = []
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            result.append(middle)
            left = middle - 1
            right = middle + 1

            while left >= 0 and nums[left] == target:
                result.insert(0, left)
                left -= 1

            while right <= len(nums) - 1 and nums[right] == target:
                result.append(right)
                right += 1

            if len(result) > 2:
                result = [result[0], result[len(result) - 1]]
            elif len(result) == 1:
                result = result + [middle]

            return result

        if nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return result if len(result) > 0 else [-1, -1]


def search_range_v2(nums, target):
    def binary_search(nums, target, left):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                if left:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low if left else high

    left_idx = binary_search(nums, target, True)
    right_idx = binary_search(nums, target, False)

    if left_idx <= right_idx < len(nums) and nums[left_idx] == nums[right_idx] == target:
        return [left_idx, right_idx]
    else:
        return [-1, -1]


ic(search_range([5, 7, 7, 8, 8, 10], 8))
ic(search_range([5, 7, 7, 8, 8, 10], 6))
ic(search_range([1], 1))
ic(search_range([1, 3], 1))
ic(search_range([1, 1, 1, 1], 1))
ic("==============")

ic(search_range_v2([5, 7, 7, 8, 8, 10], 8))
ic(search_range_v2([5, 7, 7, 8, 8, 10], 6))
ic(search_range_v2([1], 1))
ic(search_range_v2([1, 3], 1))
ic(search_range_v2([1, 1, 1, 1], 1))
