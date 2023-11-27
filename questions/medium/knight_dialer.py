"""
935. Knight Dialer

The chess knight has a unique movement,
it may move two squares vertically and one square horizontally,
or two squares horizontally and one square vertically
(with both forming the shape of an L).
The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

We have a chess knight and a phone pad as shown below,
the knight can only stand on a numeric cell (i.e. blue cell).

1 2 3
4 5 6
7 8 9
* 0 #

Given an integer n,
return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially
and then you should perform n - 1 jumps
to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

Example 1:
Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1,
so placing the knight over any numeric cell of the 10 cells is sufficient.

Example 2:
Input: n = 2
Output: 20
Explanation: All the valid number we can dial are
[04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

Example 3:
Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.

Constraints:
1 <= n <= 5000

"""
from icecream import ic


def knight_dialer(n: int) -> int:
    def count_phone_numbers(curr, remaining_steps):
        if remaining_steps == 0:
            return 1

        if (curr, remaining_steps) in memo:
            return memo[(curr, remaining_steps)]

        total = 0
        if curr in knight_moves:
            for next_digit in knight_moves[curr]:
                total = (total + count_phone_numbers(next_digit, remaining_steps - 1)) % MOD

        memo[(curr, remaining_steps)] = total
        return total

    memo = {}
    MOD = 10 ** 9 + 7
    phone_numbers = 0
    knight_moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }

    for start_digit in range(10):
        phone_numbers = (phone_numbers + count_phone_numbers(start_digit, n - 1)) % MOD

    return phone_numbers


def knight_dialer_v2(n: int) -> int:
    if n == 1:
        return 10

    a, b, c, d = 1, 2, 4, 2

    for i in range(n - 1):
        a, b, c, d = b, 2 * a + c, 2 * b + 2 * d, c

    return (a + b + c + d) % (10 ** 9 + 7)


ic(knight_dialer_v2(3131))
