"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

Constraints:
-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?

"""
from icecream import ic


def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False

    return (n & (n - 1)) == 0


def is_power_of(n: int) -> bool:
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1


ic(is_power_of_two(16))
ic(is_power_of_two(15))
ic(is_power_of(81))
