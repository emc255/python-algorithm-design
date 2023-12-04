"""
2264. Largest 3-Same-Digit Number in String

You are given a string num representing a large integer.
An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:
A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.

Example 1:
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Example 2:
Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.

Example 3:
Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit.
Therefore, there are no good integers.

Constraints:
3 <= num.length <= 1000
num only consists of digits.

"""
from icecream import ic


def largest_good_integer(num: str) -> str:
    l, r, n = 0, 1, len(num)
    ans = -1
    while l < n:
        while r < n and num[l] == num[r]:
            r += 1
        if r - l >= 3:
            ans = int(num[l]) if ans < int(num[l]) else ans
            l = r - 1
        l += 1
    return str(ans) * 3 if ans > -1 else ""


ic(largest_good_integer("6777133339"))
ic(largest_good_integer("444818042931906802860005960222213336669500011846936171709111"))
