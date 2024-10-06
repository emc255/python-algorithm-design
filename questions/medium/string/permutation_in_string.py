"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a
permutation of s1, or false otherwise.

In other words,
return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

"""
from collections import Counter

from icecream import ic


def check_inclusion(s1: str, s2: str) -> bool:
    def permutation(s: str, prefix: str):
        if len(s) == 0:
            pairs.append(prefix)
            return

        for i in range(len(s)):
            permutation(s[:i] + s[i + 1:], prefix + s[i])

    pairs = []
    permutation(s1, "")

    for pair in pairs:
        if pair in s2:
            return True

    return False


def check_inclusion_v2(s1: str, s2: str) -> bool:
    # Lengths of strings
    len_s1, len_s2 = len(s1), len(s2)

    # If s1 is longer than s2, s1 can't be a permutation of any substring in s2
    if len_s1 > len_s2:
        return False

    # Count frequencies of characters in s1
    s1_count = Counter(s1)

    # Initialize the sliding window character count
    window_count = Counter(s2[:len_s1])
    ic(window_count)
    # Compare the initial window with s1
    if s1_count == window_count:
        return True

    # Slide the window across s2
    for i in range(len_s1, len_s2):
        # Add the next character to the window
        window_count[s2[i]] += 1

        # Remove the character that's no longer in the window
        start_char = s2[i - len_s1]
        if window_count[start_char] == 1:
            del window_count[start_char]
        else:
            window_count[start_char] -= 1

        # Check if the current window matches s1_count
        if s1_count == window_count:
            return True

    return False


ic(check_inclusion(s1="ab", s2="eidabooo"))

ic(check_inclusion(s1="ab", s2="eidabooo"))
ic(check_inclusion_v2(s1="ab", s2="eidabooo"))
