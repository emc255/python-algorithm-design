from typing import Union


def how_sum(target_sum: int, numbers: list, memoize: dict = None) -> Union[list, None]:
    if memoize is None:
        memoize = {}

    if target_sum in memoize:
        return memoize[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for number in numbers:
        remainder = target_sum - number
        remainder_result = how_sum(remainder, numbers, memoize)
        if remainder_result is not None:
            remainder_result.append(number)
            memoize[target_sum] = remainder_result
            return remainder_result

    memoize[target_sum] = None
    return None


if __name__ == '__main__':
    print(how_sum(1000, [99, 77]))
