"""
219. Contains Duplicate II

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

"""


def contains_nearby_duplicate(nums: list, k: int) -> bool:
    window = set()
    left_index = 0

    for i in range(len(nums)):
        if i - left_index > k:
            window.remove(nums[left_index])
            left_index += 1

        if nums[i] in window:
            return True

        window.add(nums[i])

    return False


print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))
print(contains_nearby_duplicate([1, 0, 1, 1], 1))
