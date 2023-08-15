"""
86. Partition List

Given the head of a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

"""
from typing import Optional

from shared.commons import ListNode, LinkedList


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    current = dummy.next
    left = []
    right = []
    while current:
        if current.val >= x:
            right.append(current.val)
        else:
            left.append(current.val)
        current = current.next
    left.extend(right)
    current = dummy.next
    for n in left:
        current.val = n
        current = current.next

    return dummy.next


def partition_v2(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    before, after = ListNode(0), ListNode(0)
    before_curr, after_curr = before, after

    while head:
        if head.val < x:
            before_curr.next = head
            before_curr = head
        else:
            after_curr.next = head
            after_curr = head
        head = head.next

    after_curr.next = None
    before_curr.next = after.next

    return before.next


partition(LinkedList([1, 4, 3, 2, 5, 2]).head, 3).print()
partition_v2(LinkedList([1, 4, 3, 2, 5, 2]).head, 3).print()
