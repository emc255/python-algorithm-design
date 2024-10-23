"""
383. Ransom Note

Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

"""
from collections import Counter

from icecream import ic


def can_construct(ransom_note: str, magazine: str) -> bool:
    ransom_note_count = Counter(ransom_note)
    magazine_counter = Counter(magazine)
    for k, v in ransom_note_count.items():
        if magazine_counter[k] < v:
            return False

    return True


ic(can_construct(ransom_note="a", magazine="b"))
ic(can_construct(ransom_note="aab", magazine="baa"))
