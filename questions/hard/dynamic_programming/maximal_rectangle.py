"""
85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

"""
from icecream import ic


def maximal_rectangle(matrix: list) -> int:
    if not matrix:
        return 0

    def largest_rectangle_area(heights):
        stack = []
        max_area = 0
        i = 0

        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)

        while stack:
            top = stack.pop()
            width = i if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)

        return max_area

    maximum_area = 0
    row_histogram = [0] * len(matrix[0])
  
    for row in matrix:
        for i in range(len(row)):
            if row[i] == '1':
                row_histogram[i] += 1
            else:
                row_histogram[i] = 0
        maximum_area = max(maximum_area, largest_rectangle_area(row_histogram))

    return maximum_area


ic(maximal_rectangle([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]))
