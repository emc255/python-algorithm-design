"""
241. Different Ways to Add Parentheses

Given a string expression of numbers and operators,
return all possible results from computing all the different possible
ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit
in a 32-bit integer and the number of different results does not exceed 104.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

"""
from icecream import ic


def different_ways_to_compute(expression):
    memo = {}

    def helper(expr):
        if expr in memo:
            return memo[expr]

        if expr.isdigit():
            return [int(expr)]

        results = []
        for i, char in enumerate(expr):
            if char in "+-*":
                left_results = helper(expr[:i])
                right_results = helper(expr[i + 1:])

                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        elif char == '*':
                            results.append(left * right)

        memo[expr] = results
        return results

    return helper(expression)


ic(different_ways_to_compute("2*3-4*5"))
