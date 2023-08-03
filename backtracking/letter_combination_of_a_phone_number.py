"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""


def letter_combinations(digits: str):
    def backtrack(index, prefix):
        if len(prefix) == len(digits):
            result.append(prefix)
            return

        key = digits[index]
        for letter in phone.get(key):
            backtrack(index + 1, prefix + letter)

    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "prqs",
        "8": "tuv",
        "9": "wxyz"
    }
    result = []

    if digits:
        backtrack(0, "")

    return result


print(letter_combinations("25"))
