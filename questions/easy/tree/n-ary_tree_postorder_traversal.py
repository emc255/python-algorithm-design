"""
590. N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal
of its nodes' values.

Nary-Tree input serialization is represented in their level
order traversal. Each group of children is separated by the null
value (See examples)

Example 1:
Input:
root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Example 2:
Input:
root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.

Follow up: Recursive solution is trivial, could you do it iteratively?

"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def postorder(root: "Node") -> list[int]:
    result = []
    # If the root is None, return the empty list
    if root is None:
        return result

    node_stack = [(root, False)]

    while node_stack:
        current_node, is_visited = node_stack.pop()

        if is_visited:
            # If the node has been visited, add its value to the result
            result.append(current_node.val)
        else:
            # Mark the current node as visited and push it back to the stack
            node_stack.append((current_node, True))

            # Push all children to the stack in reverse order
            for child in reversed(current_node.children):
                node_stack.append((child, False))

    return result


def postorder_v2(root: "Node") -> list[int]:
    def traverse_postorder(current_node: "Node", postorder_list: list[int]) -> None:
        if not current_node:
            return

        # First, visit all children
        for child_node in current_node.children:
            traverse_postorder(child_node, postorder_list)

        # Then, add the current node's value
        postorder_list.append(current_node.val)

    result = []
    if not root:
        return result

    traverse_postorder(root, result)
    return result


def postorder_v3(root: 'Node') -> list[int]:
    result = []

    # If the root is None, return the empty list
    if root is None:
        return result

    node_stack = [root]

    # Traverse the tree using the stack
    while node_stack:
        current_node = node_stack.pop()
        result.append(current_node.val)
        # Push all the children of the current node to the stack
        for child in current_node.children:
            node_stack.append(child)

    # Reverse the result list to get the correct postorder traversal
    result.reverse()
    return result
