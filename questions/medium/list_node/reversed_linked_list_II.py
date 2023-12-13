"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

"""
from typing import Optional

from shared.commons import ListNode, LinkedList


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    values = []
    while head:
        values.append(head.val)
        head = head.next

    left = left - 1
    values[left:right] = reversed(values[left:right])
    for value in values:
        node = ListNode(value)
        current.next = node
        current = current.next

    return dummy.next


reverse_between(LinkedList([1, 2, 3, 4, 5]).head, 2, 3).print()
reverse_between(LinkedList([1, 2, 3, 4]).head, 1, 4).print()
