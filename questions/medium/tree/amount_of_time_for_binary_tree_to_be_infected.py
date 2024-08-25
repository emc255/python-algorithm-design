"""
2385. Amount of Time for Binary Tree to Be Infected

You are given the root of a binary tree with unique vals, and an integer start.
At minute 0, an infection starts from the node with val start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

Example 1:
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

Example 2:
Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.

Constraints:
The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
Each node has a unique val.
A node with a val of start exists in the tree.

"""
from collections import deque
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def amount_of_time(root: Optional[TreeNode], start: int) -> int:
    def convert(current_node: TreeNode, parent: int, adjacent_map: dict):
        if current_node is None:
            return
        if current_node.val not in adjacent_map:
            tree_map[current_node.val] = set()

        if parent != 0:
            tree_map[current_node.val].add(parent)
        if current_node.left:
            tree_map[current_node.val].add(current_node.left.val)
        if current_node.right:
            tree_map[current_node.val].add(current_node.right.val)
        convert(current_node.left, current_node.val, adjacent_map)
        convert(current_node.right, current_node.val, adjacent_map)

    tree_map = {}
    convert(root, 0, tree_map)
    queue = deque([start])
    minute = 0
    visited = {start}

    while queue:
        level_size = len(queue)
        while level_size > 0:
            current = queue.popleft()
            for num in tree_map[current]:
                if num not in visited:
                    visited.add(num)
                    queue.append(num)
            level_size -= 1
        minute += 1

    return minute - 1


tree = TreeNode(1)
tree.left = TreeNode(5)
tree.right = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(10)
tree.right.right = TreeNode(6)
tree.left.right.left = TreeNode(9)
tree.left.right.right = TreeNode(2)

ic(amount_of_time(tree, 3))
