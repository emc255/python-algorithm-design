"""
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

"""
from icecream import ic


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    result = ""
    for r in range(num_rows):
        increment = 2 * (num_rows - 1)

        for i in range(r, len(s), increment):
            result += s[i]
            middle_increment = i + increment - 2 * r
            if 0 < r < num_rows - 1 and middle_increment < len(s):
                result += s[middle_increment]
    return result


ic(convert("PAYPALISHIRING", 3))
