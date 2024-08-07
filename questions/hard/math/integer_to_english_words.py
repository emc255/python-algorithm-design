"""
Integer to English Words

Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output:
"Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output:
"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:
0 <= num <= 231 - 1

"""
from icecream import ic


def number_to_words(num: int) -> str:
    def get_string(n):
        temp = []
        hundreds = n // 100
        if hundreds:
            temp.append(number_words[hundreds] + " Hundred")

        last_two_digits = n % 100
        if last_two_digits >= 20:
            tens = (last_two_digits // 10) * 10
            ones = last_two_digits % 10
            temp.append(number_words[tens])
            if ones:
                temp.append(number_words[ones])
        elif last_two_digits:
            temp.append(number_words[last_two_digits])
        return " ".join(temp)

    if num == 0:
        return "Zero"

    result = []
    number_words = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
    }
    number_scales = ["", " Thousand", " Million", " Billion"]
    i = 0
    while num:
        digits = num % 1000
        s = get_string(digits)
        if s:
            result = [s + number_scales[i]] + result
        i += 1
        num //= 1000

    return " ".join(result)


def number_to_words_v2(num: int) -> str:
    def helper(number):
        if number < 20:
            s = belowTwenty[number]
        elif number < 100:
            s = tens[num // 10] + ' ' + belowTwenty[number % 10]
        elif number < 1000:
            s = helper(number // 100) + ' Hundred ' + helper(number % 100)
        elif number < 1000000:
            s = helper(number // 1000) + ' Thousand ' + helper(number % 1000)
        elif number < 1000000000:
            s = helper(number // 1000000) + ' Million ' + helper(number % 1000000)
        else:
            s = helper(number // 1000000000) + ' Billion ' + helper(number % 1000000000)

        return s.strip()

    if num == 0:
        return 'Zero'

    belowTwenty = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                   'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                   'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
            'Seventy', 'Eighty', 'Ninety']

    return helper(num)


ic(number_to_words(12345))
ic(number_to_words(42))
ic(number_to_words(1000000))

ic(number_to_words_v2(1102506))
