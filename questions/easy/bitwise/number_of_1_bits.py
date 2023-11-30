"""
191. Number of 1 Bits

"""
from icecream import ic


def hamming_weight(n: int) -> int:
    result = 0
    while n:
        result += n & 1
        n >>= 1

    return result


def hamming_weight_v2(n: int) -> int:
    result = 0
    while n:
        n &= n - 1
        result += 1

    return result


ic(hamming_weight_v2(0b01001))
