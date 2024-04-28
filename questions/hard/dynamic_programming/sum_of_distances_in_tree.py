"""
Sum of Distances in Tree

There is an undirected connected tree
with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges
where edges[i] = [ai, bi] indicates that there is an edge
between nodes ai and bi in the tree.

Return an array answer of length n
where answer[i] is the sum of the distances between
the ith node in the tree and all other nodes.

Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:
Input: n = 1, edges = []
Output: [0]

Example 3:
Input: n = 2, edges = [[1,0]]
Output: [1,1]

Constraints:
1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.

"""
from collections import defaultdict

from icecream import ic


def sum_of_distances_in_tree(n: int, edges: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    closer_nodes_count = [0] * n
    answer = [0] * n
    seen = set()

    def dfs(current):
        nonlocal closer_nodes_count, answer
        closer_node = 1
        for child in graph[current]:

            if child not in seen:
                seen.add(child)
                child_nodes_count = dfs(child)
                closer_node += child_nodes_count
                answer[0] += child_nodes_count

            closer_nodes_count[current] = closer_node

        return closer_node

    seen.add(0)
    dfs(0)

    def dfs2(cur):
        nonlocal answer
        for child in graph[cur]:
            if child not in seen:
                seen.add(child)
                answer[child] = answer[cur] - closer_nodes_count[child] + (n - closer_nodes_count[child])
                dfs2(child)

    seen = set()
    seen.add(0)
    dfs2(0)

    return answer


def sum_of_distances_in_tree_v2(n: int, edges: list[list[int]]) -> list[int]:
    # Graph initialization
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Arrays to store subtree size and distance sum
    count = [1] * n
    answer = [0] * n

    # Post-order DFS to populate count and answer
    def postOrder(node, parent):
        for child in graph[node]:
            if child != parent:
                postOrder(child, node)
                count[node] += count[child]
                answer[node] += answer[child] + count[child]

    # Pre-order DFS to adjust answer based on parent's data
    def preOrder(node, parent):
        for child in graph[node]:
            if child != parent:
                answer[child] = answer[node] - count[child] + n - count[child]
                preOrder(child, node)

    # Perform post-order and pre-order traversals
    postOrder(0, -1)  # Starting from node 0 and assuming no parent with -1
    preOrder(0, -1)

    return answer


ic(sum_of_distances_in_tree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
