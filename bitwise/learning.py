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
