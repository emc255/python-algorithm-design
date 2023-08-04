def fibonacci(number: int, memoize: dict = None) -> int:
    if memoize is None:
        memoize = {}

    if number in memoize:
        return memoize[number]

    if number <= 2:
        return 1

    memoize[number] = fibonacci(number - 1, memoize) + fibonacci(number - 2, memoize)
    return memoize[number]


print(fibonacci(50))
