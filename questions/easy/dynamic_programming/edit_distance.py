"""
72. Edit Distance

Given two strings word1 and word2, return the minimum number
of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

"""
from icecream import ic


def minimum_distance(word1: str, word2: str) -> int:
    row, col = len(word1), len(word2)
    dp = [[0] * (col + 1) for _ in range(row + 1)]

    # Base cases
    for i in range(row + 1):
        dp[i][0] = i  # delete all characters from word1
    for j in range(col + 1):
        dp[0][j] = j  # insert all characters into word1

    # DP computation
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # delete
                    dp[i][j - 1] + 1,  # insert
                    dp[i - 1][j - 1] + 1  # replace
                )

    return dp[row][col]


ic(minimum_distance(word1="horse", word2="ros"))
