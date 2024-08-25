"""
82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""
from typing import Optional

from shared.commons import ListNode, LinkedList


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head
    while current:
        while current.next and current.next.val == current.val:
            current = current.next

        if prev.next == current:
            prev = prev.next
        else:
            prev.next = current.next

        current = current.next

    return dummy.next


nodes = LinkedList([1, 1, 2, 3, 3, 3, 4, 4, 5])

delete_duplicates(nodes.head).print()
