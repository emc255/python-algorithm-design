"""
Sum of Square Numbers

Given a non-negative integer c, decide whether
there are two integers a and b such that a2 + b2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false

Constraints:
0 <= c <= 231 - 1

"""
from icecream import ic


def judge_square_sum(c: int) -> bool:
    l, r = 1, int(c ** 0.5)
    while l <= r:
        square_sum = l * l + r * r
        if square_sum == c:
            return True
        elif square_sum > c:
            r -= 1
        else:
            l += 1
    return False


ic(judge_square_sum(4))
ic(judge_square_sum(5))
