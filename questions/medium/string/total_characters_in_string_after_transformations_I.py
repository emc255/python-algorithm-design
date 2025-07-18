"""
3335. Total Characters in String After Transformations I

You are given a string s and an integer t, representing the number of
transformations to perform. In one transformation, every character in s is replaced
according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet.
For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.

Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: s = "abcyy", t = 2
Output: 7
Explanation:
First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:
Input: s = "azbk", t = 1
Output: 5
Explanation:
First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.

Constraints:
1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 105

"""
from icecream import ic


def length_after_transformations(s: str, t: int) -> int:
    MOD = 10 ** 9 + 7

    def count(c: str, steps: int) -> int:
        if steps == 0:
            return 1
        if c == 'z':
            # z -> a + b, and each undergoes (steps - 1) more
            return (count('a', steps - 1) + count('b', steps - 1)) % MOD
        else:
            # c -> next char
            return count(chr(ord(c) + 1), steps - 1)

    total = 0
    for ch in s:
        total = (total + count(ch, t)) % MOD
    return total


def length_after_transformations_v2(s: str, t: int) -> int:
    MOD = 10 ** 9 + 7

    # dp[c] = length of string from character c after current transformation step
    dp = [1] * 26  # base case: t = 0, each char = 1

    for _ in range(t):
        new_dp = [0] * 26
        for i in range(26):
            if i == 25:  # 'z'
                new_dp[i] = (dp[0] + dp[1]) % MOD  # 'z' -> "ab"
            else:
                new_dp[i] = dp[i + 1]  # shift to next character
        dp = new_dp

    # Final answer: sum over dp[ord(c) - ord('a')] for each character in s
    return sum(dp[ord(c) - ord('a')] for c in s) % MOD


ic(length_after_transformations(s="abcyy", t=2))
