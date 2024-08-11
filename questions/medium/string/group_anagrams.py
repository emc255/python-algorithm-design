"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed
by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""
from collections import Counter

from icecream import ic


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_groups = {}

    for word in strs:
        key = tuple(sorted(word))
        if key in anagram_groups:
            anagram_groups[key].append(word)
        else:
            anagram_groups[key] = [word]

    return list(anagram_groups.values())


def group_anagrams_v2(strs: list[str]) -> list[list[str]]:
    def is_anagrams(s1, s2):
        word1 = Counter(s1)
        word2 = Counter(s2)
        return word1 == word2

    result = [[strs[0]]]

    for i in range(1, len(strs)):
        undecided = True
        for res in result:
            if is_anagrams(res[0], strs[i]):
                res.append(strs[i])
                undecided = False
                break
        if undecided:
            result.append([strs[i]])
    return result


ic(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
