"""
Longest Common Subsequence

Given two strings text1 and text2,
return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated
from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

"""
from icecream import ic


def longest_common_subsequence(text1: str, text2: str) -> int:
    min_length_word = text1 if len(text2) > len(text1) else text2
    max_length_word = text2 if len(text2) > len(text1) else text1
    temp_min_word = ""
    for idx in range(len(min_length_word)):
        if min_length_word[idx] in max_length_word:
            temp_min_word += max_length_word[idx]
    ic(temp_min_word)
    count = 0
    for i in range(len(min_length_word)):
        index = i
        j = 0
        temp = 0
        while j < len(max_length_word) and index < len(min_length_word):
            if min_length_word[index] == max_length_word[j]:
                temp += 1
                index += 1
            j += 1
        count = max(count, temp)

    return count


ic(longest_common_subsequence("cabde", "ace"))
ic(longest_common_subsequence("hofubmnylkra", "pqhgxgdofcvmr"))
