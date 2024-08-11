"""
1568. Minimum Number of Days to Disconnect Island

You are given an m x n binary grid grid where 1 represents land
and 0 represents water. An island is a maximal 4-directionally
(horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly
one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1)
into a water cell (0).

Return the minimum number of days to disconnect the grid.

Example 1:
0 1 1 0     0 1 0 0
0 1 1 0 ->  0 0 1 0
0 0 0 0     0 0 0 0
Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
Output: 2
Explanation:
We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water
and get 2 disconnected island.


Example 2:
1 1 ->  0 0
Input: grid = [[1,1]]
Output: 2
Explanation:
Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either 0 or 1.

"""
from icecream import ic


def minimum_days(grid: list[list[int]]) -> int:
    def dfs(row, col, visit):
        if row < 0 or col < 0 or row == R or col == C or grid[row][col] == 0 or (row, col) in visit:
            return
        visit.add((row, col))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dr, dc in directions:
            dfs(row + dr, col + dc, visit)

    def count_island():
        visited = set()
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] and (r, c) not in visited:
                    dfs(r, c, visited)
                    count += 1
        return count

    R, C = len(grid), len(grid[0])

    if count_island() != 1:
        return 0

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                continue

            grid[i][j] = 0
            if count_island() != 1:
                return 1

            grid[i][j] = 1
    return 2


ic(minimum_days([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
ic(minimum_days([[1, 0]]))
