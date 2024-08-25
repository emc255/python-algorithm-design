"""
238. Product of Array Except Self

Given an integer array nums,
return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed
to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time
and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

"""
from icecream import ic


def product_except_self(nums: list[int]) -> list[int]:
    result = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        prod = 1
        for j in range(len(nums)):
            if i == j:
                continue
            prod *= nums[j]
        result[i] = prod
    return result


def product_except_self_v2(nums: list[int]) -> list[int]:
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [0] * n

    # Compute left products
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # Compute right products
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # Compute the final result
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result


ic(product_except_self_v2([1, 2, 3, 4]))
