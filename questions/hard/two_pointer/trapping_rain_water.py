"""
Trapping Rain Water

Given n non-negative integers representing
an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section)
is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""
from icecream import ic


def trap(height: list[int]) -> int:
    total_water = 0
    left = 0
    right = len(height) - 1
    max_left = height[left]
    max_right = height[right]

    while left < right:
        if max_left > max_right:
            right -= 1
            max_right = max(max_right, height[right])
            total_water += max_right - height[right]
        else:
            left += 1
            max_left = max(max_left, height[left])
            total_water += max_left - height[left]

    return total_water


ic(trap([4, 2, 0, 3, 2, 5]))
