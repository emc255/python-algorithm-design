"""
650. 2 Keys Keyboard

There is only one character 'A' on the screen of a notepad.
You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on
the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get
the character 'A' exactly n times on the screen.

Example 1:
Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Example 2:
Input: n = 1
Output: 0

Constraints:
1 <= n <= 1000

"""
from icecream import ic


def min_steps(n: int) -> int:
    def dp(count, paste):
        if count == n:
            return 0
        if count > n:
            return float('inf')
        if (count, paste) in memo:
            return memo[(count, paste)]

        # decision copy and copy paste
        copy = 1 + dp(count + paste, paste)
        copy_paste = 2 + dp(count + count, count)
        memo[(count, paste)] = min(copy, copy_paste)
        return memo[(count, paste)]

    memo = {}
    if n == 1:
        return 0

    return 1 + dp(1, 1)


ic(min_steps(3))
