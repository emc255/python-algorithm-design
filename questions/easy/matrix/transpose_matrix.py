"""
867. Transpose Matrix

Given a 2D integer array matrix,
return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal,
switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109

"""
from icecream import ic


def transpose(matrix: list) -> list:
    transpose_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose_matrix[j][i] = matrix[i][j]

    return transpose_matrix


def transpose_v2(matrix: list) -> list:
    return [list(row) for row in zip(*matrix)]


ic(transpose([[1, 2, 3], [4, 5, 6]]))
ic(transpose([[3]]))

ic(transpose_v2([[1, 2, 3], [4, 5, 6]]))
