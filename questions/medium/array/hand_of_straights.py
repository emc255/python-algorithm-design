"""
Hand of Straights

Alice has some number of cards and she wants to rearrange
the cards into groups so that each group is of size groupSize,
and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written
on the ith card and an integer groupSize, return true if
she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Constraints:
1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length

Note: This question is the same as 1296:
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

"""
from collections import Counter

from icecream import ic


def is_straight_hand(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size != 0:
        return False

    card_counts = Counter(hand)
    while card_counts:
        min_card = min(card_counts)
        for card in range(min_card, min_card + group_size):
            if card not in card_counts:
                return False
            card_counts[card] -= 1
            if card_counts[card] == 0:
                del card_counts[card]

    return True


ic(is_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
