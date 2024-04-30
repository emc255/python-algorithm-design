"""
Number of Wonderful Substrings

A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'),
return the number of wonderful non-empty substrings in word.
If the same substring appears multiple times in word,
then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"

Example 2:
Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"

Example 3:
Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"

"""

from icecream import ic


def wonderful_substrings(word: str) -> int:
    count = 0
    # Iterate through all possible substrings
    for i in range(len(word)):
        for j in range(i, len(word)):
            substring = word[i:j + 1]
            frequency = [0] * 10  # Initialize frequency array for characters 'a' to 'j'

            # Count occurrences of each character in the substring
            for char in substring:
                frequency[ord(char) - ord('a')] += 1

            # Check if at most one character has an odd number of occurrences
            odd_count = sum(1 for freq in frequency if freq % 2 != 0)
            if odd_count <= 1:
                count += 1

    return count


def wonderful_substrings_v2(word: str) -> int:
    count = 0
    prefix_sums = {0: 1}  # Initialize prefix sums with 0 as key and value 1
    mask = 0  # Initialize mask to keep track of character parity

    for char in word:
        index = ord(char) - ord('a')
        mask ^= 1 << index  # Update the mask by toggling the bit corresponding to the character

        # Update the count by adding the current mask value from the prefix sums
        count += prefix_sums.get(mask, 0)

        # Update the prefix sums dictionary
        for i in range(10):
            new_mask = mask ^ (1 << i)
            count += prefix_sums.get(new_mask, 0)

        prefix_sums[mask] = prefix_sums.get(mask, 0) + 1

    return count


def wonderful_substrings_v3(word: str) -> int:
    count = 0
    seen = [0] * 1024
    seen[0] = 1
    bitmask = 0
    for char in word:
        bitmask ^= 1 << (ord(char) - ord('a'))
        count += seen[bitmask]
        for i in range(10):
            count += seen[bitmask ^ (1 << i)]
        seen[bitmask] += 1
    return count


ic(wonderful_substrings_v2("ehaehcjjaafjdceac"))
# ic(wonderful_substrings("aba"))
# ic(wonderful_substrings("aabb"))
