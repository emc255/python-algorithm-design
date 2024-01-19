"""
Minimum Falling Path Sum

Given an n x n array of integers matrix,
return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row
and chooses the element in the next row that is either directly
below or diagonally left/right. Specifically, the next element
from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

"""
import sys

from icecream import ic


def min_falling_path_sum(matrix: list[list[int]]) -> int:
    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]
        if r == m:
            return 0

        if c < 0 or c == n:
            return sys.maxsize

        memo[(r, c)] = matrix[r][c] + min(
            dfs(r + 1, c - 1),
            dfs(r + 1, c),
            dfs(r + 1, c + 1)
        )
        return memo[(r, c)]

    m, n = len(matrix), len(matrix[0])
    memo = {}
    result = sys.maxsize

    for col in range(n):
        result = min(result, dfs(0, col))

    return result


ic(min_falling_path_sum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
