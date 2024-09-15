"""
1371. Find the Longest Substring Containing Vowels in Even Counts

Given the string s,
return the size of the longest substring containing
each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u'
must appear an even number of times.

Example 1:
Input: s = "eleetminicoworoep"
Output: 13
Explanation:
The longest substring is "leetminicowor" which contains two each
of the vowels: e, i and o and zero of the vowels: a and u.

Example 2:
Input: s = "leetcodeisgreat"
Output: 5
Explanation:
The longest substring is "leetc" which contains two e's.

Example 3:
Input: s = "bcbcbc"
Output: 6
Explanation:
In this case, the given string "bcbcbc" is the longest
because all vowels: a, e, i, o and u appear zero times.

Constraints:
1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.

"""
from icecream import ic


def find_the_longest_substring(s: str) -> int:
    # Vowel to bit index mapping
    vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    # Dictionary to store the first occurrence of each bitmask
    bitmask_position = {0: -1}  # Initialize bitmask 0 at index -1 to handle full valid substring
    current_bitmask = 0
    max_length = 0

    for i, char in enumerate(s):
        if char in vowels:
            # Toggle the bit corresponding to the vowel
            current_bitmask ^= (1 << vowels[char])

        if current_bitmask in bitmask_position:
            # Calculate the length of the substring if the bitmask has been seen before
            max_length = max(max_length, i - bitmask_position[current_bitmask])
        else:
            # Store the first occurrence of the bitmask
            bitmask_position[current_bitmask] = i

    return max_length


ic(find_the_longest_substring("leetcodeisgreat"))
