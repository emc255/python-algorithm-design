"""

203. Remove Linked List Elements

Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50

"""
from typing import Optional

from shared.commons import ListNode, LinkedList


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    current_nodes = dummy

    while current_nodes.next:
        if current_nodes.next.val == val:
            current_nodes.next = current_nodes.next.next
        else:
            current_nodes = current_nodes.next

    return dummy.next


nodes = LinkedList([1, 2, 6, 3, 4, 5, 6]).head

remove_elements(nodes, 6).print()
