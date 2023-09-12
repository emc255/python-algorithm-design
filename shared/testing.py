# a = "ZY"
# result = 0
# for i in range(len(a)):
#     print((ord(a[i]) - 64))
#     print(25 ** len(a) - i)
#     result += (ord(a[i]) - 64) + (25 ** len(a) - i)
# print(result)


arr = [1, 2, 3, 4, 5, 6]
left = 1
right = 3

for i in range(len(arr)):
    if i == left:
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

print(arr)

n = 110
rn = 0
while n > 0:
    rn = rn | (n & 1)
    rn <<= 1
    n >>= 1

print(rn)

memo = {}
s = "abcabc"
for i in range(len(s)):
    if s[i] in memo:
        memo[s[i]] += 1
    else:
        memo[s[i]] = 1

remove = 0
memo = dict(sorted(memo.items(), key=lambda item: item[1], reverse=True))

d_list = list(memo.values())
print(d_list)

sort = True
temp = 0
while sort and temp < len(d_list):
    sort = False
    for i in range(len(d_list)):
        sort = True
        if i != temp and d_list[i] == d_list[temp]:
            d_list[temp] -= 1
            remove += 1
            if d_list[temp] == 0:
                d_list.pop(temp)

    temp += 1

print(remove)
# for k, v in memo.items():
#     if temp:
#         tk, tv = temp
#         if tv == v:
#             remove += 1
#             tv -= 1
#             if tv == 0:
#                 temp = ()
#             else:
#                 temp = (tk, tv)
#     else:
#         temp = (k, v)
#     print(f'{k} = {v}')
print(remove)
