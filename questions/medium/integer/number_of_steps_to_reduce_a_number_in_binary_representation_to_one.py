"""
1404. Number of Steps to Reduce a Number in Binary Representation to One

Given the binary representation of an integer as a string s,
return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.
If the current number is odd, you have to add 1 to it.
It is guaranteed that you can always reach one for all test cases.

Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14.
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.
Step 5) 4 is even, divide by 2 and obtain 2.
Step 6) 2 is even, divide by 2 and obtain 1.

Example 2:
Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.

Example 3:
Input: s = "1"
Output: 0

Constraints:
1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'

"""
from icecream import ic


def number_steps(s: str) -> int:
    result = 0
    carry = 0
    for i in range(len(s) - 1, 0, -1):
        x = int(s[i]) + carry
        if x % 2 == 0:
            result += 1
        elif x % 2 == 1:
            carry = 1
            result += 2

    return result + carry


def number_steps_v2(s: str) -> int:
    c = 0
    target = int(s, 2)

    while target != 1:
        c += 1
        if target % 2 == 0:
            target = target // 2
        else:
            target += 1
    return c


ic(number_steps("1101"))
ic(number_steps("10"))
