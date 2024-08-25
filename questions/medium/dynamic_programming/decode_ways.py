"""
91. Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message,
all the digits must be grouped then mapped back into letters
using the reverse of the mapping above (there may be multiple ways).
For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot
be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits,
return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

"""
from icecream import ic


def numbers_decoding(s: str) -> int:
    decodes = {
        '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E',
        '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J',
        '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O',
        '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T',
        '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y',
        '26': 'Z'
    }

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string has one way to decode
    for i in range(1, n + 1):
        # Single digit
        if s[i - 1] in decodes:
            dp[i] += dp[i - 1]

        # Two digits
        if i > 1 and s[i - 2:i] in decodes:
            dp[i] += dp[i - 2]

    return dp[n]


ic(numbers_decoding("226"))
ic(numbers_decoding("06"))
