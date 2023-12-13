from typing import Optional


def best_sum(target_sum: int, numbers: list) -> list:
    dp: Optional[list[Optional[list]]] = [None for _ in range(target_sum + 1)]
    dp[0] = []

    for i in range(len(dp)):
        for number in numbers:
            if i + number < len(dp) and dp[i] is not None:
                temp = dp[i][:] + [number]
                if dp[i + number] is None or len(temp) < len(dp[i + number]):
                    dp[i + number] = list(temp)

    return dp[target_sum]


print(best_sum(8, [2, 3, 5]))
print(best_sum(100, [1, 2, 3, 25]))
