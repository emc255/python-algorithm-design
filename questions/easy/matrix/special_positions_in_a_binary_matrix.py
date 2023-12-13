"""
1582. Special Positions in a Binary Matrix

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1
and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1
and all other elements in row 1 and column 2 are 0.

Example 2:
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.

"""
from icecream import ic

"""

[[0,0,0,1],
[1,0,0,0],
[0,1,1,0],
[0,0,0,0]]
"""


def num_special(mat: list) -> int:
    result = 0
    m = len(mat)
    n = len(mat[0])
    row_count = [0] * m
    column_count = [0] * n

    for row in range(m):
        for col in range(n):
            if mat[row][col] == 1:
                row_count[row] += 1
                column_count[col] += 1

    for row in range(m):
        for col in range(n):
            if mat[row][col] == 1:
                if row_count[row] == 1 and column_count[col] == 1:
                    result += 1

    return result


def num_special_v2(mat: list) -> int:
    m = len(mat)
    n = len(mat[0])
    cols = [0] * n
    for i in range(n):
        col = 0
        for j in range(m):
            if mat[j][i]:
                col += 1
                if col > 1:
                    col = 0
                    break
        cols[i] = col
    ans = 0

    for i in range(m):
        isum = sum(mat[i])
        if isum == 1:
            j = mat[i].index(1)
            # for j in range(n):
            if mat[i][j] and cols[j]:
                ans += 1
                # break

    return ans


ic(num_special([[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
ic(num_special([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
ic(num_special([[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]))
ic(num_special([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
