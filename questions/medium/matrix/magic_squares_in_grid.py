"""
840. Magic Squares In Grid

A 3 x 3 magic square is a 3 x 3 grid filled with distinct
numbers from 1 to 9 such that each row, column,
and both diagonals all have the same sum.

Given a row x col grid of integers,
how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain
numbers from 1 to 9, grid may contain numbers up to 15.

Example 1:
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
4 3 8
9 5 1
2 7 6
while this one is not:
3 8 4
5 1 9
7 6 2
In total, there is only one magic square inside the given grid.

Example 2:
Input: grid = [[8]]
Output: 0

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15

"""
from icecream import ic


def num_magic_squares_inside(grid: list[list[int]]) -> int:
    def is_magic_square(r, c):
        seen = [False] * 10
        for i in range(3):
            for j in range(3):
                num = grid[r + i][c + j]
                if num < 1 or num > 9:
                    return False
                if seen[num]:
                    return False
                seen[num] = True
        # Check if diagonal sums are the same
        diagonal1 = grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]
        diagonal2 = grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2]
        if diagonal1 != diagonal2:
            return False
        # Check if all row sums are the same as the diagonal sums

        row1 = grid[r][c] + grid[r][c + 1] + grid[r][c + 2]
        row2 = grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2]
        row3 = grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2]

        if not (row1 == diagonal1 and row2 == diagonal1 and row3 == diagonal1):
            return False

        # Check if all column sums are the same as the diagonal sums
        col1 = grid[r][c] + grid[r + 1][c] + grid[r + 2][c]
        col2 = grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1]
        col3 = grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2]

        if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1):
            return False

        return True

    result = 0
    R, C = len(grid), len(grid[0])
    for current_row in range(R - 2):
        for current_col in range(C - 2):
            if is_magic_square(current_row, current_col):
                result += 1

    return result


ic(num_magic_squares_inside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
ic(num_magic_squares_inside([[10, 3, 5], [1, 6, 11], [7, 9, 2]]))
