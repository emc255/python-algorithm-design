"""
Out of Boundary Paths

There is an m x n grid with a ball.
The ball is initially at the position [startRow, startColumn].
You are allowed to move the ball to one of
the four adjacent cells in
the grid (possibly out of the grid crossing the grid boundary).
You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn,
return the number of paths to move the ball out of
the grid boundary. Since the answer can be very large,
return it modulo 109 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n

"""

from icecream import ic


def find_paths(m: int, n: int, max_move: int, start_row: int, start_column: int) -> int:
    def dfs(r, c, moves):
        if (r, c, moves) in memo:
            return memo[(r, c, moves)]

        if r < 0 or r == m or c < 0 or c == n:
            return 1
        if moves == 0:
            return 0
        memo[(r, c, moves)] = (
                                      (dfs(r + 1, c, moves - 1) + dfs(r - 1, c, moves - 1)) % mod
                                      + (dfs(r, c + 1, moves - 1) + dfs(r, c - 1, moves - 1)) % mod
                              ) % mod
        return memo[(r, c, moves)]

    mod = 10 ** 9 + 7
    memo = {}
    return dfs(start_row, start_column, max_move)


ic(find_paths(2, 2, 2, 0, 0))
