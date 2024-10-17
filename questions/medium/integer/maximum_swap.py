"""
670. Maximum Swap

You are given an integer num. You can swap two digits
at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.

Constraints:
0 <= num <= 108

"""
from collections import defaultdict

from icecream import ic


def maximum_swap(num: int) -> int:
    result = []
    digits = [int(d) for d in str(num)]
    index_digits = defaultdict(list)

    for i, n in enumerate(digits):
        index_digits[n].append(i)

    sorted_digits = sorted(digits, reverse=True)

    i = 0
    low_index = -1
    high_index = -1
    high = -1
    low = -1
    while i < len(digits):
        if sorted_digits[i] > digits[i]:
            low = digits[i]
            low_index = i
            high = sorted_digits[i]
            high_index = (index_digits[sorted_digits[i]][-1])
            break
        i += 1

    i = 0
    while i < len(digits):
        if i == high_index:
            result.append(low)
        elif i == low_index:
            result.append(high)
        else:
            result.append(digits[i])
        i += 1

    return int(''.join(map(str, result)))


def maximum_swap_v2(num: int) -> int:
    digits = [int(d) for d in str(num)]
    last_occurrence = {d: i for i, d in enumerate(digits)}

    # Loop through each digit and find the first position where a higher digit exists later in the number
    for i, digit in enumerate(digits):
        # Check digits in descending order from 9 to current digit
        for d in range(9, digit, -1):
            if d in last_occurrence and last_occurrence[d] > i:
                # Swap the current digit with the later higher digit
                digits[i], digits[last_occurrence[d]] = digits[last_occurrence[d]], digits[i]
                # Convert the list back to an integer and return
                return int(''.join(map(str, digits)))

    # If no swap was made, return the original number
    return num


ic(maximum_swap(num=2736))
ic(maximum_swap_v2(num=98368))
