"""
Subsets

Given an integer array nums of unique elements, return all possible
subsets (the power set).
The solution set must not contain duplicate subsets.
Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

"""
from icecream import ic


def subsets(nums: list[int]) -> list[list[int]]:
    result = [[]]

    def dp(i, combinations):
        if new_amount == 0:
            found = tuple(sorted(list(combinations)))
            changes.add(found)

        for num in nums:
            combinations.append(coin)
            dp(num, combinations)
            combinations.pop()

    changes = set()
    dp(0, [])


ic(subsets([1, 2, 3]))
