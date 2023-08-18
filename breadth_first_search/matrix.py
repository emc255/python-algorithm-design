"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

"""
from collections import deque


def update_matrix(mat: list) -> list:
    if not mat or not mat[0]:
        return []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    m = len(mat)
    n = len(mat[0])
    max_value = m * n

    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                queue.append((r, c))
            else:
                mat[r][c] = max_value

    while queue:
        row, column = queue.popleft()
        for dr, dc in directions:
            r = row + dr
            c = column + dc
            if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][column] + 1:
                queue.append((r, c))
                mat[r][c] = mat[row][column] + 1

    return mat


print(update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(update_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
