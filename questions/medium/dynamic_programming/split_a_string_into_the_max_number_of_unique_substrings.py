"""
1593. Split a String Into the Max Number of Unique Substrings

Given a string s,
return the maximum number of unique substrings
that the given string can be split into.

You can split string s into any list of non-empty substrings,
where the concatenation of the substrings forms the original string.
However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "ababccc"
Output: 5
Explanation:
One way to split maximally is ['a', 'b', 'ab', 'c', 'cc'].
Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is
not valid as you have 'a' and 'b' multiple times.

Example 2:
Input: s = "aba"
Output: 2
Explanation:
One way to split maximally is ['a', 'ba'].

Example 3:
Input: s = "aa"
Output: 1
Explanation:
It is impossible to split the string any further.

Constraints:
1 <= s.length <= 16
s contains only lower case English letters.

"""
from icecream import ic


def max_unique_split(s: str) -> int:
    def backtrack(start_index, unique_substrings):
        if start_index == len(s):
            return 0

        max_splits = 0

        for end_index in range(start_index, len(s)):
            substring = s[start_index:end_index + 1]
            if substring in unique_substrings:
                continue

            unique_substrings.add(substring)
            max_splits = max(max_splits, 1 + backtrack(end_index + 1, unique_substrings))
            unique_substrings.remove(substring)

        return max_splits

    return backtrack(0, set())


ic(max_unique_split(s="ababccc"))
