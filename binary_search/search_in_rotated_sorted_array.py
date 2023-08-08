"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array
is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

"""


def search(nums: list, target: int) -> int:
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if nums[mid_index] == target:
            return mid_index

        if nums[left_index] <= nums[mid_index]:
            if nums[left_index] <= target < nums[mid_index]:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
        else:
            if nums[mid_index] < target <= nums[right_index]:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1
    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([9, 1, 2, 3, 4, 5, 6], 9))
print(search([3, 1], 1))
