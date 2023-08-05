def how_sum(target_sum: int, numbers: list) -> list:
    dp = [[] for _ in range(target_sum + 1)]
    dp[0] = [[]]

    for i in range(target_sum):
        for number in numbers:
            index = i + number
            if index < len(dp) and dp[i]:
                new_combination = [combination + [number] for combination in dp[i]]
                dp[index].extend(new_combination)

    return dp[target_sum]


# print(how_sum(1000, [99, 77]))
# print(how_sum(10, [3, 5, 2]))
print(how_sum(6, [3, 4, 6]))
