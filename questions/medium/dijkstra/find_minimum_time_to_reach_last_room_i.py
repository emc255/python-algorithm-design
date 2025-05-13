"""
3341. Find Minimum Time to Reach Last Room I

There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m,
where moveTime[i][j] represents the minimum time in seconds
when you can start moving to that room. You start from
the room (0, 0) at time t = 0 and can move to an adjacent room.
Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

Example 1:
Input: move_time = [[0,4],[4,4]]
Output: 6
Explanation:
The minimum time required is 6 seconds.
At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.

Example 2:
Input: move_time = [[0,0,0],[0,0,0]]
Output: 3
Explanation:
The minimum time required is 3 seconds.
At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.

Example 3:
Input: move_time = [[0,1],[1,2]]
Output: 3

Constraints:
2 <= n == moveTime.length <= 50
2 <= m == moveTime[i].length <= 50
0 <= moveTime[i][j] <= 109

"""
import heapq

from icecream import ic


def minimum_time_to_reach(move_time: list[list[int]]) -> int:
    n, m = len(move_time), len(move_time[0])
    d = [[float("inf")] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # (distance, x, y)
    heap = [(0, 0, 0)]
    d[0][0] = 0

    while heap:
        dis, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # You must wait until moveTime[nx][ny] is allowed, then +1 second to move
                next_time = max(dis, move_time[nx][ny]) + 1
                if next_time < d[nx][ny]:
                    d[nx][ny] = next_time
                    heapq.heappush(heap, (next_time, nx, ny))

    return d[n - 1][m - 1]


ic(minimum_time_to_reach(move_time=[[0, 4], [4, 4]]))
ic(minimum_time_to_reach(move_time=[[0, 0, 0], [0, 0, 0]]))
