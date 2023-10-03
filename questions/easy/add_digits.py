"""
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0


Constraints:
0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?

"""


def add_digits(num: int) -> int:
    digit_sum = 0

    while num != 0:
        digit = num % 10
        digit_sum += digit
        num //= 10

    if digit_sum <= 9:
        return digit_sum

    return add_digits(digit_sum)


def add_digits_v2(num: int) -> int:
    if num == 0:
        return 0
    return 1 + (num - 1) % 9


# print(add_digits(38))
# print(add_digits(0))
#
# print(add_digits_v2(38))
# print(add_digits_v2(0))
print(add_digits_v2(1453))
