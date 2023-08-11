def all_sum(target_sum: int, numbers: list) -> list:
    def backtracking(target: int, array: list, answers: list, combination: list):
        if target == 0:
            answers.append(list(combination))
            return

        if target < 0:
            return

        for number in array:
            remainder = target - number
            combination.append(number)
            backtracking(remainder, array, result, combination)
            combination.pop()

    result = []
    backtracking(target_sum, numbers, result, [])

    return result


print(all_sum(10, [2, 3, 5]))
