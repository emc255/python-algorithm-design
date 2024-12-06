"""
2554. Maximum Number of Integers to Choose From a Range I

You are given an integer array banned and two integers n and maxSum.
You are choosing some number of integers following the below rules:

The chosen integers have to be in the range [1, n].
Each integer can be chosen at most once.
The chosen integers should not be in the array banned.
The sum of the chosen integers should not exceed maxSum.

Return the maximum number of integers you can choose following the mentioned rules.

Example 1:
Input: banned = [1,6,5], n = 5, maxSum = 6
Output: 2
Explanation:
You can choose the integers 2 and 4.
2 and 4 are from the range [1, 5], both did not appear in banned,
and their sum is 6, which did not exceed maxSum.

Example 2:
Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
Output: 0
Explanation:
You cannot choose any integer while following the mentioned conditions.

Example 3:
Input: banned = [11], n = 7, maxSum = 50
Output: 7
Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
They are from the range [1, 7], all did not appear in banned,
and their sum is 28, which did not exceed maxSum.

Constraints:
1 <= banned.length <= 104
1 <= banned[i], n <= 104
1 <= maxSum <= 109

"""
from icecream import ic


def maxCount(banned: list[int], n: int, max_sum: int) -> int:
    result = 0
    s = 0
    banned = set(banned)
    for i in range(n):
        if i + 1 in banned:
            continue
        s += i + 1
        if s > max_sum:
            break
        result += 1
    return result


def max_count_v2(banned: list[int], n: int, max_sum: int) -> int:
    ans = 0
    temp = 0
    banned = set(banned)
    for i in range(1, n + 1):
        if temp >= max_sum or temp + i > max_sum:
            break
        elif i not in banned:
            temp += i
            ans += 1
    return ans


ic(maxCount(banned=[1, 6, 5], n=5, max_sum=6))
ic(maxCount(banned=[1, 2, 3, 4, 5, 6, 7], n=8, max_sum=1))
ic(maxCount(banned=[11], n=7, max_sum=50))
