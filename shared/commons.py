class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def print(self):
        current = self
        print("==LIST NODE HEAD==")
        while current is not None:
            print(current.val)
            current = current.next
        print("========END=======")


class LinkedList:
    def __init__(self, numbers: list):
        dummy = ListNode(0)
        current = dummy
        for number in numbers:
            current.next = ListNode(number)
            current = current.next

        self.head = dummy.next
