"""
861. Score After Flipping Matrix

You are given an m x n binary matrix grid.

A move consists of choosing any row or column
and toggling each value in that row or column
(i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number,
and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:
Input: grid = [[0]]
Output: 1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.

"""
import collections

from icecream import ic


def matrix_score(grid: list[list[int]]) -> int:
    score = 0
    R = len(grid)
    C = len(grid[0])

    for r in range(R):
        if grid[r][0] == 0:
            for c in range(C):
                grid[r][c] = 0 if grid[r][c] else 1

    for c in range(C):
        ones = 0
        for r in range(R):
            ones += grid[r][c]
        if ones < R - ones:
            for r in range(R):
                grid[r][c] = 0 if grid[r][c] else 1

    for r in range(R):
        for c in range(C):
            if grid[r][c]:
                score += 2 ** (C - c - 1)
    return score


def matrix_score_v2(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        if grid[r][0] == 0:
            for c in range(cols):
                if grid[r][c] == 0:
                    grid[r][c] = 1
                else:
                    grid[r][c] = 0

    counts = collections.defaultdict(int)
    for c in range(1, cols):
        for r in range(rows):
            if grid[r][c] == 0:
                counts[c] += 1

    res = rows * (2 ** (cols - 1))
    for c in range(1, cols):
        res += max(counts[c], rows - counts[c]) * 2 ** (cols - c - 1)

    return res


ic(matrix_score([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
