def how_sum(target_sum: int, numbers: list, memoize: dict = None, test: list = None) -> list:
    if memoize is None:
        memoize = {}

    if test is None:
        test = [[]]

    if target_sum in memoize:
        return memoize[target_sum]

    if target_sum == 0:
        return test

    if target_sum < 0:
        return None

    all_lists = []
    for number in numbers:
        remainder = target_sum - number
        remainder_result = how_sum(remainder, numbers, memoize)

        if remainder_result is not None:
            for lst in remainder_result:
                new_list = lst + [number]
                all_lists.append(new_list)

    memoize[target_sum] = all_lists

    return all_lists


if __name__ == '__main__':
    print(how_sum(10, [5, 2, 10]))
