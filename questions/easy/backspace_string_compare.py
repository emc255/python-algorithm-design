"""
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors.
 '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?

"""
from icecream import ic


def backspace_compare(s: str, t: str) -> bool:
    def remove_character(text):
        stack = []
        for c in text:
            if c == '#' and stack:
                stack.pop()
            elif c != '#':
                stack.append(c)
        return stack

    return remove_character(s) == remove_character(t)


ic(backspace_compare("ab#c", "ad#c"))
