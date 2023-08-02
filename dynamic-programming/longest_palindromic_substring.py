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


def longest_palindrome(s: str) -> str:
    result = ""
    for i in range(len(s)):
        substring_odd = check_palindrome(s, i, i)
        substring_even = check_palindrome(s, i, i + 1)

        if len(substring_odd) > len(result):
            result = substring_odd
        if len(substring_even) > len(result):
            result = substring_even

    return result


def check_palindrome(s: str, left_index: int, right_index: int) -> str:
    while left_index > 0 and right_index < len(s) and s[left_index] == s[right_index]:
        left_index -= 1
        right_index += 1

    return s[left_index + 1:right_index].replace(" ", "")


def find_palindrome(s: str) -> list:
    result = []
    for i in range(len(s)):
        substring_odd = check_palindrome(s, i, i)
        substring_even = check_palindrome(s, i, i + 1)

        if len(substring_odd) > 1:
            result.append(substring_odd)
        if len(substring_even) > 1:
            result.append(substring_even)

    return result


print(longest_palindrome("cbbd"))
print(find_palindrome("Madam, nurses run radar, kayak, and level in a civic racecar event."))
print(check_palindrome("aabvvbcd", 3, 4))
