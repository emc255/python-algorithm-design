"""
1814. Count Nice Pairs in an Array

You are given an array nums that consists of non-negative integers.
Let us define rev(x) as the reverse of the non-negative integer x.
For example, rev(123) = 321, and rev(120) = 21.
A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices.
Since that number can be too large, return it modulo 109 + 7.

Example 1:
Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

Example 2:
Input: nums = [13,10,35,24,76]
Output: 4

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 109

"""
from collections import defaultdict, Counter

from icecream import ic


def count_nice_pairs(nums: list) -> int:
    def reverse(n: int):
        reverse_number = 0
        while n > 0:
            digit = n % 10
            reverse_number = reverse_number * 10 + digit
            n //= 10
        return reverse_number

    nice_pairs = 0
    reverse_nums = defaultdict(int)
    MOD = 10 ** 9 + 7

    arr = []
    for i in range(len(nums)):
        arr.append(nums[i] - reverse(nums[i]))

    for num in arr:
        nice_pairs = (nice_pairs + reverse_nums[num]) % MOD
        reverse_nums[num] += 1

    return nice_pairs


def count_nice_pairs_v2(nums: list) -> int:
    modified = [i - int(str(i)[::-1]) for i in nums]

    count = 0
    ic(modified)
    for i in Counter(modified).values():
        count += i * (i - 1) // 2
    return count % (1000000000 + 7)


ic(count_nice_pairs([42, 11, 1, 97, 22, 2]))
ic(count_nice_pairs_v2([42, 11, 1, 97, 22, 2]))
