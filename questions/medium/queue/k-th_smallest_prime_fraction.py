"""
K-th Smallest Prime Fraction

You are given a sorted integer array arr containing 1 and prime numbers,
where all the integers of arr are unique.
You are also given an integer k.

For every i and j where 0 <= i < j < arr.length,
we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered.
Return your answer as an array of integers of size 2,
where answer[0] == arr[i] and answer[1] == arr[j].

Example 1:
Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

Example 2:
Input: arr = [1,7], k = 1
Output: [1,7]

Constraints:
2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 104
arr[0] == 1
arr[i] is a prime number for i > 0.
All the numbers of arr are unique and sorted in strictly increasing order.
1 <= k <= arr.length * (arr.length - 1) / 2

Follow up: Can you solve the problem with better than O(n2) complexity?

"""
import heapq

from icecream import ic


def kth_smallest_prime_fraction(arr: list[int], k: int) -> list[int]:
    N = len(arr)
    pq = []
    for i in range(N):
        for j in range(i + 1, N):
            heapq.heappush(pq, (arr[i] / arr[j], (arr[i], arr[j])))
    for i in range(k - 1):
        heapq.heappop(pq)
    return heapq.heappop(pq)[1]


def kth_smallest_prime_fraction_v2(arr: list[int], k: int) -> list[int]:
    def con(value):
        nb_smallest_fraction = 0
        numer = arr[0]
        denom = arr[-1]

        slow = 0
        for fast in range(1, len(arr)):
            while slow < fast and arr[slow] / arr[fast] < value:
                if arr[slow] / arr[fast] > numer / denom:
                    numer, denom = arr[slow], arr[fast]

                slow += 1

            nb_smallest_fraction += slow

        return nb_smallest_fraction, numer, denom

    l = arr[0] / arr[-1]
    r = 1

    while l < r:
        m = (l + r) / 2

        count, numer, denom = con(m)

        if count == k:
            return [numer, denom]

        if count > k:
            r = m
        else:
            l = m


ic(kth_smallest_prime_fraction([1, 2, 3, 5], 3))
