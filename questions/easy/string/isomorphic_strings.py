"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters. No two characters may map to the same character,
but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""


def is_isomorphic(s: str, t: str) -> bool:
    s_map = {}
    t_map = {}
    for i in range(len(s)):
        c1, c2 = s[i], t[i]

        if (c1 in s_map and s_map[c1] != c2
                or c2 in t_map and t_map[c2] != c1):
            return False

        s_map[c1] = c2
        t_map[c2] = c1

    return True


print(is_isomorphic("egg", "add"))
print(is_isomorphic("paper", "title"))
print(is_isomorphic("Foo", "bar"))
print(is_isomorphic("badc", "baba"))
