"""
2131. Longest Palindrome by Concatenating Two Letter Words

You are given an array of strings words. Each element of words consists
of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from
words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create.
If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.



Example 1:
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation:
One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2
Explanation:
One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

Constraints:
1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.

"""
from collections import Counter

from icecream import ic


def longest_palindrome(words: list[str]) -> int:
    word_count = Counter(words)
    res = 0
    single_center = False

    for word in word_count:
        rev = word[::-1]
        if word != rev and rev in word_count:
            pairs = min(word_count[word], word_count[rev])
            res += pairs * 4
            word_count[word] -= pairs
            word_count[rev] -= pairs

        if word[0] == word[1]:  # self-palindrome words
            count = word_count[word]
            res += (count // 2) * 4
            if count % 2 == 1 and not single_center:
                res += 2
                single_center = True

    return res


ic(longest_palindrome(words=["aa", "ty", "yt", "lc", "cl", "ab"]))
ic(longest_palindrome(words=["cc", "ll", "xx"]))
