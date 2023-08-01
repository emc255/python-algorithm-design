"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
1 <= n <= 20
1 <= k <= n

"""


def combine(n: int, k: int) -> list:
    result = []
    combine_helper(n, k, 1, [], result)
    return result


def combine_helper(n: int, k: int, start_index: int, temp_combinations: list, result: list):
    if len(temp_combinations) == k:
        result.append(temp_combinations[:])
        return

    for i in range(start_index, n + 1):
        temp_combinations.append(i)
        combine_helper(n, k, i + 1, temp_combinations, result)
        temp_combinations.pop()


print(combine(4, 3))
