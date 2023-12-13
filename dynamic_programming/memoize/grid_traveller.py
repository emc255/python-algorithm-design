def grid_traveller(row: int, column: int, memoize: dict = None) -> int:
    key = f'{row}->{column}'

    if memoize is None:
        memoize = {}

    if key in memoize:
        return memoize[key]

    if row <= 0 or column <= 0:
        return 0

    if row == 1 and column == 1:
        return 1

    memoize[key] = grid_traveller(row - 1, column, memoize) + grid_traveller(row, column - 1, memoize)
    return memoize[key]


print(grid_traveller(18, 18))
