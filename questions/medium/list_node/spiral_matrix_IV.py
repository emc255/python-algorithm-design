"""
2326. Spiral Matrix IV

You are given two integers m and n,
which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented
in spiral order (clockwise), starting from the top-left of the matrix. If there
are remaining empty spaces, fill them with -1.

Return the generated matrix.

Example 1:
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation:
The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

Example 2:
Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation:
The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.

Constraints:
1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000

"""
from typing import Optional

from icecream import ic

from shared.commons import ListNode


def spiral_matrix(m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
    result = [[-1 for _ in range(n)] for _ in range(m)]
    r, c = 0, 0
    dr, dc = 0, 1  # initial direction is right (0, 1)

    for _ in range(m * n):
        if not head:
            break
        result[r][c] = head.val
        head = head.next

        # Calculate the next position
        nr, nc = r + dr, c + dc

        # Check if we need to change direction (out of bounds or the cell is already filled)
        if not (0 <= nr < m and 0 <= nc < n and result[nr][nc] == -1):
            # Turn to the next direction (right -> down -> left -> up)
            dr, dc = dc, -dr

        # Move to the next cell
        r, c = r + dr, c + dc

    return result


def spiral_matrix_v2(rows: int, columns: int, head: ListNode) -> list[list[int]]:
    matrix = [[-1] * columns for _ in range(rows)]

    topRow, bottomRow = 0, rows - 1
    leftColumn, rightColumn = 0, columns - 1

    while head:
        for col in range(leftColumn, rightColumn + 1):
            if head:
                matrix[topRow][col] = head.val
                head = head.next
        topRow += 1

        for row in range(topRow, bottomRow + 1):
            if head:
                matrix[row][rightColumn] = head.val
                head = head.next
        rightColumn -= 1

        for col in range(rightColumn, leftColumn - 1, -1):
            if head:
                matrix[bottomRow][col] = head.val
                head = head.next
        bottomRow -= 1

        for row in range(bottomRow, topRow - 1, -1):
            if head:
                matrix[row][leftColumn] = head.val
                head = head.next
        leftColumn += 1

    return matrix


nodes = ListNode(3)
nodes.next = ListNode(0)
nodes.next.next = ListNode(2)
nodes.next.next.next = ListNode(6)
nodes.next.next.next.next = ListNode(8)
nodes.next.next.next.next.next = ListNode(1)
nodes.next.next.next.next.next.next = ListNode(7)
nodes.next.next.next.next.next.next.next = ListNode(9)
nodes.next.next.next.next.next.next.next.next = ListNode(4)
nodes.next.next.next.next.next.next.next.next.next = ListNode(2)
nodes.next.next.next.next.next.next.next.next.next.next = ListNode(5)
nodes.next.next.next.next.next.next.next.next.next.next.next = ListNode(5)
nodes.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)

ic(spiral_matrix(3, 5, nodes))
