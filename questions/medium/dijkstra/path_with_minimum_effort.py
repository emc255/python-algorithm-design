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
import heapq

from icecream import ic


def minimum_effort_path(heights: list) -> int:
    rows, cols = len(heights), len(heights[0])
    # Directions for moving up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Priority queue, starting with (effort, x, y)
    pq = [(0, 0, 0)]  # (effort, row, col)
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0

    while pq:
        effort, x, y = heapq.heappop(pq)

        # If we reached the bottom-right corner, return the effort
        if x == rows - 1 and y == cols - 1:
            return effort

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                # Calculate the effort to move to the next cell
                next_effort = max(effort, abs(heights[nx][ny] - heights[x][y]))

                # If this path offers a smaller effort, update and push to pq
                if next_effort < efforts[nx][ny]:
                    efforts[nx][ny] = next_effort
                    heapq.heappush(pq, (next_effort, nx, ny))

    return 0  # This will never be reached as there's always a valid path.


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
