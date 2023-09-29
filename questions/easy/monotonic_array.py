"""
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false

Constraints:
1 <= nums.length <= 105
-105 <= nums[i] <= 105

"""


def is_monotonic(nums: list) -> bool:
    increasing = True
    starting_index = 0

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        else:
            increasing = nums[i] > nums[i - 1]
            starting_index = i
            break

    if increasing:
        for i in range(starting_index, len(nums)):
            if nums[i] < nums[i - 1] and nums[i] != nums[i - 1]:
                return False
    else:
        for i in range(starting_index, len(nums)):
            if nums[i] > nums[i - 1] and nums[i] != nums[i - 1]:
                return False

    return True


def is_monotonic_v2(nums: list) -> bool:
    if len(nums) < 2:
        return True

    direction = 0  # 0 means unknown, 1 means increasing, -1 means decreasing

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:  # increasing
            if direction == 0:
                direction = 1
            elif direction == -1:
                return False
        elif nums[i] < nums[i - 1]:  # decreasing
            if direction == 0:
                direction = -1
            elif direction == 1:
                return False

    return True


def is_monotonic_v3(nums):
    increasing = None  # Initialize as None to handle an empty list
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        if increasing is None:
            increasing = nums[i] > nums[i - 1]

        elif increasing != (nums[i] > nums[i - 1]):
            return False
    return True


print(is_monotonic([1, 3, 2]))
print(is_monotonic([1, 2, 2, 3]))

print(is_monotonic_v2([1, 3, 2]))
print(is_monotonic_v2([1, 2, 2, 3]))
