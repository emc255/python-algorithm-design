"""
1497. Check If Array Pairs Are Divisible by k

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that
the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

Example 1:
Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation:
Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

Example 2:
Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation:
Pairs are (1,6),(2,5) and(3,4).

Example 3:
Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation:
You can try all possible pairs to see that there is no way to
divide arr into 3 pairs each with sum divisible by 10.

Constraints:
arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105

"""
from icecream import ic


def can_arrange(arr: list[int], k: int) -> bool:
    # Frequency array to count remainders
    remainder_count = [0] * k

    # Count remainders when each element is divided by k
    for num in arr:
        remainder = num % k
        if remainder < 0:
            remainder += k  # Handle negative numbers
        remainder_count[remainder] += 1
    ic(remainder_count)
    # Check if the array can be paired as per the conditions
    for i in range(k):
        if i == 0:  # Remainder 0 case: must have even count
            if remainder_count[i] % 2 != 0:
                return False
        else:  # General case: count[i] should match count[k-i]
            if remainder_count[i] != remainder_count[k - i]:
                return False

    return True


def can_arrange_v2(arr: list[int], k: int) -> bool:
    return (sum(arr) % k == 0) and min(arr) < k / 2 < max(arr)


ic(can_arrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))
