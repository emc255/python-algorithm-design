"""
1381. Design a Stack With Increment Operation

Design a stack that supports increment operations
on its elements.

Implement the CustomStack class:
CustomStack(int maxSize) Initializes the object with maxSize
which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack
has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1
if the stack is empty.
void inc(int k, int val) Increments the bottom k elements
of the stack by val. If there are less than k elements
in the stack, increment all the elements in the stack.

Example 1:
Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack stk = new CustomStack(3); // Stack is Empty []
stk.push(1);                          // stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.push(3);                          // stack becomes [1, 2, 3]
stk.push(4);                          // stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100);                // stack becomes [101, 102, 103]
stk.increment(2, 100);                // stack becomes [201, 202, 103]
stk.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop();                            // return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop();                            // return 201 --> Return top of the stack 201, stack becomes []
stk.pop();                            // return -1 --> Stack is empty return -1.

Constraints:
1 <= maxSize, x, k <= 1000
0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately.

"""
from icecream import ic


class _Node:
    def __init__(self, val: int = -1, next_node: '_Node' = None):
        self.val = val
        self.next = next_node


class CustomStack:

    def __init__(self, maxSize: int):
        self.list_nodes = self.__create_nodes(maxSize)

    def push(self, x: int) -> None:
        current = self.list_nodes
        while current:
            if current.val == -1:
                current.val = x
                break
            current = current.next

    def pop(self) -> int:
        current = self.list_nodes
        if current.val == -1:
            return -1

        prev = _Node()
        while current and current.val != -1:
            prev = current
            current = current.next
        temp = prev.val
        prev.val = -1

        return temp

    def increment(self, k: int, val: int) -> None:
        current = self.list_nodes
        while current and k and current.val != -1:
            current.val += val
            current = current.next
            k -= 1
        a = self.list_nodes
        while a:
            ic(a.val)
            a = a.next

    def __create_nodes(self, max_size: int):
        dummy = _Node()
        current = dummy
        for i in range(max_size):
            current.next = _Node()
            current = current.next
        return dummy.next


custom_stack = CustomStack(3)
custom_stack.push(1)
custom_stack.push(2)
ic(custom_stack.pop())
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(4)
custom_stack.increment(5, 100)
custom_stack.increment(2, 100)
ic(custom_stack.pop())
ic(custom_stack.pop())
ic(custom_stack.pop())
ic(custom_stack.pop())
