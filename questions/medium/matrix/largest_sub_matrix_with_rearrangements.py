"""
1727. Largest Submatrix With Rearrangements

ou are given a binary matrix matrix of size m x n,
and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix
where every element of the submatrix is 1 after reordering the columns optimally.

Example 1:
Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.

Example 2:
Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.

Example 3:
Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns,
and there is no way to make a submatrix of 1s larger than an area of 2.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m * n <= 105
matrix[i][j] is either 0 or 1.

"""
from icecream import ic


def largest_sub_matrix(matrix: list) -> int:
    result = 0
    R = len(matrix)
    C = len(matrix[0])

    for row in range(R):
        for col in range(C):
            if matrix[row][col] != 0 and row > 0:
                matrix[row][col] += matrix[row - 1][col]

        current_row = sorted(matrix[row], reverse=True)
        ic(current_row)
        for i in range(C):
            result = max(result, current_row[i] * (i + 1))

    return result


ic(largest_sub_matrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
