"""
1347. Minimum Number of Steps to Make Two Strings Anagram

You are given two strings of the same length s and t.
In one step you can choose any character of t
and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains
the same characters with a different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b,
t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t
with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.

Constraints:
1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.

"""
from collections import Counter

from icecream import ic


def min_steps(s: str, t: str) -> int:
    word1 = Counter(s)
    word2 = Counter(t)
    result = 0
    for k, v in word1.items():
        if k in word2:
            temp = word2[k] - v
            if temp < 0:
                result += abs(temp)
        else:
            result += v

    return result


def min_steps_v2(s: str, t: str) -> int:
    counter_s = Counter(s)
    counter_t = Counter(t)

    diff = counter_s - counter_t

    return sum(diff.values())


ic(min_steps("leetcode", "practice"))
