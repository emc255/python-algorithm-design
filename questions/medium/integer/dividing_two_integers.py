"""
29. Divide Two Integers

Given two integers dividend and divisor,
divide two integers without using multiplication,
division, and mod operator.

The integer division should truncate toward zero,
which means losing its fractional part. For example,
8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−231, 231 − 1].
For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1,
and if the quotient is strictly less than -231, then return -231.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""
from icecream import ic


def divide(dividend: int, divisor: int) -> int:
    result = 0
    new_dividend = abs(dividend)
    new_divisor = abs(divisor)
    is_negative = (dividend < 0) ^ (divisor < 0)

    if new_divisor == 1:
        result = new_dividend
        return -result if is_negative else min(result, 2 ** 31 - 1)

    while new_dividend >= new_divisor:
        new_dividend -= new_divisor
        result += 1

    return -result if is_negative else min(result, 2 ** 31 - 1)


def divide_v2(dividend: int, divisor: int) -> int:
    int_max = 2 ** 31 - 1
    int_min = -2 ** 31

    is_negative = (dividend < 0) ^ (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    if dividend < divisor:
        return 0

    result = 0
    while dividend >= divisor:
        temp_divisor = divisor
        multiple = 1

        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1
        dividend -= temp_divisor
        result += multiple

    result = -result if is_negative else result
    return min(max(result, int_min), int_max)


ic(divide_v2(-2147483648, 2))
ic(divide(1, -1))
ic(divide(-1, 1))
ic(divide_v2(7, -3))
ic(divide(10, 3))
