"""
390. Elimination Game

You have a list arr of all integers in the range [1, n] sorted
in a strictly increasing order. Apply the following algorithm on arr:

Starting from left to right, remove the first number and every
other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left,
remove the rightmost number and every other number from the remaining
numbers.

Keep repeating the steps again, alternating left to right
and right to left, until a single number remains.

Given the integer n, return the last number that remains in arr.

Example 1:
Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 109

"""
from icecream import ic


def last_remaining(n: int) -> int:
    result = [i + 1 for i in range(n)]
    reverse = False
    while len(result) > 1:
        if reverse:
            result = [result[i] for i in range(len(result) - 2, -1, -2)]
        else:
            result = [result[i] for i in range(1, len(result), 2)]
        result.sort()
        reverse = not reverse
    return result[0]


def last_remaining_v2(n: int) -> int:
    head = 1
    step = 1
    left_to_right = True

    while n > 1:
        if left_to_right or n % 2 == 1:
            head += step
        step *= 2
        n //= 2
        left_to_right = not left_to_right

    return head


# ic(last_remaining(n=9))
ic(last_remaining_v2(n=1222))
