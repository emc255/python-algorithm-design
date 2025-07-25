"""
2071. Maximum Number of Tasks You Can Assign

You have n tasks and m workers. Each task has a strength requirement stored
in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength
to complete. The strength of each worker is stored in a 0-indexed integer array workers,
with the jth worker having workers[j] strength. Each worker can only be assigned
to a single task and must have a strength greater than or equal to the task's
strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength
by strength. You can decide which workers receive the magical pills, however,
you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills
and strength, return the maximum number of tasks that can be completed.

Example 1:
Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)

Example 2:
Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)

Example 3:
Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.

Constraints:
n == tasks.length
m == workers.length
1 <= n, m <= 5 * 104
0 <= pills <= m
0 <= tasks[i], workers[j], strength <= 109

"""
from collections import deque

from icecream import ic


def max_task_assign(tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
    def can_assign(middle):
        available_pills = pills
        available_workers = deque()
        ptr = NWorkers - 1

        for i in range(middle - 1, -1, -1):
            while ptr >= NWorkers - mid and workers[ptr] + strength >= tasks[i]:
                available_workers.appendleft(workers[ptr])
                ptr -= 1
            ic(available_workers)
            if not available_workers:
                return False

            elif available_workers[-1] >= tasks[i]:
                available_workers.pop()

            else:
                if available_pills == 0:
                    return False

                available_pills -= 1
                available_workers.popleft()

        return True

    NWorkers = len(workers)
    tasks.sort()
    workers.sort()
    left, right = 0, min(len(tasks), len(workers))
    result = 0

    # Binary search for max number of assignable tasks
    while left <= right:
        mid = (left + right) // 2
        if can_assign(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


"""
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid: int) -> bool:
            p = pills
            ws = deque()
            ptr = m - 1
            # Enumerate each task from largest to smallest
            for i in range(mid - 1, -1, -1):
                while ptr >= m - mid and workers[ptr] + strength >= tasks[i]:
                    ws.appendleft(workers[ptr])
                    ptr -= 1
                if not ws:
                    return False
                # If the largest element in the deque is greater than or equal to tasks[i]
                elif ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    p -= 1
                    ws.popleft()
            return True

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

"""
ic(max_task_assign(tasks=[10, 15, 30], workers=[0, 10, 10, 10, 10], pills=3, strength=10))
ic(max_task_assign(tasks=[5, 9, 8, 5, 9], workers=[1, 6, 4, 2, 6], pills=1, strength=5))
