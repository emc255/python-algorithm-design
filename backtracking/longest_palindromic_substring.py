"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def longest_palindromic_substring(s: str) -> str:
    def backtracking(s: str, left_index: int, right_index: int, string_found) -> str:
        while left_index >= 0 and right_index <= len(s) - 1 and s[left_index] == s[right_index]:
            string_found = s[left_index:right_index + 1]
            left_index -= 1
            right_index += 1

        return string_found

    result = ""

    for i in range(len(s)):
        word_odd = backtracking(s, i, i, "")
        word_even = backtracking(s, i, i + 1, "")

        if len(word_odd) > len(result):
            result = word_odd

        if len(word_even) > len(result):
            result = word_even

    return result


#
# def backtracking(s: str, left_index: int, right_index: int, string_found):
#     while left_index >= 0 and right_index <= len(s) - 1 and s[left_index] == s[right_index]:
#         string_found = s[left_index:right_index + 1]
#         left_index -= 1
#         right_index += 1
#
#     return string_found


print(longest_palindromic_substring("badad"))
print(longest_palindromic_substring("cbbd"))
