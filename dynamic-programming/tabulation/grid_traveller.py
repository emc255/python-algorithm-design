def grid_traveller(row, column):
    table = [[0 for _ in range(column + 1)] for _ in range(row + 1)]
    table[1][1] = 1
    for i in range(row + 1):
        for j in range(column + 1):
            if i + 1 <= row:
                table[i + 1][j] += table[i][j]
            if j + 1 <= column:
                table[i][j + 1] += table[i][j]

    return table[row][column]


print(grid_traveller(1, 1))
print(grid_traveller(4, 3))
print(grid_traveller(3, 2))
print(grid_traveller(18, 18))
