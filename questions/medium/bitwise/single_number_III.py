"""
Single Number III

Given an integer array nums,
in which exactly two elements appear only once
and all the other elements appear exactly twice.
Find the two elements that appear only once.
You can return the answer in any order.

You must write an algorithm
that runs in linear runtime complexity
and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]

Constraints:
2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice,
only two integers will appear once.

"""
from collections import Counter

from icecream import ic


def single_number(nums: list[int]) -> list[int]:
    # Step 1: XOR all numbers to get the XOR of the two unique numbers
    xor_result = 0
    for num in nums:
        xor_result ^= num

    # Step 2: Find the rightmost set bit in the xor_result
    set_bit = xor_result & -xor_result

    # Step 3: Divide the numbers into two groups and XOR within each group
    num1, num2 = 0, 0
    for num in nums:
        if num & set_bit:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]


def single_number_v2(nums: list[int]) -> list[int]:
    result = []
    numbers = Counter(nums)
    for k, v in numbers.items():
        if v == 1:
            result.append(k)
    return result


ic(single_number([1, 2, 1, 3, 2, 5]))
