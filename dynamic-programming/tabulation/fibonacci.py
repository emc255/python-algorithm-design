def fibonacci(n: int) -> int:
    table = [0 for _ in range(n + 2)]
    table[1] = 1

    for i in range(n):
        table[i + 1] += table[i]
        table[i + 2] += table[i]

    return table[n]


print(fibonacci(6))
print(fibonacci(100))
print(fibonacci(50))
