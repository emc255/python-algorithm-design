"""
1239. Maximum Length of a Concatenated String with Unique Characters

You are given an array of strings arr.
A string s is formed by the concatenation of a
subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived
from another array by deleting some or no elements
without changing the order of the remaining elements.



Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid
concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.

"""
from icecream import ic


def max_length(arr: list[str]) -> int:
    def dfs(start, path):
        if (start, path) in memo:
            return memo[(start, path)]

        result = len(path) if len(path) == len(set(path)) else 0

        for i in range(start, len(arr)):
            result = max(result, dfs(i + 1, path + arr[i]))

        memo[(start, path)] = result
        return result

    memo = {}  # Memoization dictionary
    return dfs(0, "")


ic(max_length(["cha", "r", "act", "ers"]))
ic(max_length(["abcdefghijklmnopqrstuvwxyz"]))
ic(max_length(["aa", "bb"]))
ic(max_length(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]))
