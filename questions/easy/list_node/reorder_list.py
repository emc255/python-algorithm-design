"""
Reorder List

You are given the head of a singly linked-list.
The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes.
Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

"""
from typing import Optional

from icecream import ic

from shared.commons import ListNode, LinkedList


def reorder_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

        # Step 1: Find the middle of the linked list
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    second = slow.next
    prev = slow.next = None

    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # Step 3: Merge the two halves
    first = head
    second = prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2


nodes = LinkedList([1, 2, 3, 4]).head
b = reorder_list(nodes)

while b:
    ic(b.val)
    b = b.next
