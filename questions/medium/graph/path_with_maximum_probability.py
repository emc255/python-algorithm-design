"""
1514. Path with Maximum Probability

You are given an undirected weighted graph of n nodes (0-indexed),
represented by an edge list where edges[i] = [a, b] is an undirected edge
connecting the nodes a and b with a probability of success of traversing
that edge success_probability[i].

Given two nodes start and end, find the path with the maximum probability
of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will
be accepted if it differs from the correct answer by at most 1e-5.

Example 1:
Input:
n = 3, edges = [[0,1],[1,2],[0,2]],
success_probability = [0.5,0.5,0.2],
start = 0, end = 2
Output: 0.25000
Explanation:
There are two paths from start to end, one having a probability
of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
Input:
n = 3, edges = [[0,1],[1,2],[0,2]],
success_probability = [0.5,0.5,0.3],
start = 0, end = 2
Output: 0.30000

Example 3:
Input:
n = 3, edges = [[0,1]],
success_probability = [0.5],
start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.


Constraints:
2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= success_probability.length == edges.length <= 2*10^4
0 <= success_probability[i] <= 1
There is at most one edge between every two nodes.

"""
import heapq
from collections import defaultdict

from icecream import ic


def max_probability(n: int, edges: list[list[int]], success_probability: list[float], start_node: int,
                    end_node: int) -> float:
    graph = defaultdict(list)
    visited = set()
    priority_queue = [(-1, start_node)]

    for i, (source, distance) in enumerate(edges):
        graph[source].append([distance, success_probability[i]])
        graph[distance].append([source, success_probability[i]])

    while priority_queue:
        probability, node = heapq.heappop(priority_queue)
        visited.add(node)
        if node == end_node:
            return probability * -1

        for neighbor, neighbor_probability in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (probability * neighbor_probability, neighbor))

    return 0


ic(max_probability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
