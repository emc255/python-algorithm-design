"""
Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial,
could you find an O(n) solution using a different approach?

"""
import sys

from icecream import ic


def sorted_squares(nums: list[int]) -> list[int]:
    return sorted([x ** 2 for x in nums])


def sorted_squares_v2(nums: list[int]) -> list[int]:
    # Check if the array is empty or contains only one element
    if not nums:
        return []
    if len(nums) == 1:
        return [nums[0] ** 2]

    # Find the index of the last negative number
    smallest = sys.maxsize
    smallest_index = -1
    for i in range(len(nums)):

        if abs(nums[i]) < smallest:
            smallest = abs(nums[i])
            smallest_index = i

    # Initialize an array to store the squared results
    result = [0] * len(nums)

    # Start filling the result array
    result[0] = nums[smallest_index] ** 2
    l, r = smallest_index - 1, smallest_index + 1
    i = 1

    # Merge the squared values from both sides
    while l >= 0 and r < len(nums):
        left = nums[l] ** 2
        right = nums[r] ** 2
        if left <= right:
            result[i] = left
            l -= 1
        else:
            result[i] = right
            r += 1
        i += 1

    # Add remaining elements if any
    while l >= 0:
        result[i] = nums[l] ** 2
        l -= 1
        i += 1
    while r < len(nums):
        result[i] = nums[r] ** 2
        r += 1
        i += 1

    return result


def sorted_squares_v3(nums: list[int]) -> list[int]:
    p1 = 0
    p2 = len(nums) - 1
    idx = len(nums) - 1
    result = [0 for _ in range(len(nums))]

    while p1 <= p2:
        if abs(nums[p1]) < abs(nums[p2]):
            result[idx] = nums[p2] * nums[p2]
            p2 -= 1
        else:
            result[idx] = nums[p1] * nums[p1]
            p1 += 1

        idx -= 1

    return result


ic(sorted_squares_v2([-4, -1, 0, 3, 10]))
ic(sorted_squares_v2([-4, -3, -2]))
ic(sorted_squares_v3([-4, -3, -2]))
