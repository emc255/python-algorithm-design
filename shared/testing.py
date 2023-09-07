# a = "ZY"
# result = 0
# for i in range(len(a)):
#     print((ord(a[i]) - 64))
#     print(25 ** len(a) - i)
#     result += (ord(a[i]) - 64) + (25 ** len(a) - i)
# print(result)


arr = [1, 2, 3, 4, 5, 6]
left = 1
right = 4

for i in range(len(arr)):
    if i == left:
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

print(arr)
