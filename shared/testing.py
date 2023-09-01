a = "ZY"
result = 0
for i in range(len(a)):
    print((ord(a[i]) - 64))
    print(25 ** len(a) - i)
    result += (ord(a[i]) - 64) + (25 ** len(a) - i)
print(result)
