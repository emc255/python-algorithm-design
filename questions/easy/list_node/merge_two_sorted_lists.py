"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
from typing import Optional

from icecream import ic

from shared.commons import LinkedList, ListNode


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    while list1 or list2:
        if list1 and (not list2 or list1.val <= list2.val):
            current.next = ListNode(list1.val)
            list1 = list1.next
        else:
            current.next = ListNode(list2.val)
            list2 = list2.next

        current = current.next

    return dummy.next


l1 = LinkedList([1, 2, 4]).head
l2 = LinkedList([1, 3, 4]).head

ic(merge_two_lists(l1, l2).print())
