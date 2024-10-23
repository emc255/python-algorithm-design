"""
2641. Cousins in Binary Tree II

Given the root of a binary tree, replace the value of each node in the tree
with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth
with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

Example 1:
Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation:
The diagram above shows the initial binary tree and the binary tree
after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.

Example 2:
Input: root = [3,1,2]
Output: [0,0,0]
Explanation:
The diagram above shows the initial binary tree and the binary tree
after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.

Constraints:
The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 104

"""
from collections import deque
from typing import Optional

from shared.commons import TreeNode


def replace_value_in_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    level_sum = []  # To store the sum of values at each level
    queue = deque([root])

    # First BFS: Calculate the sum of values at each level
    while queue:
        current_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            current_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level_sum.append(current_sum)

    # Second BFS: Update the value of each node
    queue = deque([(root, root.val)])
    level = 0
    while queue:
        for _ in range(len(queue)):
            node, parent_value = queue.popleft()
            # Subtract the parent value from the total level sum to get the cousin sum
            node.val = level_sum[level] - parent_value

            # Calculate the sum of the current node's children
            child_sum = 0
            if node.left:
                child_sum += node.left.val
            if node.right:
                child_sum += node.right.val

            # Add children to the queue with the new parent sum (which is their "cousins sum")
            if node.left:
                queue.append((node.left, child_sum))
            if node.right:
                queue.append((node.right, child_sum))

        level += 1  # Move to the next level

    return root


tree = TreeNode(5)
tree.left = TreeNode(4)
tree.right = TreeNode(9)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(10)
tree.right.right = TreeNode(7)

replace_value_in_tree(tree).print()
