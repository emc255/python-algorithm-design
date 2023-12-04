"""
1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Constraints:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.

"""
from collections import Counter

from icecream import ic


def count_characters(words: list, chars: str) -> int:
    def compare_word(word):
        char_count = Counter(chars)
        ic(char_count)
        for char in word:
            if char_count[char] <= 0:
                return False
            char_count[char] -= 1
        return True

    count = 0

    for w in words:
        if compare_word(w):
            count += len(w)

    return count


ic(count_characters(["cat", "bt", "hat", "tree"], "atach"))
