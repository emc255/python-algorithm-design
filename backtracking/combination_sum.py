"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique
combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    def backtracking(new_target, combination: list[int]):
        if new_target == 0:
            sorted_list_descending = sorted(combination, reverse=True)
            if sorted_list_descending not in result:
                result.append(sorted_list_descending)
            return

        if new_target < 0:
            return

        for candidate in candidates:
            remainder = new_target - candidate
            combination.append(candidate)
            backtracking(remainder, combination)
            combination.pop()

    result = []
    backtracking(target, [])
    return result


def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    dfs(candidates, target, [], result)
    return result


def dfs(nums, target, path, result):
    if target < 0:
        # backtracking
        return
    if target == 0:
        result.append(path)
        return
    for i in range(len(nums)):
        dfs(nums[i:], target - nums[i], path + [nums[i]], result)


print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([8, 7, 4, 3], 11))

print(combination_sum2([2, 3, 6, 7], 7))
print(combination_sum2([8, 7, 4, 3], 11))
