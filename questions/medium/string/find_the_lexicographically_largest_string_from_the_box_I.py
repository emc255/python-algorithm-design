"""
3403. Find the Lexicographically Largest String From the Box I

You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends.
There are multiple rounds in the game, where in each round:

word is split into numFriends non-empty strings,
such that no previous round has had the exact same split.
All the split words are put into a box.

Find the lexicographically largest string from
the box after all the rounds are finished.

Example 1:
Input: word = "dbca", numFriends = 2
Output: "dbc"
Explanation:
All possible splits are:
"d" and "bca".
"db" and "ca".
"dbc" and "a".

Example 2:
Input: word = "gggg", numFriends = 4
Output: "g"
Explanation:
The only possible split is: "g", "g", "g", and "g".

Constraints:
1 <= word.length <= 5 * 103
word consists only of lowercase English letters.
1 <= numFriends <= word.length

"""
from icecream import ic


def answer_string(word: str, num_friends: int) -> str:
    if num_friends == 1:
        return word
    max_substring = ""
    substring_size = len(word) - num_friends + 1
    for i in range(len(word)):
        max_substring = max(max_substring, word[i:i + substring_size])
    return max_substring


def answer_string_v2(word: str, num_friends: int) -> str:
    if num_friends == 1:
        return word

    window = len(word) - num_friends + 1
    res = -1
    max_score = ""
    for idx in range(len(word)):
        if word[idx: idx + window] > max_score:
            max_score = word[idx: idx + window]
            res = idx
    return word[res: res + window]


ic(answer_string(word="bif", num_friends=2))
ic(answer_string(word="dbca", num_friends=2))
