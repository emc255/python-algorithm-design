"""
1106. Parsing A Boolean Expression

A boolean expression is an expression that evaluates to either true or false.
It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of
the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of
the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression,
return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

Example 1:
Input: expression = "&(|(f))"
Output: false
Explanation:
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

Example 2:
Input: expression = "|(f,f,f,t)"
Output: true
Explanation:
The evaluation of (false OR false OR false OR true) is true.

Example 3:
Input: expression = "!(&(f,t))"
Output: true
Explanation:
First, evaluate &(f,t) --> (false AND true) --> false --> f.
The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.


Constraints:
1 <= expression.length <= 2 * 104
expression[i] is one following characters:
'(', ')', '&', '|', '!', 't', 'f', and ','.

"""

from icecream import ic


def parse_bool_expression(expression: str) -> bool:
    def evaluate():
        nonlocal index
        operator = expr[index]
        index += 1

        if operator == "t":  # True literal
            return True
        if operator == "f":  # False literal
            return False
        if operator == "!":  # NOT operation
            index += 1  # Skip opening parenthesis
            result = not evaluate()  # Evaluate the inner expression and negate
            index += 1  # Skip closing parenthesis
            return result

        # AND or OR operations
        values = []
        index += 1
        while expr[index] != ")":  # Process until the closing parenthesis
            if expr[index] != ",":  # Skip commas
                values.append(evaluate())  # Recursively evaluate inner expressions
            else:
                index += 1  # Move past the comma
        index += 1  # Skip the closing parenthesis

        # Return the result of AND or OR operation
        if operator == "&":  # AND operation
            return all(values)
        if operator == "|":  # OR operation
            return any(values)

    expr = expression  # Rename to 'expr' for better readability
    index = 0  # Use 'index' instead of 'i' for clarity

    return evaluate()


ic(parse_bool_expression(expression="&(|(f))"))
