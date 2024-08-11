"""
959. Regions Cut By Slashes

An n x n grid is composed of 1 x 1 squares where each 1 x 1
square consists of a '/', '\', or blank space ' '.
These characters divide the square into contiguous regions.

Given the grid, grid represented as a string array,
return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

Example 1:
[ /]
[/ ]
Input: grid = [" /","/ "]
Output: 2

Example 2:
[ /]
[  ]
Input: grid = [" /","  "]
Output: 1

Example 3:
[/\]
[\/]
Input: grid = ["/\\","\\/"]
Output: 5
Explanation:
Recall that because \ characters are escaped,
"\\/" refers to \/, and "/\\" refers to /\.

Constraints:
n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.

"""
from icecream import ic


def region_by_slashes(grid: list[str]) -> int:
    def dfs(row, col):
        if row < 0 or col < 0 or row == R3 or col == C3 or grid3[row][col] != 0 or (row, col) in visited:
            return

        visited.add((row, col))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in directions:
            dfs(row + dr, col + dc)

    R, C = len(grid), len(grid[0])
    R3, C3 = 3 * R, 3 * C
    grid3 = [[0] * C3 for _ in range(R3)]
    visited = set()
    result = 0

    for r in range(R):
        for c in range(C):
            r3, c3 = r * 3, c * 3
            if grid[r][c] == "/":
                grid3[r3][c3 + 2] = 1
                grid3[r3 + 1][c3 + 1] = 1
                grid3[r3 + 2][c3] = 1
            elif grid[r][c] == "\\":  # Fixed the escape sequence
                grid3[r3][c3] = 1
                grid3[r3 + 1][c3 + 1] = 1
                grid3[r3 + 2][c3 + 2] = 1

    for r in range(R3):
        for c in range(C3):
            if grid3[r][c] == 0 and (r, c) not in visited:
                dfs(r, c)
                result += 1

    return result


ic(region_by_slashes(["/\\", "\\/"]))
