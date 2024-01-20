"""
Sum of Subarray Minimums

Given an array of integers arr,
find the sum of min(b),
where b ranges over every (contiguous) subarray of arr.
Since the answer may be large, return the answer modulo 109 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Sub-arrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444

Constraints:
1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104

"""
from icecream import ic


def sum_subarray_minimum(arr: list[int]) -> int:
    mod = 10 ** 9 + 7
    result = 0
    stack = []

    for i in range(len(arr)):
        while stack and arr[i] < stack[-1][1]:
            index, value = stack.pop()
            left = index - stack[-1][0] if stack else index + 1
            right = i - index
            result += value * left * right
        stack.append((i, arr[i]))

    for i in range(len(stack)):
        index, value = stack[i]
        left = index - stack[i - 1][0] if i > 0 else index + 1
        right = len(arr) - index
        result += value * left * right % mod

    return result


def sum_subarray_minimum_v2(arr: list[int]) -> int:
    mod = 10 ** 9 + 7
    result = 0
    arr = [float('-inf')] + arr + [float('-inf')]
    stack = []

    for i in range(len(arr)):
        while stack and arr[i] < stack[-1][1]:
            index, value = stack.pop()
            left = index - stack[-1][0] if stack else index + 1
            right = i - index
            result += value * left * right % mod
        stack.append((i, arr[i]))

    return result


ic(sum_subarray_minimum([3, 1, 2, 4]))
ic(sum_subarray_minimum_v2([3, 1, 2, 4]))
