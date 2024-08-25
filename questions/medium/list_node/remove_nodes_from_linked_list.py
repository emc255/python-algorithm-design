"""
2487. Remove Nodes From Linked List

You are given the head of a linked list.
Remove every node which has a node with a greater value
anywhere to the right side of it.

Return the head of the modified linked list.

Example 1:
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

Example 2:
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.

Constraints:
The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105

"""
from collections import deque
from typing import Optional

from shared.commons import ListNode


def remove_nodes(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    stack = deque()
    while current:
        while stack and stack[-1] < current.val:
            stack.pop()
        stack.append(current.val)
        current = current.next

    dummy = ListNode(0)
    result = dummy
    while stack:
        dummy.next = ListNode(stack.popleft())
        dummy = dummy.next

    return result.next


nodes = ListNode(5)
nodes.next = ListNode(2)
nodes.next.next = ListNode(13)
nodes.next.next.next = ListNode(3)
nodes.next.next.next.next = ListNode(8)

remove_nodes(nodes).print()
