"""
1442. Count Triplets That Can Form Two Arrays of Equal XOR

Given an array of integers arr.
We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
Let's define a and b as follows:
a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.
Return the number of triplets (i, j and k) Where a == b.

Example 1:
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:
Input: arr = [1,1,1,1,1]
Output: 10

Constraints:
1 <= arr.length <= 300
1 <= arr[i] <= 108

"""
from icecream import ic


def count_triplets(arr: list[int]) -> int:
    prefix_xor = [0] + arr[:]
    size = len(prefix_xor)

    # Perform XOR on consecutive elements in the modified array
    for i in range(1, size):
        prefix_xor[i] ^= prefix_xor[i - 1]

    count = 0
    ic(prefix_xor)
    # Iterate through the modified array to count triplets
    for start in range(size):
        for end in range(start + 1, size):
            if prefix_xor[start] == prefix_xor[end]:
                # Increment the result by the count of valid triplets
                count += end - start - 1

    return count


ic(count_triplets([2, 3, 1, 6, 7]))
