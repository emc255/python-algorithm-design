"""
Double a Number Represented as a Linked List

You are given the head of a non-empty linked list
representing a non-negative integer without leading zeroes.
Return the head of the linked list after doubling it.

Example 1:
Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list
which represents the number 189. Hence,
the returned linked list represents the number 189 * 2 = 378.

Example 2:
Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list
which represents the number 999. Hence,
the returned linked list reprersents the number 999 * 2 = 1998.

Constraints:
The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that
the list represents a number that does not have leading zeros,
except the number 0 itself.

"""

from typing import Optional

from shared.commons import ListNode


def double_it(head: Optional[ListNode]) -> Optional[ListNode]:
    answer = 0
    while head:
        answer = (answer * 10) + head.val
        head = head.next

    answer = answer * 2
    dummy = ListNode(0)
    result = dummy

    if answer == 0:
        return ListNode(0)

    while answer:
        r = answer % 10
        answer //= 10
        dummy.next = ListNode(r)
        dummy = dummy.next

    dummy = result.next
    reverse = None

    while dummy:
        next_node = dummy.next
        dummy.next = reverse
        reverse = dummy
        dummy = next_node

    return reverse


def double_it_v2(head: Optional[ListNode]) -> Optional[ListNode]:
    if head.val > 4:
        head = ListNode(0, head)
    node = head
    while node:
        node.val = (node.val * 2) % 10
        if node.next and node.next.val > 4:
            node.val += 1
        node = node.next
    return head


nodes = ListNode(9)
nodes.next = ListNode(9)
nodes.next.next = ListNode(9)

double_it(nodes).print()
double_it(ListNode(0)).print()
