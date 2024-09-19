"""
179. Largest Number

Given a list of non-negative integers nums,
arrange them such that they form the largest number and return it.

Since the result may be very large,
so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109

"""
from functools import cmp_to_key

from icecream import ic


def largest_number(nums: list[int]) -> str:
    def compare(x, y):
        if x + y > y + x:
            return -1
        else:
            return 1

    nums_str = list(map(str, nums))
    nums_str.sort(key=cmp_to_key(compare))
    largest_num = ''.join(nums_str)

    return '0' if largest_num[0] == '0' else largest_num


ic(largest_number([10, 2]))
