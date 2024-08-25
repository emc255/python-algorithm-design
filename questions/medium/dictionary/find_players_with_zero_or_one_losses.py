"""
2225. Find Players With Zero or One Losses

You are given an integer array matches where matches[i] = [winneri, loseri]
indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:
You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Example 2:
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

Constraints:
1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.

"""
import collections
from collections import defaultdict

from icecream import ic


def find_winners(matches: list[list[int]]) -> list[list[int]]:
    players = set()
    losses = collections.Counter()
    result = [[], []]
    for winner, loser in matches:
        players.add(winner)
        players.add(loser)
        losses[loser] += 1

    for player in sorted(players):
        ic(losses[player])
        if losses[player] == 0:
            result[0].append(player)
        elif losses[player] == 1:
            result[1].append(player)

    return result


def find_winners_v2(matches: list[list[int]]) -> list[list[int]]:
    winners = defaultdict(int)
    losers = defaultdict(int)

    result = [[], []]
    for match in matches:
        winners[match[0]] += 1
        losers[match[1]] += 1
    for k, v in winners.items():
        if k in losers:
            if losers[k] == 1:
                result[1].append(k)
        else:
            result[0].append(k)

    for k, v in losers.items():
        if v == 1 and k not in result[1]:
            result[1].append(k)

    result[0].sort()
    result[1].sort()
    return result


ic(find_winners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
# ic(find_winners([[2, 3], [1, 3], [5, 4], [6, 4]]))
