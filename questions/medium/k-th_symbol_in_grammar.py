"""
779. K-th Symbol in Grammar

We build a table of n rows (1-indexed).
We start by writing 0 in the 1st row. Now in every subsequent row,
we look at the previous row and replace each occurrence of 0 with 01,
and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Example 1:
Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0

Example 2:
Input: n = 2, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01

Example 3:
Input: n = 2, k = 2
Output: 1
Explanation:
row 1: 0
row 2: 01

Constraints:
1 <= n <= 30
1 <= k <= 2n - 1

"""
from icecream import ic


def kth_grammar(n: int, k: int) -> int:
    value = 0
    l, r = 1, 2 ** (n - 1)

    for _ in range(1, n):
        mid = (l + r) // 2
        if k <= mid:
            r = mid
        else:
            l = mid + 1
            value = 0 if value else 1

    return value


ic(kth_grammar(1, 1))
ic(kth_grammar(2, 2))
ic(kth_grammar(5, 2))
