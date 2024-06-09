"""
Subarray Sums Divisible by K

Given an integer array nums and an integer k,
return the number of non-empty sub arrays that have a sum divisible by k.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 sub arrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0

Constraints:
1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104

"""
from icecream import ic


def sub_arrays_div_by_k(nums: list[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    remainder_count = {0: 1}  # Initialize with 0:1 to handle sub arrays directly divisible by k

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k

        # Handle negative remainders
        if remainder < 0:
            remainder += k

        # If remainder has been seen before, add the number of times it was seen to the count
        if remainder in remainder_count:
            count += remainder_count[remainder]

        # Update the remainder count in the hashmap
        if remainder in remainder_count:
            remainder_count[remainder] += 1
        else:
            remainder_count[remainder] = 1

    return count


ic(sub_arrays_div_by_k([4, 5, 0, -2, -3, 1], 5))
