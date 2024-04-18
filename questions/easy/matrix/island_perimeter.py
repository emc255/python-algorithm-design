"""
Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1
represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes",
meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1.
The grid is rectangular,
width and height don't exceed 100. Determine the perimeter of the island.


Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.

"""
from icecream import ic


def island_perimeter(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    perimeter = 0

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return 1  # Boundary or water cell, count as perimeter

        if grid[r][c] == -1:  # Visited cell
            return 0

        grid[r][c] = -1  # Mark cell as visited

        # Explore neighboring cells
        perimeter = 0
        perimeter += dfs(r + 1, c)
        perimeter += dfs(r - 1, c)
        perimeter += dfs(r, c + 1)
        perimeter += dfs(r, c - 1)
        return perimeter

    # Find the first land cell and start DFS
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                perimeter += dfs(i, j)
                return perimeter

    return perimeter


def island_perimeter_v2(grid: list[list[int]]) -> int:
    row = len(grid)
    col = len(grid[0])
    ans = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                ans += 4
                if i > 0 and grid[i - 1][j] == 1:
                    ans -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    ans -= 2

    return ans


ic(island_perimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
