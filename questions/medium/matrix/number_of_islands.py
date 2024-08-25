"""
200. Number of Islands

Given an m x n 2D binary grid grid which
represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""
from icecream import ic


def number_islands(grid: list[list[str]]) -> int:
    def dfs(row, column):
        # Check if the cell is within the grid and is unvisited
        if row < 0 or row >= m or column < 0 or column >= n or visited[row][column] or grid[row][column] == "0":
            return
        visited[row][column] = True
        # Explore all four directions
        dfs(row + 1, column)
        dfs(row - 1, column)
        dfs(row, column + 1)
        dfs(row, column - 1)

    m = len(grid)
    n = len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    island_count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1" and not visited[r][c]:
                dfs(r, c)
                island_count += 1
    return island_count


ic(number_islands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
