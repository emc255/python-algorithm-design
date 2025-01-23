"""
Count Servers that Communicate

You are given a map of a server center, represented as a m * n integer matrix grid,
where 1 means that on that cell there is a server and 0 means that it is no server.
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation:
No servers can communicate with others.

Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation:
All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation:
The two servers in the first row can communicate with each other.
The two servers in the third column can communicate with each other.
The server at right bottom corner can't communicate with any other server.

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1

"""
from icecream import ic


def count_servers(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # Step 1: Count servers in each row and column
    row_counts = [0] * m
    col_counts = [0] * n

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                row_counts[r] += 1
                col_counts[c] += 1

    # Step 2: Count servers that can communicate
    result = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and (row_counts[r] > 1 or col_counts[c] > 1):
                result += 1

    return result


ic(count_servers(grid=[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
ic(count_servers(grid=[[1, 0], [1, 1]]))
