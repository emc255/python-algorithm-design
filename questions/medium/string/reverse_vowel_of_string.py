"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u',
and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

"""
from icecream import ic


def reverse_vowels(s: str) -> str:
    vowels = "AEIOUaeiou"
    result = list(s)
    l, r = 0, len(s) - 1

    while l < r:
        if result[l] in vowels and result[r] in vowels:
            result[l], result[r] = result[r], result[l]
            l += 1
            r -= 1

        if result[l] not in vowels:
            l += 1
        if result[r] not in vowels:
            r -= 1

    return "".join(result)


#
# ic(reverse_vowels("hello"))
ic(reverse_vowels("leetcode"))
