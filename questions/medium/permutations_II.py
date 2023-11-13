"""
46. Permutations

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from icecream import ic


def permute_unique(nums: list) -> list:
    def dfs(combinations, n):
        if not n:
            result.add(tuple(combinations))
            return
        for i in range(len(n)):
            dfs(combinations + [n[i]], n[:i] + n[i + 1:])

    result = set()
    dfs([], nums)
    return list(result)


ic(permute_unique([1, 1, 2]))
