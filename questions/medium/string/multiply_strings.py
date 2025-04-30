"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert
the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero,
except the number 0 itself.

"""
from icecream import ic


def multiply(num1: str, num2: str) -> str:
    def string_to_int(arr: str) -> int:
        number = 0
        for c in arr:
            number = number * 10 + (ord(c) - ord("0"))
        return number

    def int_to_string(digit: int) -> str:
        res = []
        while digit > 0:
            r = digit % 10
            if r == 0:
                res.append("0")
            else:
                res.append(chr(ord("0") + r))
            digit //= 10

        return "".join(res[::-1])

    n1 = string_to_int(num1)
    n2 = string_to_int(num2)
    total = n1 * n2
    return int_to_string(total)


ic(multiply(num1="123", num2="456"))
