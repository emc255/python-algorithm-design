"""
592. Fraction Addition and Subtraction

Given a string expression representing an expression of fraction
addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer,
change it to the format of a fraction that has a denominator 1.
So in this case, 2 should be converted to 2/1.

Example 1:
Input: expression = "-1/2+1/2"
Output: "0/1"

Example 2:
Input: expression = "-1/2+1/2+1/3"
Output: "1/3"

Example 3:
Input: expression = "1/3-1/2"
Output: "-1/6"


Constraints:
The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator.
If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator
and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1,
it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid
and in the range of 32-bit int.

"""
import math
from functools import reduce

from icecream import ic


def fraction_addition(expression: str) -> str:
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    def lcm_of_list(numbers):
        return reduce(lcm, numbers)

    fractions = []
    denominators = []

    # Split the expression into individual fractions
    parts = expression.replace('-', '+-').split('+')
    ic(parts)
    for part in parts:
        if part:
            numerator, denominator = map(int, part.split('/'))
            denominators.append(denominator)
            fractions.append((numerator, denominator))

    # Calculate the least common denominator (LCD)
    LCD = lcm_of_list(denominators)

    # Adjust all numerators to have the same denominator (LCD)
    numerators = [num * (LCD // den) for num, den in fractions]

    # Sum all the adjusted numerators
    total_numerator = sum(numerators)

    # Simplify the resulting fraction
    gcd = math.gcd(total_numerator, LCD)
    simplified_numerator = total_numerator // gcd
    simplified_denominator = LCD // gcd

    return f"{simplified_numerator}/{simplified_denominator}"


ic(fraction_addition("-1/2+1/2+1/3"))
ic(fraction_addition("1/2+1/2+1/3"))
ic(fraction_addition("-1/3+1/4-1/5+1/6-1/7+1/8-1/9+1/10-1/11+1/12"))
