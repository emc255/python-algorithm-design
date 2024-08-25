"""
343. Integer Break

Given an integer n, break it into the sum of k positive integers, where k >= 2,
and maximize the product of those integers.

Return the maximum product you can get.

Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Constraints:
2 <= n <= 58

"""
import operator
from functools import reduce

from icecream import ic


def integer_break(n: int) -> int:
    def find_combinations(target):
        def dfs(remaining, current_combo):
            if remaining == 0:
                result.append(current_combo)
                return
            if remaining < 0 or (current_combo and current_combo[-1] > remaining):
                return
            start = current_combo[-1] if current_combo else 1
            for num in range(start, target):
                dfs(remaining - num, current_combo + [num])

        result = []
        dfs(target, [])
        return result

    combinations = find_combinations(n)

    ans = {}
    for combination in combinations:
        key = reduce(operator.mul, combination, 1)
        if key in ans and len(combination) < len(ans[key]):
            ans[key] = combination
        else:
            ans[key] = combination
    key_list = sorted(list(ans.keys()), reverse=True)

    return ans[key_list[0]]


def integer_break_v2(n: int) -> int:
    def dfs(remainder):
        if remainder in memo:
            return memo[remainder]

        memo[remainder] = 0 if remainder == n else remainder

        for i in range(1, remainder):
            value = dfs(i) * dfs(remainder - i)
            memo[remainder] = max(memo[remainder], value)

        return memo[remainder]

    memo = {1: 1}
    return dfs(n)


def integer_break_v3(n: int) -> int:
    dp = {1: 1}

    for num in range(2, n + 1):
        dp[num] = 0 if num == n else num
        for i in range(1, num):
            value = dp[i] * dp[num - i]
            dp[num] = max(dp[num], value)
    return dp[n]


ic(integer_break_v2(10))

ic(integer_break_v3(44))
