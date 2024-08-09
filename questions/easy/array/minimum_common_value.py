"""
2540. Minimum Common Value

Given two integer arrays nums1 and nums2,
sorted in non-decreasing order,
return the minimum integer common to both arrays.
If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2
if both arrays have at least one occurrence of that integer.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to
both arrays is 2, so we return 2.

Example 2:
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements
in the array 2 and 3 out of which 2 is the smallest,
so 2 is returned.


Constraints:
1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.

"""
from icecream import ic


def get_common(nums1: list[int], nums2: list[int]) -> int:
    n1_index = 0
    n2_index = 0

    while n1_index < len(nums1) and n2_index < len(nums2):
        if nums1[n1_index] == nums2[n2_index]:
            return nums1[n1_index]

        if nums1[n1_index] > nums2[n2_index]:
            n2_index += 1
        else:
            n1_index += 1

    return -1


ic(get_common([1, 2, 3, 6], [2, 3, 4, 5]))
