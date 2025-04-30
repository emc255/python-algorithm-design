"""
61. Rotate List

Given the head of a linked list, rotate the list
to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
[5,1,2,3,4]
[4,5,1,2,3]
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
[2,0,1]
[1,2,0]
[0,1,2]
[2,0,1]
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

"""
from typing import Optional, Tuple

from icecream import ic

from shared.commons import ListNode, LinkedList


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if head is None:
        return None

    numbers = []
    while head:
        numbers = [head.val] + numbers
        head = head.next
    numbers = numbers[::-1]
    N = len(numbers)
    if k > N:
        k = k % len(numbers)

    for i in range(k):
        m = numbers[-1]
        numbers = [m] + numbers
        numbers = numbers[:N]

    dummy = ListNode(0)
    current = dummy
    for n in numbers:
        current.next = ListNode(n)
        current = current.next

    return dummy.next


def rotate_right_v2(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def length_and_tail(nodes: Optional[ListNode]) -> Tuple[int, Optional[ListNode]]:
        result = 0
        prev = None
        while nodes:
            result += 1
            prev = nodes
            nodes = nodes.next

        return result, prev

    if not head or not head.next or k == 0:
        return head

    l, tail = length_and_tail(head)

    k %= l
    if k == 0:
        return head

    runner = head

    for _ in range(l - k - 1):
        runner = runner.next
    new_head = runner.next
    runner.next = None
    tail.next = head
    return new_head


node = LinkedList([0, 1, 2])
ic(rotate_right(head=node.head, k=4).print())
node = LinkedList([1, 2, 4, 5, 6])
rotate_right_v2(head=node.head, k=3).print()
