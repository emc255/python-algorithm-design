"""
1624. Largest Substring Between Two Equal Characters

Given a string s,
return the length of the longest substring between two equal characters,
excluding the two characters.
If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

Constraints:
1 <= s.length <= 300
s contains only lowercase English letters.

"""
from icecream import ic


def max_length_between_equal_characters(s: str) -> int:
    seen = {}
    counter = -1
    n = len(s)
    for i in range(n):
        if s[i] in seen:
            counter = max(counter, i - seen[s[i]] - 1)
        else:
            seen[s[i]] = i

    return counter


ic(max_length_between_equal_characters("adddcabca"))
ic(max_length_between_equal_characters("mgntdygtxrvxjnwksqhxuxtrv"))
