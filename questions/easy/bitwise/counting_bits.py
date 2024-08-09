"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:
0 <= n <= 105

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n).
Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

"""
from icecream import ic


def count_bits(n: int) -> list:
    result = []
    for i in range(n + 1):
        string_bit = bin(i)[2:]
        counter = 0
        for j in range(len(string_bit)):
            if string_bit[j] == '1':
                counter += 1
        result.append(counter)
    return result


"""
0   1   10
0   1   1

"""


def count_bits_v2(n: int) -> list:
    result = []
    dp = [0]
    for i in range(n + 1):
        string_bit = bin(i)[2:]
        counter = 0
        for j in range(len(string_bit)):
            if string_bit[j] == '1':
                counter += 1
        result.append(counter)
    return result


ic(count_bits(5))
