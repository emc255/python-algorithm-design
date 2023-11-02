from collections import deque

from icecream import ic

from shared.commons import TreeNode

head = TreeNode(1)
head.left = TreeNode(2)
head.left.left = TreeNode(3)
head.left.right = TreeNode(6)
head.right = TreeNode(3)
head.right.left = TreeNode(5)


def preorder_traversal(root):
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []


def preorder_traversal_v2(root: TreeNode) -> list:
    res = []
    stack = deque([(root, False)])
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # preorder: root -> left -> right
                stack.append((node.right, False))
                stack.append((node.left, False))
                stack.append((node, True))
    return res


print("PREORDER")
print(preorder_traversal(head))
print(preorder_traversal_v2(head))
print("==========")


def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


def inorder_traversal_v2(root: TreeNode) -> list:
    res = []
    stack = deque([(root, False)])
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # inorder: left -> root -> right
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
    return res


print("INORDER")
print(inorder_traversal(head))
print(inorder_traversal_v2(head))
print("==========")


def postorder_traversal(root):
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val] if root else []


def postorder_traversal_v2(root: TreeNode) -> list:
    res = []
    stack = deque([(root, False)])
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # postorder: left -> right -> root
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return res


print("POSTORDER")
ic(postorder_traversal(head))
ic(postorder_traversal_v2(head))
print("==========")
