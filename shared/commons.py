class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        current = self
        print("==LIST NODE HEAD==")
        while current is not None:
            print(current.val)
            current = current.next
        print("========END=======")
