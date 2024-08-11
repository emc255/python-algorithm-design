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
    # If there's only one row, the zigzag pattern is just the original string.
    if num_rows == 1:
        return s

    result = ""  # This will hold the final zigzag-converted string.

    # Iterate over each row in the zigzag pattern.
    for r in range(num_rows):
        # The 'increment' is the distance between characters in the same column.
        increment = 2 * (num_rows - 1)

        # Start iterating over the string from the current row's start point.
        for i in range(r, len(s), increment):
            # Add the character from the current column of the zigzag pattern.
            result += s[i]

            # Calculate the index of the character in the middle of the zigzag.
            middle_increment = i + increment - (2 * r)

            # For all rows except the first and last, add the middle character.
            if 0 < r < num_rows - 1 and middle_increment < len(s):
                result += s[middle_increment]

    return result


ic(convert("PAYPALISHIRING", 3))
