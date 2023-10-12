from icecream import ic


def generate_parenthesis(n: int) -> list:
    result = []
    stack = []

    def backtracking(open_parenthesis: int, close_parenthesis: int):
        if open_parenthesis == close_parenthesis == n:
            result.append("".join(stack))
            return
        
        if open_parenthesis < n:
            stack.append("(")
            backtracking(open_parenthesis + 1, close_parenthesis)
            stack.pop()

        if close_parenthesis < open_parenthesis:
            stack.append(")")
            backtracking(open_parenthesis, close_parenthesis + 1)
            stack.pop()

    backtracking(0, 0)

    return result


ic(generate_parenthesis(3))
