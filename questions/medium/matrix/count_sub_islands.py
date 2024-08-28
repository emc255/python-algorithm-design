"""
1905. Count Sub Islands

You are given two m x n binary matrices grid1 and grid2 containing
only 0's (representing water) and 1's (representing land). An island is a group of 1's
connected 4-directionally (horizontal or vertical). Any cells outside of the grid are
considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1
that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Example 1:
1 1 1 0 0       1 1 1 0 0
0 1 1 1 1       0 0 1 1 1
0 0 0 0 0       0 1 0 0 0
1 0 0 0 0       1 0 1 1 0
1 1 0 1 1       0 1 0 1 0
Input:
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and
the grid on the right is grid2. The 1s colored red in grid2 are
those considered to be part of a sub-island. There are three sub-islands.

Example 2:
1 0 1 0 1       0 0 0 0 0
1 1 1 1 1       1 1 1 1 1
0 0 0 0 0       0 1 0 1 0
1 1 1 1 1       0 1 0 1 0
1 0 1 0 1       1 0 0 0 1
Input:
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2
Explanation: In the picture above, the grid on the left is grid1 and
the grid on the right is grid2. The 1s colored red in grid2 are those
considered to be part of a sub-island. There are two sub-islands.


Constraints:
m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.

"""

from icecream import ic


def count_sub_islands(grid1: list[list[int]], grid2: list[list[int]]) -> int:
    def dfs(row, col):
        if row < 0 or col < 0 or row >= R or col >= C or grid2[row][col] == 0 or (row, col) in visited:
            return True

        visited.add((row, col))
        is_sub_island = True
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        if grid1[row][col] == 0:
            is_sub_island = False

        for dr, dc in directions:
            is_sub_island = dfs(row + dr, col + dc) and is_sub_island

        return is_sub_island

    R = len(grid1)
    C = len(grid1[0])
    result = 0
    visited = set()

    for r in range(R):
        for c in range(C):
            if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                result += 1

    return result


ic(count_sub_islands([[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
                     [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]))
