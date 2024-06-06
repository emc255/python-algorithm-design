"""
Find Common Characters

Given a string array words, return an array of all characters
that show up in all strings within the words (including duplicates).
You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

"""
from collections import Counter

from icecream import ic


def common_chars(words: list[str]) -> list[str]:
    result = Counter(words[0])

    # Iterate through the rest of the words
    for word in words[1:]:
        # Create a counter for the current word
        current_count = Counter(word)
        ic(current_count)
        # Intersect the result counter with the current word's counter
        result &= current_count

    # Expand the counter to a list of characters
    return list(result.elements())


ic(common_chars(["bella", "label", "roller"]))
ic(common_chars(["cool", "lock", "cook"]))
