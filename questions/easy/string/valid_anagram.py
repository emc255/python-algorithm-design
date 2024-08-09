"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""
from collections import Counter

from icecream import ic


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    for ss in s:
        if ss not in t:
            return False
        else:
            t = t.replace(ss, "", 1)

    return len(t) == 0


def is_anagram_v2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    for ss in set(s):
        if s.count(ss) != t.count(ss):
            return False

    return True


def is_anagram_v3(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


ic(is_anagram("anagram", "nagaram"))
ic(is_anagram_v2("anagram", "nagaram"))
ic(is_anagram_v3("anagram", "nagaram"))
