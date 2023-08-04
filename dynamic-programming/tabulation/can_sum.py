def can_sum(target_sum: int, numbers: list) -> bool:
    dp = [False for _ in range(target_sum + 1)]
    dp[0] = True
    for i in range(target_sum):
        for number in numbers:
            if i + number < len(dp) and dp[i]:
                dp[i + number] = True

    return dp[target_sum]


print(can_sum(7, [3, 4]))
print(can_sum(300, [7, 14]))
