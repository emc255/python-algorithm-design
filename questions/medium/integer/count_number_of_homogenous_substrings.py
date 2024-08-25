"""
1759. Count Number of Homogenous Substrings

Given a string s, return the number of homogenous substrings of s.
 Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

Example 2:
Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".

Example 3:
Input: s = "zzzzz"
Output: 15

Constraints:
1 <= s.length <= 105
s consists of lowercase letters.

"""
from itertools import groupby

from icecream import ic


def count_homogenous(s: str) -> int:
    """
     1234567 = 1
        123456 234567 = 2
        12345 23456 34567 = 3
        1234 2345 3456 4567 = 4
        123 234 345 456 567 = 5
        12 23 34 45 56 67 = 6

        12345 = 1
        1234 2345 = 2
        123 234 345 = 3
        12 23 34 45 = 4

        123456 = 1
        12345 23456 = 2
        1234 2345 3456 = 3
        123 234 345 456 = 4
        12 23 34 45 56 = 5

        You can use the formula for the sum of an arithmetic series:
        Sum = (n/2) * (first number + last number)
    """
    result = 0
    for k, group in groupby(s):
        n = len(list(group))
        if n == 1:
            result += n
        else:
            result += int((n / 2) * (1 + n))
    return result % (10 ** 9 + 7)


def count_homogenous_v2(s: str) -> int:
    result = 0
    mod_value = 10 ** 9 + 7
    n = 1  # Initialize n with 1 to account for the last character

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            n += 1
        else:
            result = (result + (n * (n + 1) // 2)) % mod_value
            n = 1

    result = (result + (n * (n + 1) // 2)) % mod_value
    return result


def count_homogenous_v3(self, s: str) -> int:
    ans = 0
    for k, g in groupby(s):
        temp = len(list(g))
        ans = (ans + temp * (temp + 1) // 2) % (10 ** 9 + 7)

    return ans


ic(count_homogenous("abbcccaa"))
ic(count_homogenous("zzzzz"))
