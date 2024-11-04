"""
796. Rotate String

Given two strings s and goal, return true if and only
if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character
of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

Constraints:
1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

"""

from icecream import ic


def rotate_string(s: str, goal: str) -> bool:
    for i in range(len(s)):
        suffix = s[:i]
        prefix = s[i:]
        if prefix + suffix == goal:
            return True

    return False


ic(rotate_string(s="abcde", goal="cdeab"))
