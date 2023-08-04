def four_sum(nums: list[int], target: int) -> list[list[int]]:
    def backtracking(numbers: list, total, combination_found: list):
        if len(combination_found) == 4:
            result.append(combination_found)
            return
        if len(combination_found) > 4:
            return

        # for i in range(len(numbers)):
        #     backtracking(numbers[i:], remainder - numbers[i], combination_found + [nums[i]], )

    result = []
    backtracking(nums, target, [])
    return result


print(four_sum([1, 0, -1, 0, -2, 2], 0))
