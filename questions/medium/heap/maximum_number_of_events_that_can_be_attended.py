"""
1353. Maximum Number of Events That Can Be Attended

You are given an array of events
where events[i] = [startDayi, endDayi].
Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d
where startTimei <= d <= endTimei. You can only attend
one event at any time d.

Return the maximum number of events you can attend.

Example 1:
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation:
You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:
Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Constraints:
1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105

"""
from _heapq import heappush, heappop

from icecream import ic


def max_events(events: list[list[int]]) -> int:
    events.sort()  # Sort by start day
    min_heap = []
    day = 0
    i = 0
    n = len(events)
    result = 0

    while i < n or min_heap:
        # If no active events, jump to the next event's start day
        if not min_heap:
            day = events[i][0]

        # Add all events starting today or earlier
        while i < n and events[i][0] <= day:
            heappush(min_heap, events[i][1])  # Push end day
            i += 1

        # Remove expired events
        while min_heap and min_heap[0] < day:
            heappop(min_heap)

        # Attend the event with the earliest end day
        if min_heap:
            heappop(min_heap)
            result += 1
            day += 1  # Move to the next day

    return result


ic(max_events(events=[[1, 2], [2, 3], [3, 4], [1, 2]]))
