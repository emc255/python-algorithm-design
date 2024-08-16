"""
Maximum Distance in Arrays

You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one)
and calculate the distance. We define the distance
between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

Example 1:
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in
the first or third array and pick 5 in the second array.

Example 2:
Input: arrays = [[1],[1]]
Output: 0


Constraints:
m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.

"""
from icecream import ic


def max_distance(arrays: list[list[int]]) -> int:
    min1, max1 = arrays[0][0], arrays[0][-1]
    result = 0
    for i in range(1, len(arrays)):
        result = max(
            result,
            max(arrays[i][-1] - min1, max1 - arrays[i][0])
        )
        min1 = min(min1, arrays[i][0])
        max1 = max(max1, arrays[i][-1])
    return result


def max_distance_v2(arrays: list[list[int]]) -> int:
    minimum_numbers = []
    maximum_numbers = []
    for i, array in enumerate(arrays):
        minimum_numbers.append([i, min(array)])
        maximum_numbers.append([i, max(array)])

    result = 0
    for i, m in maximum_numbers:
        for j, n in minimum_numbers:
            if i != j:
                result = max(result, abs(m - n))
    return result


ic(max_distance([[1, 4], [0, 5]]))
ic(max_distance([[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]]))
