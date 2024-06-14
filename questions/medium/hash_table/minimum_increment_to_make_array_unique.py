"""
Minimum Increment to Make Array Unique

ou are given an integer array nums.
In one move, you can pick an index i
where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves
that it is impossible for the array to have all unique values.

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105

"""
from collections import Counter

from icecream import ic


def minimum_increment_for_unique(nums: list[int]) -> int:
    nums.sort()
    result = 0
    prev = nums[0]  # Start with the first element in the sorted list

    for i in range(1, len(nums)):
        if nums[i] <= prev:
            result += prev + 1 - nums[i]
            prev += 1
        else:
            prev = nums[i]

    return result


def minimum_increment_for_unique_v2(nums: list[int]) -> int:
    result = 0
    counter_numbers = Counter(nums)
    set_numbers = set(counter_numbers.keys())
    sorted_counter_numbers = dict(sorted(counter_numbers.items()))
    for k, v in sorted_counter_numbers.items():
        for i in range(v - 1):
            num = k
            while num in set_numbers:
                num += 1
            set_numbers.add(num)
            result += num - k

    return result


ic(minimum_increment_for_unique([3, 2, 1, 2, 1, 1, 7]))
