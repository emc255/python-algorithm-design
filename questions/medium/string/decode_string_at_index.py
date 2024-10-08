"""
880. Decoded String at Index

You are given an encoded string s. To decode the string to a tape,
the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.

Example 1:
Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

Example 2:
Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".

Example 3:
Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".

Constraints:
2 <= s.length <= 100
s consists of lowercase English letters and digits 2 through 9.
s starts with a letter.
1 <= k <= 109
It is guaranteed that k is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 263 letters.

"""
from icecream import ic


def decode_at_index(s: str, k: int) -> str:
    length = 0
    i = 0

    while length < k:
        if s[i].isdigit():
            length *= int(s[i])
        else:
            length += 1
        i += 1

    for j in range(i - 1, -1, -1):
        char = s[j]
        if char.isdigit():
            length //= int(char)
            k %= length
        else:
            if k == 0 or k == length:
                return char
            length -= 1


ic(decode_at_index("leet2code3", 10))
ic(decode_at_index("a2345678999999999999999", 1))
ic(decode_at_index("a23", 6))
