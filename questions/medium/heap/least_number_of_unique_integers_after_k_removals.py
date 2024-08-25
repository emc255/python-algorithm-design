"""
1481. Least Number of Unique Integers after K Removals

Given an array of integers arr and an integer k.
Find the least number of unique integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s.
1 and 3 will be left.

Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length

"""
import heapq
from collections import Counter

from icecream import ic


def find_least_num_of_unique_ints(arr: list[int], k: int) -> int:
    result = []
    frequency = Counter(arr)
    values = sorted(frequency.values())
    for value in values:
        if k >= value:
            k -= value
        else:
            result.append(value)

    return len(result)


def find_least_num_of_unique_ints_v2(arr: list[int], k: int) -> int:
    frequency = Counter(arr)
    heap = list(frequency.values())
    result = len(heap)
    heapq.heapify(heap)
    while k > 0 and heap:
        f = heapq.heappop(heap)
        if k >= f:
            k -= f
            result -= 1

    return result


ic(find_least_num_of_unique_ints([4, 3, 1, 1, 3, 3, 2], 3))
ic(find_least_num_of_unique_ints_v2([5, 5, 4], 1))
