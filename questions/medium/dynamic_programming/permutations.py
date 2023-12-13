"""
46. Permutations

Given an numsay nums of distinct integers,
return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""
from icecream import ic


def permute(nums: list) -> list:
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums.copy())
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


def permute_v2(nums: list) -> list:
    def dfs(combination, n):
        if not n:
            result.append(combination[:])
            return

        for i in range(len(n)):
            dfs(combination + [n[i]], n[:i] + n[i + 1:])

    result = []
    dfs([], nums)

    return result


ic(permute_v2([1, 2, 3]))
