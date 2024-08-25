"""
752. Open the Lock

You have a lock in front of you with 4 circular wheels.
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
The wheels can rotate freely and wrap around:
for example we can turn '9' to be '0', or '0' to be '9'.
Each move consists of turning one wheel one slot.

The lock initially starts at '0000',
a string representing the state of the 4 wheels.

You are given a list of deadends dead ends,
meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.

Constraints:
1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.

"""
import heapq
from collections import deque

from icecream import ic


def open_lock(dead_ends: list[str], target: str) -> int:
    def children(lock):
        result = []
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            result.append(lock[:i] + digit + lock[i + 1:])
            digit = str((int(lock[i]) - 1 + 10) % 10)
            result.append(lock[:i] + digit + lock[i + 1:])
        return result

    if "0000" in dead_ends:
        return -1

    queue = deque()
    queue.append(["0000", 0])  # [locks, turn]
    visited = set(dead_ends)
    while queue:
        lock, turn = queue.popleft()

        if lock == target:
            return turn

        for child in children(lock):
            if child not in visited:
                visited.add(child)
                queue.append([child, turn + 1])
    return -1


def open_lock_memoization(dead_ends: list[str], target: str) -> int:
    def priority(current: str, target: str) -> int:
        total_turns = 0
        for cur_digit, tar_digit in zip(current, target):
            cur_val, tar_val = int(cur_digit), int(tar_digit)
            turns = min(abs(tar_val - cur_val), 10 - abs(tar_val - cur_val))
            total_turns += turns
        return total_turns

    dead_ends_set = set(dead_ends)
    if "0000" in dead_ends_set:
        return -1

    visited = set()
    pending = []
    heapq.heapify(pending)
    heapq.heappush(pending, (priority("0000", target), 0, "0000"))
    visited.add("0000")

    while pending:
        _, turns_so_far, current = heapq.heappop(pending)
        if current == target:
            return turns_so_far
        if current in dead_ends_set:
            continue

        for wheel in range(4):
            for move in [-1, 1]:
                new_digit = (int(current[wheel]) + move) % 10
                new_combination = current[:wheel] + str(new_digit) + current[wheel + 1:]
                if new_combination not in visited:
                    heapq.heappush(pending, (
                        turns_so_far + 1 + priority(new_combination, target), turns_so_far + 1, new_combination))
                    visited.add(new_combination)

    return -1


ic(open_lock(["0201", "0101", "0102", "1212", "2002"], "0202"))
ic(open_lock_memoization(["0201", "0101", "0102", "1212", "2002"], "0202"))
