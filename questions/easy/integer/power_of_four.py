"""
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true

Constraints:
-231 <= n <= 231 - 1

"""
from icecream import ic


def is_power_of_four(n: int) -> bool:
    if n == 1:
        return True
    if n <= 0 and n % 4:
        return False

    return is_power_of_four(n // 4)


ic(is_power_of_four(16))
