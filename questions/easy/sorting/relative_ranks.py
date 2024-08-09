"""
506. Relative Ranks

You are given an integer array score of size n,
where score[i] is the score of the ith athlete in a competition.
All the scores are guaranteed to be unique.

The athletes are placed based on their scores,
where the 1st place athlete has the highest score,
the 2nd place athlete has the 2nd highest score, and so on.
The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete,
their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

Constraints:
n == score.length
1 <= n <= 104
0 <= score[i] <= 106
All the values in score are unique.

"""
from collections import defaultdict

from icecream import ic


def find_relative_ranks(score: list[int]) -> list[str]:
    result = ["o" for i in range(len(score))]
    sorted_score = sorted(score, reverse=True)

    for i, s in enumerate(sorted_score):
        index = score.index(s)
        if i == 0:
            result[index] = "Gold Medal"
        elif i == 1:
            result[index] = "Silver Medal"
        elif i == 2:
            result[index] = "Bronze Medal"
        else:
            result[index] = str(i + 1)

    return result


def find_relative_ranks_v2(score: list[int]) -> list[str]:
    N = len(score)

    # Save the index of each athlete
    score_to_index = defaultdict(int)
    for i in range(N):
        score_to_index[score[i]] = i

    # Sort score in descending order
    score.sort(reverse=True)

    # Assign ranks to athletes
    rank = [" "] * N
    for i in range(N):
        if i == 0:
            rank[score_to_index[score[i]]] = "Gold Medal"
        elif i == 1:
            rank[score_to_index[score[i]]] = "Silver Medal"
        elif i == 2:
            rank[score_to_index[score[i]]] = "Bronze Medal"
        else:
            rank[score_to_index[score[i]]] = str(i + 1)

    return rank


ic(find_relative_ranks([10, 3, 8, 9, 4]))
ic(find_relative_ranks([5, 4, 3, 2, 1]))
