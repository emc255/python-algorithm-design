"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""

from typing import Optional

from shared.commons import ListNode, LinkedList


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current:
        while current.next and current.next.val == current.val:
            current.next = current.next.next

        current = current.next

    return head


nodes = LinkedList([1, 1, 2, 3, 3, 3, 4])

delete_duplicates(nodes.head).print()
