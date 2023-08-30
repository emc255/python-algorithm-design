"""
2616. Minimize the Maximum Difference of Pairs

You are given a 0-indexed integer array nums and an integer p.
Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized.
Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j,
the difference of this pair is |nums[i] - nums[j]|,
where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs.
We define the maximum of an empty set to be zero.

Example 1:
Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4,
and the second pair is formed from the indices 2 and 5.
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1.
Therefore, we return 1.

Example 2:
Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair.
The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= p <= (nums.length)/2

"""


def minimize_max(nums: list, p: int) -> int:
    def has_enough_pairs(avg_diff) -> bool:
        count = 0
        i = 0
        while i < len(nums) - 1 and count < p:
            if nums[i + 1] - nums[i] <= avg_diff:
                count += 1
                i += 2
            else:
                i += 1

        return count >= p

    nums.sort()
    left_bound = 0
    right_bound = nums[-1] - nums[0]

    while left_bound < right_bound:
        average_difference = (left_bound + right_bound) // 2
        if has_enough_pairs(average_difference):
            right_bound = average_difference
        else:
            left_bound = average_difference + 1

    return left_bound


def quick_sort(numbers: list) -> list:
    if len(numbers) <= 1:
        return numbers

    mid = numbers[0 + len(numbers) // 2]

    left = [number for number in numbers if number < mid]
    mid_array = [number for number in numbers if number == mid]
    right = [number for number in numbers if number > mid]

    return quick_sort(left) + mid_array + quick_sort(right)


print(minimize_max([10, 1, 2, 7, 1, 3], 2))
print(minimize_max([4, 2, 1, 2], 1))
print(minimize_max([3, 4, 2, 3, 2, 1, 2], 3))
