"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it
and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.

"""
from collections import Counter

from icecream import ic


def first_uniq_char(s: str) -> int:
    result = -1

    letters = Counter(s)
    for k, v in letters.items():
        if v == 1:
            for i in range(len(s)):
                if k == s[i]:
                    if result == -1:
                        result = i
                    else:
                        result = min(result, i)
    return result


ic(first_uniq_char("leetcode"))
ic(first_uniq_char("loveleetcode"))
ic(first_uniq_char("aabb"))
