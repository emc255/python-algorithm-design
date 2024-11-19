"""
3097. Shortest Subarray With OR at Least K II

You are given an array nums of non-negative integers
and an integer k.

An array is called special if the bitwise OR of all
of its elements is at least k.

Return the length of the shortest special non-empty
subarray of nums, or return -1 if no special subarray exists.

Example 1:
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:
Input: nums = [2,1,8], k = 10
Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1. Hence, we return 1.

"""
from icecream import ic


def minimum_subarray_length(nums: list[int], k: int) -> int:
    def update_bit_counts(bit_counts3: list, number: int, delta: int) -> None:

        for pos in range(32):
            if number & (1 << pos):
                bit_counts3[pos] += delta

    def convert_bits_to_num(bit_counts2: list) -> int:
        result = 0
        for pos in range(32):
            if bit_counts2[pos]:
                result |= 1 << pos
        return result

    min_length = float("inf")
    window_start = window_end = 0
    bit_counts = [0] * 32

    while window_end < len(nums):
        update_bit_counts(bit_counts, nums[window_end], 1)

        while window_start <= window_end and convert_bits_to_num(bit_counts) >= k:
            min_length = min(min_length, window_end - window_start + 1)
            update_bit_counts(bit_counts, nums[window_start], -1)
            window_start += 1

        window_end += 1

    return -1 if min_length == float("inf") else min_length


ic(minimum_subarray_length(nums=[1, 2, 3], k=2))
