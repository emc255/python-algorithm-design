result = [[1], [1, 1]]

for i in range(1, 5):
    t = []
    for j in range(i + 1):
        t.append(i + 1)
    result.append(t)
print(result)
