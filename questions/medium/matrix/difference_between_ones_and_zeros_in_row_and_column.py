"""
2482. Difference Between Ones and Zeros in Row and Column

You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.

Example 1:
Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]
[0,1,1],
[1,0,1],
[0,0,1]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2

Example 2:
Input: grid = [[1,1,1],[1,1,1]]
Output: [[5,5,5],[5,5,5]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
grid[i][j] is either 0 or 1.

"""
from icecream import ic

"""
[0,1,1],
[1,0,1],
[0,0,1]
"""


def ones_minus_zeros(grid: list) -> list:
    m, n = len(grid), len(grid[0])
    result = [[0] * n for _ in range(m)]
    rows_zeros = [0 for _ in range(m)]
    rows_ones = [0 for _ in range(m)]
    column_zeroes = [0 for _ in range(n)]
    column_ones = [0 for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                rows_zeros[i] += 1
                column_zeroes[j] += 1
            else:
                rows_ones[i] += 1
                column_ones[j] += 1

    for i in range(m):
        for j in range(n):
            result[i][j] = rows_ones[i] + column_ones[j] - rows_zeros[i] - column_zeroes[j]

    return result


ic(ones_minus_zeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
ic(ones_minus_zeros([[1, 1, 1], [1, 1, 1]]))
