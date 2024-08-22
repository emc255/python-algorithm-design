"""
476. Number Complement

The complement of an integer is the integer you get
when you flip all the 0's to 1's and all the 1's to 0's in
its binary representation.

For example, The integer 5 is "101" in binary
and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:
Input: num = 5
Output: 2
Explanation:
The binary representation of 5 is 101 (no leading zero bits),
and its complement is 010. So you need to output 2.

Example 2:
Input: num = 1
Output: 0
Explanation:
The binary representation of 1 is 1 (no leading zero bits),
and its complement is 0. So you need to output 0.

Constraints:
1 <= num < 231

"""
from icecream import ic


def find_complement(num: int) -> int:
    # Create a bitmask with all bits set to 1 for the length of the binary representation of num
    bitmask = (1 << num.bit_length()) - 1
    # XOR the number with the bitmask to get the complement
    return num ^ bitmask


def find_complement_v2(num: int) -> int:
    str_num = bin(num)[2:]
    binary_string = []
    for i in range(len(str_num)):
        if str_num[i] == "1":
            binary_string.append("0")
        else:
            binary_string.append("1")

    return int("".join(binary_string), 2)


ic(find_complement(500))
