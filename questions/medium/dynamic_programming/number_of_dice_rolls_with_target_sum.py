"""
Number of Dice Rolls With Target Sum

You have n dice, and each die has k faces numbered from 1 to k.

Given three integers n, k, and target,
return the number of possible ways (out of the kn total ways) to roll the dice,
so the sum of the face-up numbers equals target.
Since the answer may be too large, return it modulo 109 + 7.



Example 1:
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.

Constraints:
1 <= n, k <= 30
1 <= target <= 1000

"""
from icecream import ic


def num_rolls_to_target(n: int, k: int, target: int) -> int:
    def backtrack(new_n, new_target):
        if new_n == 0:
            return 1 if new_target == 0 else 0

        if (new_n, new_target) in memo:
            return memo[(new_n, new_target)]

        result = 0
        for i in range(1, k + 1):
            result = (result + backtrack(new_n - 1, new_target - i)) % mod

        memo[(new_n, new_target)] = result
        return memo[(new_n, new_target)]

    mod = 10 ** 9 + 7
    memo = {}
    return backtrack(n, target)


ic(num_rolls_to_target(2, 6, 7))
