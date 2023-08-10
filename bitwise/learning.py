dividend = 100
divisor = 6
multiple = 1

result = 0

while dividend >= divisor:
    temp_divisor = divisor
    multiple = 1

    while dividend >= (temp_divisor << 1):
        temp_divisor <<= 1
        multiple <<= 1

    dividend -= temp_divisor
    result += multiple

x = 121
ans = 0
while x > 0:
    r = x % 10
    ans = (ans * 10) + r
    x //= 10
print(ans)
