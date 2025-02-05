"""
1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length.
A string swap is an operation where you choose two indices
in a string (not necessarily different) and swap the characters
at these indices.

Return true if it is possible to make both strings equal
by performing at most one string swap on exactly one of
the strings. Otherwise, return false.



Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation:
For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation:
It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation:
The two strings are already equal, so no string swap operation is required.

Constraints:
1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.

"""
from icecream import ic


def are_almost_equal(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    mismatches = []  # Store indices of mismatched characters

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatches.append(i)
            if len(mismatches) > 2:  # More than 2 mismatches means it's impossible
                return False

    # If no mismatches, they are already equal
    if len(mismatches) == 0:
        return True
   
    # If exactly two mismatches, check if swapping makes them equal
    if len(mismatches) == 2:
        i, j = mismatches
        return s1[i] == s2[j] and s1[j] == s2[i]

    return False  # If there is exactly one mismatch, it's impossible to fix with one swap


ic(are_almost_equal(s1="bank", s2="kanb"))
ic(are_almost_equal(s1="aa", s2="bc"))
