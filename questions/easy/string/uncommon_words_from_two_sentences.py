"""
884. Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each
word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences,
and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words.
You may return the answer in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Explanation:
The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]

Constraints:
1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.

"""
from collections import Counter

from icecream import ic


def uncommon_from_sentences(s1: str, s2: str) -> list[str]:
    s1_arr = s1.split(" ")
    s2_arr = s2.split(" ")

    # Count occurrences of words in both sentences
    count = Counter(s1_arr) + Counter(s2_arr)

    # Return words that appear exactly once across both sentences
    return [word for word in count if count[word] == 1]


ic(uncommon_from_sentences("this apple is sweet", "this apple is sour"))
