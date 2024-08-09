"""
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537

Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

"""
from icecream import ic


def tri_fibonacci(n: int) -> int:
    def fibonacci(number):
        if number in memoize:
            return memoize[number]

        if number == 0:
            return 0
        if number == 3:
            return 2
        if number == 1 or number == 2:
            return 1

        memoize[number] = fibonacci(number - 1) + fibonacci(number - 2) + fibonacci(number - 3)
        return memoize[number]

    memoize = {}
    return fibonacci(n)


def tri_fibonacci_v2(n: int) -> int:
    t = [0, 1, 1]
    if n < 3:
        return t[n]

    for i in range(3, n + 1):
        t[0], t[1], t[2] = t[1], t[2], sum(t)
    return t[2]


ic(tri_fibonacci_v2(4))

ic(tri_fibonacci(4))
