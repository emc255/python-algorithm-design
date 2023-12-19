"""
1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
where heights[row][col] represents the height of cell (row, col).
You are situated in the top-left cell, (0, 0),
and you hope to travel to the bottom-right cell,
(rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right,
and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

Constraints:
rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106

"""
from icecream import ic


def minimum_effort_path(heights: list) -> int:
    r, c = len(heights), len(heights[0])

    def dfs(row, column):
        if row > r or column > c:
            return 0
        total = 0

        if row == r - 1:
            return total

        dfs(row + 1, column)

    dfs(0, 0)
    pass


"""
1 2 2
3 8 2
5 3 5



1 2 3
4 5 6
7 8 9
"""
# print(minimum_effort_path([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
ic(minimum_effort_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
