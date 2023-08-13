"""
Bitwise AND (&)
10  = 1010
2   = 0010
ans = 0010
"""
print("Bitwise AND (&)")
a = 10
b = 2
ans = a & b
print(f'a = {bin(a)[2:]}')
print(f'b = {bin(b)[2:]}')
print(f'ans = {bin(ans)[2:]}')
print("===============")

"""
Bitwise OR (|)
11  = 1011
2   = 0010
ans = 1011
"""
print("Bitwise OR (|)")
a = 11
b = 2
ans = a | b
print(f'a = {bin(a)[2:]}')
print(f'b = {bin(b)[2:]}')
print(f'ans = {bin(ans)[2:]}')
print("===============")

"""
Bitwise XOR (^)
11  = 1110
2   = 1010
ans = 0100
"""
print("Bitwise XOR (^)")
a = 14
b = 10
ans = a ^ b
print(f'a = {bin(a)[2:]}')
print(f'b = {bin(b)[2:]}')
print(f'ans = {bin(ans)[2:]}')
print("===============")

"""
Bitwise NOT (~)
10  = 0101
ans = 1010
"""
print("Bitwise NOT (~)")
a = 10
ans = ~a
print(f'a = {bin(a)[2:]}')
print(f'ans = {bin(ans)}')
print("===============")

"""
Bitwise LEFT SHIFT (<<)
bits << (n) add zeroes to the right
14  = 1110 << 1
ans = 111110
"""
print("Bitwise LEFT SHIFT (<<)")
a = 10
ans = a << 5
print(f'a = {bin(a)[2:]}')
print(f'ans = {bin(ans)[2:]}')
print("===============")

"""
Bitwise RIGHT SHIFT (>>)
bits << (n) add zeroes to the left
15  = 1010
ans = 0101
"""
print("Bitwise RIGHT SHIFT (^)")
a = 10
ans = a >> 1
print(f'a = {bin(a)[2:]}')
print(f'ans = {bin(ans)[2:]}')
print("===============")

"""
ODD OR EVEN USING &
15  = 1010
ans = 0101
"""
print("ODD OR EVEN USING &")
a = 10
odd_or_even = "even" if (a & 1) == 0 else "odd"
print(f'a = {bin(a)[2:]}')
print(f'{bin(a)[2:]} is {odd_or_even}')
a = 11
odd_or_even = "even" if (a & 1) == 0 else "odd"
print(f'a = {bin(a)[2:]}')
print(f'{bin(a)[2:]} is {odd_or_even}')
print("===============")

"""
no number appears more than twice
problem solve using XOR (^)
"""
print("FIND NUMBER APPEAR ONCE IN ARRAY")
numbers = [1, 1, 4, 5, 6, 4, 5, 10, 6]
ans = 0
for number in numbers:
    ans ^= number
print(f'ans = {ans}')

"""

"""
print("FIND MAGIC NUMBER nth")
n = 5
base = n
ans = 0
while n != 0:
    last_digit = n & 1
    n >>= 1
    ans = last_digit * base
    base = base * 5

print(f'ans = {ans}')
