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
from icecream import ic


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


def is_isomorphic_v2(s: str, t: str) -> bool:
    s_dict = {}
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]

        # Check if t_char is already mapped to a different s_char
        if t_char in s_dict.values() and s_char not in s_dict:
            return False

        # Check if s_char is already mapped to a different t_char
        if s_char in s_dict and s_dict[s_char] != t_char:
            return False

        # Add the mapping of s_char to t_char
        s_dict[s_char] = t_char

    return True


ic(is_isomorphic("egg", "add"))
ic(is_isomorphic("paper", "title"))
ic(is_isomorphic("Foo", "bar"))
ic(is_isomorphic("badc", "baba"))

ic(is_isomorphic_v2("egg", "add"))
ic(is_isomorphic_v2("paper", "title"))
ic(is_isomorphic_v2("Foo", "bar"))
ic(is_isomorphic_v2("badc", "baba"))
