"""
1980. Find Unique Binary String

Given an array of strings nums containing n unique binary strings each of length n,
return a binary string of length n that does not appear in nums.
If there are multiple answers, you may return any of them.

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Constraints:
n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.

"""
from icecream import ic


def find_different_binary_string(nums: list) -> str:
    def backtrack(answer):
        if len(answer) == answer_length and answer not in numbers:
            return answer
        if len(answer) < answer_length:
            return backtrack(answer + "0") or backtrack(answer + "1")
        return ""

    answer_length = len(nums[0])
    numbers = set(nums)
    return backtrack("")


ic(find_different_binary_string(["01", "10"]))
