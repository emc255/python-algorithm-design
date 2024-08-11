"""
2038. Remove Colored Pieces if Both Neighbors are the Same Color

There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'.
You are given a string colors of length n where colors[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line.
In this game, Alice moves first.

Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'.
She is not allowed to remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'.
He is not allowed to remove pieces that are colored 'A'.
Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

Example 1:
Input: colors = "AAABABB"
Output: true
Explanation:
AAABABB -> AABABB
Alice moves first.
She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.

Now it's Bob's turn.
Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
Thus, Alice wins, so return true.

Example 2:
Input: colors = "AA"
Output: false
Explanation:
Alice has her turn first.
There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
Thus, Bob wins, so return false.

Example 3:
Input: colors = "ABBBBBBBAAA"
Output: false
Explanation:
ABBBBBBBAAA -> ABBBBBBBAA
Alice moves first.
Her only option is to remove the second to last 'A' from the right.

ABBBBBBBAA -> ABBBBBBAA
Next is Bob's turn.
He has many options for which 'B' piece to remove. He can pick any.

On Alice's second turn, she has no more pieces that she can remove.
Thus, Bob wins, so return false.


Constraints:
1 <= colors.length <= 105
colors consists of only the letters 'A' and 'B'

"""
from collections import Counter
from itertools import groupby

from icecream import ic


def winner_of_game(colors: str) -> bool:
    i = 0
    a_list = []
    b_list = []

    while i < len(colors) - 2:
        a_index = i
        b_index = i
        while a_index < len(colors) and colors[a_index] == 'A':
            a_index += 1

        while b_index < len(colors) and colors[b_index] == 'B':
            b_index += 1

        if len(colors[i:a_index]) >= 3:
            a_list.append(colors[i:a_index])
            i = a_index - 1
        if len(colors[i:b_index]) >= 3:
            b_list.append(colors[i:b_index])
            i = b_index - 1

        i += 1
    a_total = 0
    b_total = 0
    for a in a_list:
        a_total += len(a) - 2
    for b in b_list:
        b_total += len(b) - 2

    return a_total > b_total


def winner_of_game_v2(colors: str) -> bool:
    c = Counter()

    for x, t in groupby(colors):
        c[x] += max(len(list(t)) - 2, 0)

    if c['A'] > c['B']:
        return True

    return False


ic(winner_of_game("AAABABB"))
ic(winner_of_game("ABBBBBBBAAA"))
ic(winner_of_game("AA"))
ic(winner_of_game("AAAABBBB"))
ic(winner_of_game("BBAAABBABBABB"))

ic(winner_of_game_v2("BBAAABBABBABB"))
ic(winner_of_game_v2("AAABABB"))
