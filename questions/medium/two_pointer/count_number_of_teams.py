"""
1395. Count Number of Teams

There are n soldiers standing in a line.
Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:
Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k])
or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions.
(soldiers can be part of multiple teams).

Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4

Constraints:
n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.

"""
from icecream import ic


def number_teams(rating: list[int]) -> int:
    N = len(rating)
    if N < 3:
        return 0

    result = 0

    for i in range(N):
        less_before = greater_before = less_after = greater_after = 0

        for j in range(i):
            if rating[j] < rating[i]:
                less_before += 1
            elif rating[j] > rating[i]:
                greater_before += 1

        for j in range(i + 1, N):
            if rating[j] < rating[i]:
                less_after += 1
            elif rating[j] > rating[i]:
                greater_after += 1

        result += less_before * greater_after + greater_before * less_after

    return result


ic(number_teams([2, 5, 3, 4, 1]))
ic(number_teams([1, 2, 3, 4]))
ic(number_teams([2, 1, 4]))
ic(number_teams([3, 6, 7, 5, 1]))
