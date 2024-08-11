"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove
the minimum number of parentheses ( '(' or ')',
in any positions ) so that the resulting parentheses string
is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:
1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.

"""
from icecream import ic


def min_remove_to_make_valid(s: str) -> str:
    open_parenthesis = 0
    result = []

    # First pass: Remove excess closing parentheses
    for c in s:
        if c == "(":
            open_parenthesis += 1
        elif c == ")":
            if open_parenthesis == 0:
                continue  # Skip this closing parenthesis
            open_parenthesis -= 1
        result.append(c)

    # Second pass: Remove excess opening parentheses
    final_result = []
    for c in reversed(result):
        if c == "(" and open_parenthesis > 0:
            open_parenthesis -= 1
            continue
        final_result.append(c)

    return "".join(reversed(final_result))


def min_remove_to_make_valid_v2(s: str) -> str:
    stack: list[int] = []
    result: list[str] = []
    for c in s:
        if c == '(':
            stack.append(len(result))
            result.append(c)
        elif c == ')':
            if stack:
                stack.pop()
                result.append(c)
        else:
            result.append(c)

    for i in stack:
        result[i] = ''

    return ''.join(result)


ic(min_remove_to_make_valid("lee(t(c)o)de)"))
