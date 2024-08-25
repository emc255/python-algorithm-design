"""
131. Palindrome Partitioning

Given a string s, partition s such that every
substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.


Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]


Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.

"""
from icecream import ic


def partition(s: str) -> list[list[str]]:
    def is_palindrome(substring):
        return substring == substring[::-1]

    def dp(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            current_substring = s[start:end]
            if is_palindrome(current_substring):
                path.append(current_substring)
                dp(end, path)
                path.pop()

    result = []
    dp(0, [])
    return result


ic(partition("aab"))
