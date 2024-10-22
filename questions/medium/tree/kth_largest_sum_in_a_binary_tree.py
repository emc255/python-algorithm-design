"""
2583. Kth Largest Sum in a Binary Tree

You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes
that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct).
If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance
from the root.

Example 1:
Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.

Example 2:
Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.

Constraints:
The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n

"""
from collections import defaultdict, deque
from typing import Optional

from icecream import ic

from shared.commons import TreeNode


def kth_largest_level_sum(root: Optional[TreeNode], k: int) -> int:
    # Dictionary to store the sum of node values at each level
    level_sums = defaultdict(int)
    queue = deque([(root, 0)])  # Use deque for efficient queue operations

    # Perform level order traversal to compute level sums
    while queue:
        node, level = queue.popleft()  # Use popleft for deque to maintain queue behavior
        level_sums[level] += node.val

        # Add child nodes to the queue with incremented level
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    # Get the level sums sorted in descending order
    sorted_sums = sorted(level_sums.values(), reverse=True)

    # Return the k-th largest sum or -1 if k is out of bounds
    return sorted_sums[k - 1] if k <= len(sorted_sums) else -1


tree = TreeNode(5)
tree.left = TreeNode(8)
tree.right = TreeNode(9)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(1)
tree.right.left = TreeNode(3)
tree.right.right = TreeNode(7)
tree.left.left.left = TreeNode(4)
tree.left.left.right = TreeNode(6)

ic(kth_largest_level_sum(tree, 2))
