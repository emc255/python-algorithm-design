# a = "ZY"
# result = 0
# for i in range(len(a)):
#     print((ord(a[i]) - 64))
#     print(25 ** len(a) - i)
#     result += (ord(a[i]) - 64) + (25 ** len(a) - i)
# print(result)


def grid(m: int, n: int):
    def dp(row, column):
        if (row, column) in memoize:
            return memoize[(row, column)]

        if row == 1 and column == 1:
            return 1
        if row <= 0 or column <= 0:
            return 0

        memoize[(row, column)] = dp(row - 1, column) + dp(row, column - 1)
        return memoize[(row, column)]

    memoize = {}
    return dp(m, n)


print(grid(3, 2))
print(grid(1, 1))
