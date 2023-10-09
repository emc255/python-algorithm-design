"""
1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

You are given three integers n, m and k.
Consider the following algorithm to find the maximum element of an array of positive integers:

You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.

Return the number of ways to build the array arr under the mentioned conditions.
As the answer may grow large, the answer must be computed modulo 109 + 7.

Example 1:
Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

Example 2:
Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.

Example 3:
Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]

Constraints:
1 <= n <= 50
1 <= m <= 100
0 <= k <= n

"""


def num_of_arrays(n: int, m: int, k: int) -> int:
    mod = 10 ** 9 + 7

    dp = [[0] * (k + 1) for _ in range(m + 1)]
    prefix = [[0] * (k + 1) for _ in range(m + 1)]
    previous_dp = [[0] * (k + 1) for _ in range(m + 1)]
    previous_prefix = [[0] * (k + 1) for _ in range(m + 1)]

    for j in range(1, m + 1):
        previous_dp[j][1] = 1
        previous_prefix[j][1] = j

    for _ in range(2, n + 1):
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        prefix = [[0] * (k + 1) for _ in range(m + 1)]

        for maxNum in range(1, m + 1):
            for cost in range(1, k + 1):
                dp[maxNum][cost] = (maxNum * previous_dp[maxNum][cost]) % mod

                if maxNum > 1 and cost > 1:
                    dp[maxNum][cost] += previous_prefix[maxNum - 1][cost - 1]
                    dp[maxNum][cost] %= mod

                prefix[maxNum][cost] = (prefix[maxNum - 1][cost] + dp[maxNum][cost]) % mod

        previous_dp, previous_prefix = [row[:] for row in dp], [row[:] for row in prefix]

    return prefix[m][k]


print(num_of_arrays(2, 3, 1))
print(num_of_arrays(5, 2, 3))
