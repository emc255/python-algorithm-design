"""
2707. Extra Characters in a String

You are given a 0-indexed string s and a dictionary of
words dictionary. You have to break s into one or more
non-overlapping substrings such that each substring is
present in dictionary. There may be some extra characters
in s which are not present in any of the substrings.

Return the minimum number of extra characters left
over if you break up s optimally.

Example 1:
Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation:
We can break s in two substrings: "leet" from index 0 to 3
and "code" from index 5 to 8. There is only 1
unused character (at index 4), so we return 1.

Example 2:
Input:s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation:
We can break s in two substrings: "hello" from index 3 to 7
and "world" from index 8 to 12. The characters at indices 0, 1, 2
are not used in any substring and thus are considered as
extra characters. Hence, we return 3.

Constraints:
1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words

"""

from icecream import ic


def minimum_extra_char(s: str, dictionary: list[str]) -> int:
    def dp(idx):
        # Base case: If we reach the end of the string, no extra characters
        if idx == N:
            return 0

        # Check if we've already computed this state
        if idx in memo:
            return memo[idx]

        # Option 1: Treat the current character as an extra character
        result = dp(idx + 1) + 1

        # Option 2: Try to match each word in the dictionary starting at idx
        for word in dict_set:
            word_len = len(word)
            if idx + word_len <= N and s[idx:idx + word_len] == word:
                result = min(result, dp(idx + word_len))

        # Store the result in memo and return
        memo[idx] = result
        return result

    N = len(s)
    dict_set = set(dictionary)  # Convert dictionary to set for O(1) lookup
    memo = {}

    return dp(0)


ic(minimum_extra_char(s="leetscode", dictionary=["leet", "code", "leetcode"]))
