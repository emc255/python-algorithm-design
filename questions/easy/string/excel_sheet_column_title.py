"""
168. Excel Sheet Column Title

Given an integer columnNumber,
return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
1 <= columnNumber <= 231 - 1

"""
from icecream import ic


def convert_to_title(column_number: int) -> str:
    result = []
    while column_number:
        column_number, remainder = divmod(column_number - 1, 26)
        result.append(chr(65 + remainder))
    return ''.join(reversed(result))


ic(convert_to_title(701))
