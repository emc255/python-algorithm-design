"""
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3],
the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array
are sorted in one container according to their lexicographical order,
then the next permutation of that array is the permutation that follows it in the sorted container.
If such arrangement is not possible,
the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1]
does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

"""
from icecream import ic


def next_permutation(nums: list) -> None:
    n = len(nums)
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i + 1] > nums[i]:
            pivot = i
            break

    if pivot == -1:
        return nums.sort()

    for i in range(n - 1, pivot, -1):
        if nums[pivot] < nums[i]:
            nums[pivot], nums[i] = nums[i], nums[pivot]
            break

    nums[pivot + 1:] = sorted(nums[pivot + 1:])
    ic(nums)


def next_permutation_v2(nums: list) -> None:
    n = len(nums)
    pivot = -1
    for i in range(n - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            pivot = i
            break

    if pivot == -1:
        return nums.sort()

    swap = n - 1
    while nums[pivot - 1] >= nums[swap]:
        swap -= 1

    nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]
    nums[pivot:] = sorted(nums[pivot:])
    ic(nums)


ic(next_permutation([1, 2, 3]))
ic(next_permutation([1, 1, 5]))
ic(next_permutation([1, 3, 2]))
ic(next_permutation([1, 3, 5, 4, 3, 2, 1]))

ic(next_permutation_v2([1, 3, 5, 4, 3, 2, 1]))
