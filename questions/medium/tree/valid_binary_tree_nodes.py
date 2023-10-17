"""
1361. Validate Binary Tree Nodes

You have n binary tree nodes numbered from 0 to n - 1
where node i has two children leftChild[i] and rightChild[i],
return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Constraints:
n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1

"""
from collections import deque

from icecream import ic


def valid_binary_tree_nodes(n: int, left_child: list, right_child: list) -> bool:
    def dfs(index):
        if index == -1:
            return True
        if index in visited:
            return False
        visited.add(index)
        return dfs(left_child[index]) and dfs(right_child[index])

    has_parent = set(left_child + right_child)
    has_parent.discard(-1)
    visited = set()

    if len(has_parent) == n:
        return False

    root = -1
    for i in range(n):
        if i not in has_parent:
            root = i
            break

    return dfs(root) and len(visited) == n


def valid_binary_tree_nodes_v2(n: int, left_child: list, right_child: list) -> bool:
    indegree = [0] * n  # Initialize in-degree of all nodes to 0

    # Build the in-degree array in a single pass
    for i in range(n):
        if left_child[i] != -1:
            indegree[left_child[i]] += 1
        if right_child[i] != -1:
            indegree[right_child[i]] += 1
    ic(indegree)
    # Find the root (node with in-degree 0)
    root = None
    for i in range(n):
        if indegree[i] == 0:
            if root is None:
                root = i
            else:
                return False  # More than one root

    # If there's no root
    if root is None:
        return False

    visited = [False] * n
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if visited[node]:
            return False  # Already visited this node, not a valid tree
        visited[node] = True
        if left_child[node] != -1:
            queue.append(left_child[node])
        if right_child[node] != -1:
            queue.append(right_child[node])

    return sum(visited) == n  # If all nodes are visited, it's a valid tree


ic(valid_binary_tree_nodes(4, [1, -1, 3, -1], [2, -1, -1, -1]))
ic(valid_binary_tree_nodes(4, [1, -1, 3, -1], [2, 3, -1, -1]))
ic(valid_binary_tree_nodes(2, [1, 0], [-1, -1]))
