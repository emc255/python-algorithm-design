"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?

"""


def majority_element(nums: list) -> int:
    nums.sort()
    slow = 0
    fast = 1
    previous_counter = 0
    counter = 0
    ans = nums[0]
    while slow < len(nums):
        if fast < len(nums) and nums[slow] == nums[fast]:
            counter += 1
            fast += 1
        else:
            if counter > previous_counter:
                previous_counter = counter
                ans = nums[slow]
            slow = fast
            fast = slow + 1
            counter = 0
    return ans


print(majority_element([2, 2, 1, 1, 1, 2, 2]))
