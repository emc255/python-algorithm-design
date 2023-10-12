from collections import deque


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
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


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def print(self):
        queue_nodes = deque()
        queue_nodes.append(self)
        print("==TREE NODE HEAD==")
        while queue_nodes:
            node = queue_nodes.popleft()
            print(node.val)
            if node.left:
                queue_nodes.append(node.left)
            if node.right:
                queue_nodes.append(node.right)
        print("========END=======")


class Tree:
    def __init__(self, array: list):
        self.head = self.create(array)

    def create(self, arr: list, index: int = 0):
        # root = TreeNode(arr[0])
        # l = True
        # for i in range(1, len(arr)):
        #     if l:
        #         if arr[i]:
        #             root.left = TreeNode(arr[i])
        #         l = False
        #     else:
        #         if arr[i]:
        #             root.right = TreeNode(arr[i])
        #
        #     if root.left:
        if index < len(arr):
            root = TreeNode(arr[index])
            root.left = self.create(arr, 2 * index + 1)
            root.right = self.create(arr, 2 * index + 2)

            return root

        return None


class Node:
    def __init__(self, x: int, next_node: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next_node
        self.random = random

    def print(self):
        current = self
        while current:
            print(f'VALUE = {current.val}')
            if current.random:
                current_random = current.random
                print("Random")
                while current_random:
                    print(f'\t{current_random.val}')
                    current_random = current_random.next
            current = current.next


class MountainArray:
    def __init__(self, arr: list):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)
