"""
2094. Finding 3-Digit Even Numbers

You are given an integer array digits,
where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:
The integer consists of the concatenation of three elements
from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.

For example, if the given digits were [1, 2, 3],
integers 132 and 312 follow the requirements.
Return a sorted array of the unique integers.

Example 1:
Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation:
All the possible integers that follow the requirements are in the output array.
Notice that there are no odd integers or integers with leading zeros.

Example 2:
Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation:
The same digit can be used as many times as it appears in digits.
In this example, the digit 8 is used twice each time in 288, 828, and 882.

Example 3:
Input: digits = [3,7,5]
Output: []
Explanation:
No even integers can be formed using the given digits.

Constraints:
3 <= digits.length <= 100
0 <= digits[i] <= 9

"""
from collections import Counter

from icecream import ic


def find_even_numbers(digits: list[int]) -> list[int]:
    res = set()

    for i in range(len(digits)):
        for j in range(len(digits)):
            if i == j:
                continue
            for k in range(len(digits)):
                if j == k or i == k:
                    continue
                n = digits[i] * 100 + digits[j] * 10 + digits[k]
                if n % 2 == 0 and n >= 100:
                    res.add(n)
    a = list(res)
    a.sort()
    return a


def find_even_numbers_v2(digits: list[int]) -> list[int]:
    digits_counter = Counter(map(str, digits))

    def is_possible(n):
        num = Counter(str(n))
        return num == (num & digits_counter)

    output = list(filter(is_possible, range(100, 1000, 2)))

    return output


ic(find_even_numbers(digits=[2, 1, 3, 0]))
ic(find_even_numbers_v2(digits=[2, 2, 8, 8, 2]))
ic(find_even_numbers(digits=[3, 7, 5]))
