"""
1897. Redistribute Characters to Make All Strings Equal

You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j,
where words[i] is a non-empty string,
and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal
using any number of operations, and false otherwise.

Example 1:
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

"""
from collections import Counter

from icecream import ic


def make_equal(words: list[str]) -> bool:
    all_words = ''.join(words)
    n = len(words)
    set1 = set(all_words)
    ic(set1)
    for k, v in dict(Counter(all_words)).items():
        if v % n != 0:
            return False
    return True


def make_equal_v2(words: list[str]) -> bool:
    all_words = ''.join(words)
    n = len(words)
    letters = set(all_words)

    for letter in letters:
        if all_words.count(letter) % n != 0:
            return False
    return True


ic(make_equal(["abc", "aabc", "bc"]))
ic(make_equal(["ab", "a"]))
