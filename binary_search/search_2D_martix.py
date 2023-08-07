"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

"""
import math


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    low = 0
    high = len(matrix[0]) - 1

    while low < len(matrix) and high >= 0:
        if matrix[low][high] == target:
            return True
        elif matrix[low][high] > target:
            high -= 1
        else:
            low += 1

    return False


"""
the divmod() function is used to perform floor division and modulus operation 
simultaneously on two numbers. It takes two arguments, typically the dividend and the divisor, 
and returns a tuple containing two values: the result of the floor division (quotient) 
and the remainder obtained from the modulus operation.
"""


def search_matrix_v2(matrix: list[list[int]], target: int) -> bool:
    if not matrix:
        return False
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        # mid_row, mid_col = divmod(mid, n)
        mid_row = math.floor(mid / n)
        mid_col = mid % n

        if matrix[mid_row][mid_col] == target:
            return True
        elif matrix[mid_row][mid_col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60))
print(search_matrix_v2([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60))
