"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?

"""
from typing import Optional

from shared.commons import ListNode, LinkedList


def is_palindrome(head: Optional[ListNode]) -> bool:
    a = []
    while head:
        a.append(head.val)
        head = head.next
    return a == a[::-1]


def is_palindrome_v2(head: Optional[ListNode]) -> bool:
    def reverse(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev, node = node, next_node

        return prev

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    n1 = head
    n2 = reverse(slow.next)
    while n2:
        if n1.val != n2.val:
            return False

        n1 = n1.next
        n2 = n2.next

    return True


nodes = LinkedList([1, 2, 3, 4, 2, 1]).head

print(is_palindrome(nodes))
print(is_palindrome_v2(nodes))
