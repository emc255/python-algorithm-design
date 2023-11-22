"""
1424. Diagonal Traverse II

Given a 2D integer array nums,
return all elements of nums in diagonal order as shown in the below images.

Example 1:
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

Constraints:
1 <= nums.length <= 105
1 <= nums[i].length <= 105
1 <= sum(nums[i].length) <= 105
1 <= nums[i][j] <= 105

"""
from collections import defaultdict, deque

from icecream import ic


def find_diagonal_order(nums: list[list]) -> list:
    result = []
    diagonals = defaultdict(list)
    for r in range(len(nums)):
        for c in range(len(nums[r])):
            diagonals[r + c].append(nums[r][c])
    for v in diagonals.values():
        result.extend(reversed(v))

    return result


def find_diagonal_order_v2(nums: list[list]) -> list:
    queue = deque()
    result = []

    # start with initial, it has two neighbor, right and down
    queue.append((0, 0))

    while queue:
        row, col = queue.popleft()

        result.append(nums[row][col])

        # add neighbor of current node, if first col, go to next row
        if col == 0 and row + 1 < len(nums):
            queue.append((row + 1, col))

        # add right neighbor
        if col + 1 < len(nums[row]):
            queue.append((row, col + 1))

        # [0,0] -> [1,0],[0,1] -> process [1,0] first and add [2,0],[1,1]
        #  process [0,1], so, add 0,2, q=[2,0][1,1][0,2]
        # then q=[3,0],[2,1] [1,2],[0,3]
    return result


# ic(find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

ic(find_diagonal_order([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
