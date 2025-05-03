"""
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, tops[i] and bottoms[i] represent the
top and bottom halves of the ith domino. (A domino is a tile
with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i]
swap values.

Return the minimum number of rotations so that all the values
in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Example 1:
Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by tops and bottoms:
before we do any rotations. If we rotate the second and fourth dominoes,
we can make every value in the top row equal to 2, as indicated by
the second figure.

Example 2:
Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make
one row of values equal.

Constraints:
2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6

"""
from collections import defaultdict

from icecream import ic


def minimum_domino_rotations(tops: list[int], bottoms: list[int]) -> int:
    N = max(len(tops), len(bottoms))
    t = defaultdict(set)
    b = defaultdict(set)
    combine = defaultdict(set)
    num = set()
    for i, v in enumerate(tops):
        combine[v].add(i)
        t[v].add(i)

    for i, v in enumerate(bottoms):
        combine[v].add(i)
        b[v].add(i)

    for k, v in combine.items():
        if len(v) >= N:
            num.add(k)

    if len(num) >= 1:
        m = float('inf')

        for n in num:
            common = t[n].intersection(b[n])

            m = min(m, min(len(t[n]) - len(common), len(b[n]) - len(common)))
        return m
    return -1


def minimum_domino_rotations_v2(self, tops, bottoms):
    def check(x):
        rotations_top = rotations_bottom = 0
        for i in range(len(tops)):
            if tops[i] != x and bottoms[i] != x:
                return -1
            elif tops[i] != x:
                rotations_top += 1
            elif bottoms[i] != x:
                rotations_bottom += 1
        return min(rotations_top, rotations_bottom)

    res = check(tops[0])
    if res != -1:
        return res
    return check(bottoms[0])


ic(minimum_domino_rotations(tops=[3, 3, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]))
ic(minimum_domino_rotations(tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]))
ic(minimum_domino_rotations(tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]))
