"""
815. Bus Routes

You are given an array routes representing bus routes
where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7],
this means that the 0th bus travels in
the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially),
and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target.
Return -1 if it is not possible.

Example 1:
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7,
then take the second bus to the bus stop 6.

Example 2:
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

Constraints:
1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106

"""
import heapq
from collections import defaultdict

from icecream import ic


def number_of_buses_to_destination(routes: list[list], source: int, target: int) -> int:
    graph = defaultdict(list)
    for route in routes:
        for stop in route:
            temp = list(route)  # Use list() to create a new list
            temp.remove(stop)
            graph[stop].append(temp)

    heap = [(0, source, [source])]
    while heap:
        r, curr_node, visited = heapq.heappop(heap)
        if curr_node == target:
            return r
        for next_stop in graph[curr_node]:
            for ss in next_stop:
                if ss not in visited:
                    heapq.heappush(heap, (r + 1, ss, visited + [ss]))

    return -1


def number_of_buses_to_destination_v2(routes: list[list], source: int, target: int) -> int:
    if source == target:
        return 0

    max_stop = max(max(route) for route in routes)
    if max_stop < target:
        return -1

    n = len(routes)
    min_buses_to_reach = [float('inf')] * (max_stop + 1)
    min_buses_to_reach[source] = 0

    flag = True
    while flag:
        flag = False
        for route in routes:
            mini = float('inf')
            for stop in route:
                mini = min(mini, min_buses_to_reach[stop])
            mini += 1
            for stop in route:
                if min_buses_to_reach[stop] > mini:
                    min_buses_to_reach[stop] = mini
                    flag = True

    return min_buses_to_reach[target] if min_buses_to_reach[target] < float('inf') else -1


ic(number_of_buses_to_destination_v2([[1, 2, 7], [3, 6, 7]], 1, 6))
