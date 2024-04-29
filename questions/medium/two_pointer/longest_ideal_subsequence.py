"""
Longest Ideal Subsequence

You are given a string s consisting of lowercase letters and an integer k.
We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every
two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string
by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic.
For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

Example 1:
Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd".
The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f'
have a difference of 3 in alphabet order.

Example 2:
Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd".
The length of this string is 4, so 4 is returned.

Constraints:
1 <= s.length <= 105
0 <= k <= 25
s consists of lowercase English letters.

"""

from icecream import ic


def longest_ideal_string(s: str, k: int) -> int:
    def dp(i, prev):
        if i == len(s):
            return 0

        if (i, prev) in memo:
            return memo[(i, prev)]

        result = dp(i + 1, prev)  # skip s[i]

        if prev == "" or abs(ord(s[i]) - ord(prev)) <= k:
            result = max(result, 1 + dp(i + 1, s[i]))  # include
        memo[(i, prev)] = result
        return result

    memo = {}
    return dp(0, "")


def longest_ideal_string_v2(s: str, k: int) -> int:
    dp = [0] * 26
    for c in s:
        current = ord(c) - ord('a')
        longest = 1
        for previous in range(26):
            if abs(current - previous) <= k:
                longest = max(longest, 1 + dp[previous])
        dp[current] = max(dp[current], longest)

    return max(dp)


ic(longest_ideal_string_v2("acfgbd", 2))
ic(longest_ideal_string("abcd", 3))
ic(longest_ideal_string("pvjcci", 3))
