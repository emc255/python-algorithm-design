from typing import Optional


def how_sum(target_sum: int, numbers: list) -> list:
    dp: list[Optional[list[int]]] = [None] * (target_sum + 1)
    dp[0] = []

    for i in range(len(dp)):
        for number in numbers:
            if i + number < len(dp) and dp[i] is not None:
                dp[i + number] = dp[i][:] + [number]

    print(dp)

    return dp[target_sum]


# print(how_sum(1000, [99, 77]))
print(how_sum(10, [3, 5, 2]))
print(how_sum(15, [3, 5, 2]))
