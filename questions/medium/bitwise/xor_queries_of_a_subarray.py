"""
1310. XOR Queries of a Subarray

You are given an array arr of positive integers.
You are also given the array queries where queries[i] = [left[i], right[i]].

For each query i compute the XOR of elements from left[i]
to right[i] (that is, arr[left[i]] XOR arr[left[i] + 1] XOR ... XOR arr[right[i]] ).

Return an array answer where answer[i] is the answer to the ith query.

Example 1:
Input:
arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8]
Explanation:
The binary representation of the elements in the array are:
1 = 0001
3 = 0011
4 = 0100
8 = 1000
The XOR values for queries are:
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8

Example 2:
Input:
arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]

Constraints:
1 <= arr.length, queries.length <= 3 * 104
1 <= arr[i] <= 109
queries[i].length == 2
0 <= left[i] <= right[i] < arr.length

"""
from icecream import ic


def xor_queries(arr: list[int], queries: list[list[int]]) -> list[int]:
    result = []
    for start, end in queries:
        numbers = arr[start: end + 1]
        xor = numbers[0]
        for i in range(1, len(numbers)):
            xor ^= numbers[i]
        result.append(xor)
    return result


def xor_queries_v2(arr: list[int], queries: list[list[int]]) -> list[int]:
    # Step 1: Precompute the prefix XOR array
    prefix_xor = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

    # Step 2: Process each query
    result = []
    for start, end in queries:
        # XOR from start to end is prefix[end + 1] ^ prefix[start]
        result.append(prefix_xor[end + 1] ^ prefix_xor[start])

    return result


ic(xor_queries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))
ic(xor_queries_v2([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]))
