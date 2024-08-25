"""
1289. Minimum Falling Path Sum II

Given an n x n integer matrix grid,
return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element
from each row of grid such that no two elements chosen in adjacent rows are in the same column.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation:
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.

Example 2:
Input: grid = [[7]]
Output: 7

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99

"""
from icecream import ic


def minimum_falling_path_sum(grid: list[list[int]]) -> int:
    def dp(row, col):
        if row == R - 1:
            return grid[row][col]

        if (row, col) in memoize:
            return memoize[(row, col)]

        result = float('inf')

        for c in range(C):
            if c != col:
                result = min(result, grid[row][col] + dp(row + 1, c))

        memoize[(row, col)] = result
        return result

    R = len(grid)
    C = len(grid[0])
    total = float('inf')
    memoize = {}
    for column in range(C):
        total = min(total, dp(0, column))

    return total


def minimum_falling_path_sum_v2(grid: list[list[int]]) -> int:
    N = len(grid)
    dp = grid[0]
    for r in range(1, N):
        next_dp = [float('inf')] * N
        for current_column in range(N):
            for previous_column in range(N):
                if previous_column != current_column:
                    next_dp[current_column] = min(
                        next_dp[current_column], grid[r][current_column] + dp[previous_column]
                    )
        dp = next_dp
    return min(dp)


def minimum_falling_path_sum_v3(grid: list[list[int]]) -> int:
    N = len(grid)
    DP = grid[0]

    for i in range(1, N):
        index1 = DP.index(min(DP))
        index2 = DP.index(min(DP[:index1] + DP[index1 + 1:]))
        for j in range(N):
            if j != index1:
                grid[i][j] += DP[index1]
            else:
                grid[i][j] += DP[index2]
        DP = grid[i]

    return min(DP)


ic(minimum_falling_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
ic(minimum_falling_path_sum_v2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
