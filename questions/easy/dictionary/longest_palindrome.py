"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome that can be built with those letters.

Letters are case sensitive,
for example, "Aa" is not considered a palindrome.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.


Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.

"""
from collections import Counter

from icecream import ic


def longest_palindrome(s: str) -> int:
    result = 0
    single = False
    letters = Counter(s)

    for v in letters.values():
        if v % 2 == 0:
            result += v
        else:
            result += v - 1
            single = True

    if single:
        result += 1

    return result


ic(longest_palindrome("abccccdd"))
ic(longest_palindrome("ab"))
ic(longest_palindrome("bananas"))
ic(longest_palindrome("ababababa"))
