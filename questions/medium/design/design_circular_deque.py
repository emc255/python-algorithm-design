"""
641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:
MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque.
Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque.
Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque.
Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque.
Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque.
Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque.
Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.


Example 1:
Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront",
"insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]
Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

Constraints:
1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront,
insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.

"""

from icecream import ic


class MyCircularDeque:
    def __init__(self, k: int):
        # Initialize the deque with size k + 1 to distinguish between empty and full states
        self.size = k + 1
        self.deque = [0] * self.size
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # Move front pointer backward in a circular manner
        self.front = (self.front - 1 + self.size) % self.size
        self.deque[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        # Insert at rear and move rear pointer forward
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # Move front pointer forward
        self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # Move rear pointer backward
        self.rear = (self.rear - 1 + self.size) % self.size
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        # (self.rear - 1 + self.size) % self.size gives the last element
        return self.deque[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        # Deque is full when one position ahead of rear is the front
        return (self.rear + 1) % self.size == self.front


de = MyCircularDeque(10)
ic(de.insertFront(1))
