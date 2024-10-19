"""
1545. Find Kth Bit in Nth Binary String

Given two positive integers n and k,
the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns
the reversed string x, and invert(x) inverts all the bits
in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:
S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid
for the given n.

Example 1:
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".

Example 2:
Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".

Constraints:
1 <= n <= 20
1 <= k <= 2n - 1

"""
from icecream import ic


def find_kth_bit(n: int, k: int) -> str:
    def invert_bits(s: str) -> str:
        inverted = ""
        for bit in s:
            inverted += "1" if bit == "0" else "0"
        return inverted

    n = n - 1
    result = "0"

    while n > 0:
        temp = result
        result += "1"
        result += invert_bits(temp)[::-1]
        n -= 1

    return result[k - 1]


def find_kth_bit_v2(n: int, k: int) -> str:
    # Recursive function to find the k-th bit in the nth binary string
    def find_bit(n: int, k: int) -> str:
        # Base case: if we are at S1, the string is simply "0"
        if n == 1:
            return "0"

        length = (1 << n) - 1  # Length of Sn is 2^n - 1
        mid = length // 2 + 1  # Mid-point is (2^n)//2

        if k == mid:
            return "1"  # The middle bit is always '1' for all n
        elif k < mid:
            return find_bit(n - 1, k)  # Look in the left half (S_{n-1})
        else:
            # If k is in the right half, calculate its mirrored position in S_{n-1}
            mirror_pos = length - k + 1
            # Invert the result of the mirrored position from the left half
            return "1" if find_bit(n - 1, mirror_pos) == "0" else "0"

    # Call the recursive function
    return find_bit(n, k)


ic(find_kth_bit(n=3, k=1))
