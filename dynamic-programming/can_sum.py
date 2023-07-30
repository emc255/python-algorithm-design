def can_sum(target_sum: int, numbers: list, memoize: dict = None) -> bool:
    if memoize is None:
        memoize = {}

    if target_sum in memoize:
        return memoize[target_sum]

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for number in numbers:
        remainder = target_sum - number
        memoize[remainder] = can_sum(remainder, numbers, memoize)
        if memoize[remainder]:
            return True

    return False


if __name__ == '__main__':
    print(can_sum(7, [2, 4]))
    print(can_sum(300, [7, 14]))
