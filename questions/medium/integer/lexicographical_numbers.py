"""
386. Lexicographical Numbers

Given an integer n,
return all the numbers in the range [1, n]
sorted in lexicographical order.

You must write an algorithm that runs
in O(n) time and uses O(1) extra space.

Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:
Input: n = 2
Output: [1,2]

Constraints:
1 <= n <= 5 * 104

"""
from icecream import ic


def lexical_order(n: int) -> list[int]:
    result = []
    current = 1
    for _ in range(n):
        result.append(current)
        if current * 10 <= n:
            current *= 10
        else:
            if current >= n:
                current //= 10
            current += 1
            while current % 10 == 0:
                current //= 10

    return result


def lexical_order_v2(n: int) -> list[int]:
    result = []
    num = 1
    for _ in range(n):
        result.append(num)
        if num * 10 <= n:
            num *= 10
        else:
            while num % 10 == 9 or num + 1 > n:
                num //= 10
            num += 1
    ic(result[1])
    return result


def lexical_order_v3(n: int, k: int) -> int:
    current = 1
    for _ in range(n):

        if current * 10 <= n:
            current *= 10
        else:
            if current >= n:
                current //= 10
            current += 1
            while current % 10 == 0:
                current //= 10
        k -= 1
        if k == 1:
            return current
    return n


ic(lexical_order(33))
ic(lexical_order_v2(222))
ic(lexical_order_v3(12, 1))
