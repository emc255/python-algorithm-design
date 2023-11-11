"""
2642. Design Graph With Shortest Path Calculator


There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1.
The edges of the graph are initially represented by
the given array edges where edges[i] = [fromi, toi,
edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:
Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost].
It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2.
If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.


Example 1:
Input
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
Output
[null, 6, -1, null, 6]
Explanation
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first
diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3
with a total cost of 2 + 4 = 6.

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1)
edges[i].length == edge.length == 3
0 <= fromi, toi, from, to, node1, node2 <= n - 1
1 <= edgeCosti, edgeCost <= 106
There are no repeated edges and no self-loops in the graph at any point.
At most 100 calls will be made for addEdge.
At most 100 calls will be made for shortestPath.

"""
import heapq

from icecream import ic


class Graph:

    def __init__(self, n: int, edges: list[list]):
        self.graph = {i: [] for i in range(n)}
        for root, node, weight in edges:
            self.graph[root].append((node, weight))

    def add_edge(self, edge: list) -> None:
        root, node, weight = edge
        self.graph[root].append((node, weight))

    def shortest_path(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        distances = {node: float('infinity') for node in self.graph}
        distances[node1] = 0

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_node == node2:
                return current_distance

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        # return distances[node2] if distances[node2] != float('infinity') else -1
        return -1


g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
ic(g.shortest_path(3, 2))
