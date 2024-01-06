"""
Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done
from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays,
return the maximum profit you can take such
that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X
you will be able to start another job that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

Constraints:
1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104

"""
import bisect

from icecream import ic


def job_scheduling(start_time: list[int], end_time: list[int], profit: list[int]) -> int:
    intervals = sorted(zip(start_time, end_time, profit))

    def dfs(i):
        if i == len(intervals):
            return 0
        if i in memo:
            return memo[i]

        # dont include
        result = dfs(i + 1)

        # include
        # implements binary search
        j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
        # j = i + 1 time limit exceeded
        # while j < len(intervals):
        #     if intervals[i][1] <= intervals[j][0]:
        #         break
        #     j += 1
        result = max(result, intervals[i][2] + dfs(j))
        memo[i] = result
        return result

    memo = {}
    return dfs(0)


ic(job_scheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
