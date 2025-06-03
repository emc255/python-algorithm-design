"""
1298. Maximum Candies You Can Get from Boxes

You have n boxes labeled from 0 to n - 1. You are given four arrays:
status, candies, keys, and containedBoxes where:

status[i] is 1 if the ith box is open and 0 if the ith box is closed,
candies[i] is the number of candies in the ith box, keys[i] is a list
of the labels of the boxes you can open after opening the ith box.
containedBoxes[i] is a list of the boxes you found inside the ith box.

You are given an integer array initialBoxes that contains the labels
of the boxes you initially have. You can take all the candies in any
open box and you can use the keys in it to open new boxes and you
also can use the boxes you find in it.

Return the maximum number of candies you can get following the rules above.

Example 1:
Input:
status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]],
contained_boxes = [[1,2],[3],[],[]], initial_boxes = [0]
Output: 16
Explanation:
You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
Box 1 is closed and you do not have a key for it so you will open box 2. You will
find 4 candies and a key to box 1 in box 2. In box 1, you will find 5 candies
and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.

Example 2:
Input:
status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]],
contained_boxes = [[1,2,3,4,5],[],[],[],[],[]], initial_boxes = [0]
Output: 6
Explanation:
You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
The total number of candies will be 6.

Constraints:
n == status.length == candies.length == keys.length == containedBoxes.length
1 <= n <= 1000
status[i] is either 0 or 1.
1 <= candies[i] <= 1000
0 <= keys[i].length <= n
0 <= keys[i][j] < n
All values of keys[i] are unique.
0 <= containedBoxes[i].length <= n
0 <= containedBoxes[i][j] < n
All values of containedBoxes[i] are unique.
Each box is contained in one box at most.
0 <= initialBoxes.length <= n
0 <= initialBoxes[i] < n

"""
from collections import deque

from icecream import ic


def max_candies(status: list[int], candies: list[int], keys: list[list[int]], contained_boxes: list[list[int]],
                initial_boxes: list[int]) -> int:
    n = len(status)
    has_box = [False] * n
    has_key = [False] * n
    opened = [False] * n

    queue = deque()

    for box in initial_boxes:
        has_box[box] = True
        if status[box] == 1:
            queue.append(box)

    result = 0

    while queue:
        box = queue.popleft()
        if opened[box]:
            continue
        opened[box] = True
        result += candies[box]

        # Add keys found in the current box
        for key in keys[box]:
            has_key[key] = True
            if has_box[key] and not opened[key]:
                queue.append(key)

        # Add contained boxes
        for contained in contained_boxes[box]:
            has_box[contained] = True
            if has_key[contained] and not opened[contained]:
                queue.append(contained)

        # Recheck boxes that might now be openable (status=1 or has key)
        for i in range(n):
            if has_box[i] and not opened[i] and (status[i] == 1 or has_key[i]):
                queue.append(i)

    return result


ic(max_candies(status=[1, 0, 1, 0], candies=[7, 5, 4, 100], keys=[[], [], [1], []],
               contained_boxes=[[1, 2], [3], [], []], initial_boxes=[0]))

ic(max_candies(status=[1, 0, 0, 0, 0, 0], candies=[1, 1, 1, 1, 1, 1], keys=[[1, 2, 3, 4, 5], [], [], [], [], []],
               contained_boxes=[[1, 2, 3, 4, 5], [], [], [], [], []], initial_boxes=[0]))
