"""
1857. Largest Color Value in a Directed Graph

There is a directed graph of n colored nodes
and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i]
is a lowercase English letter representing the color
of the ith node in this graph (0-indexed). You are also
given a 2D array edges where edges[j] = [aj, bj] indicates
that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence
of nodes x1 -> x2 -> x3 -> ... -> xk such that there is
a directed edge from xi to xi+1 for every 1 <= i < k.
The color value of the path is the number of nodes
that are colored the most frequently occurring color
along that path.

Return the largest color value of any valid path
in the given graph, or -1 if the graph contains a cycle.

Example 1:
Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation:
The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

Example 2:
Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation:
There is a cycle from 0 to 0.

Constraints:
n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n

"""
from collections import defaultdict, deque

from icecream import ic


def largest_path_value(colors: str, edges: list[list[int]]) -> int:
    n = len(colors)
    graph = defaultdict(list)
    indegree = [0] * n

    # Build graph
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Initialize dp table
    dp = [[0] * 26 for _ in range(n)]
    for i in range(n):
        dp[i][ord(colors[i]) - ord('a')] = 1
    ic(dp)
    # Kahn's algorithm
    queue = deque([i for i in range(n) if indegree[i] == 0])
    visited = 0
    max_color_value = 0

    while queue:
        u = queue.popleft()
        visited += 1
        for v in graph[u]:
            for c in range(26):
                dp[v][c] = max(dp[v][c], dp[u][c] + (1 if ord(colors[v]) - ord('a') == c else 0))
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
        max_color_value = max(max_color_value, max(dp[u]))

    # Check for cycle
    if visited < n:
        return -1
    return max_color_value


ic(largest_path_value(colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]))
