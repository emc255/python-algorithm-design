"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point
in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation:
Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200

"""
from icecream import ic


def minimum_path_sum(grid: list[list[int]]) -> int:
    def path(r, c):
        if (r, c) in memo:
            return memo[r, c]

        if r >= R or c >= C:
            return float('inf')
        
        if r == R - 1 and c == C - 1:
            return grid[r][c]

        down = path(r + 1, c)
        right = path(r, c + 1)
        memo[(r, c)] = grid[r][c] + min(down, right)
        return memo[(r, c)]

    R = len(grid)
    C = len(grid[0])
    memo = {}
    return path(0, 0)


ic(minimum_path_sum(grid=[[1, 2, 3], [4, 5, 6]]))
