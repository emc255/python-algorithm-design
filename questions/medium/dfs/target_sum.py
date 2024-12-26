"""
494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of
the symbols '+' and '-' before each integer in nums and then
concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-'
before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build,
which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation:
There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

"""
from icecream import ic


def find_target_sum_ways(nums: list[int], target: int) -> int:
    def dfs(i, current_sum):
        # Base case: Reached the end of the array
        if i == len(nums):
            return 1 if current_sum == target else 0

        # Recursive calls: include nums[i] as positive and negative
        add = dfs(i + 1, current_sum + nums[i])
        subtract = dfs(i + 1, current_sum - nums[i])

        return add + subtract

    return dfs(0, 0)


def find_target_sum_ways_v2(nums: list[int], target: int) -> int:
    total_sum = sum(nums)

    if (target + total_sum) % 2 != 0 or target > total_sum or target < -total_sum:
        return 0

    subset_sum = (target + total_sum) // 2

    dp = [0] * (subset_sum + 1)
    dp[0] = 1

    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[subset_sum]


ic(find_target_sum_ways(nums=[1, 1, 1, 1, 1], target=3))
