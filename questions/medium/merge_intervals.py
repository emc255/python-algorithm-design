"""
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""
from icecream import ic


def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  # Sort intervals by their start point
    result = [intervals[0]]

    for i in range(1, len(intervals)):
        l, r = intervals[i]
        found = False

        for j in range(len(result)):
            left, right = result[j]

            if l <= right:  # If there's an overlap
                result[j] = [min(l, left), max(r, right)]
                found = True
                break

        if not found:
            result.append([l, r])

    return result


def merge_v2(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])

    result = []
    n = len(intervals)

    for i in range(n):
        if i == 0 or result[-1][1] < intervals[i][0]:
            result.append(intervals[i])
        else:
            result[-1][1] = max(result[-1][1], intervals[i][1])
    return result


ic(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
ic(merge([[1, 4], [4, 5]]))
ic(merge([[1, 3], [2, 6], [8, 10], [8, 18]]))
