from collections import deque
from itertools import groupby

from icecream import ic

tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

map = {}
temp_key = None
test = []
for ticket in tickets:
    if temp_key is None:
        temp_key = tuple(ticket)
    else:
        departure, destination = temp_key
        if ticket[0] < departure or ticket[0] == departure and ticket[1] < destination:
            temp_key = ticket

    map[ticket[0]] = ticket

map.pop(temp_key[0])
test.append(temp_key)
my_queue = deque()
# while map:
#
#     original_departure = temp_key[0]
#     original_destination = temp_key[1]
#     while original_destination in map:
#         my_queue.append(map[original_destination])
#
#     while my_queue:
#         departure, destination = my_queue.pop()
#         if original_departure < departure or original_departure == departure and original_destination < destination:
#             print(my_queue)


print(test)
print(temp_key)

print(map)


def find132pattern(nums: list) -> bool:
    stack = []
    current_minimum = nums[0]
    for n in nums[1:]:
        while stack and n >= stack[-1][0]:
            stack.pop()
        if stack and n > stack[-1][1]:
            return True
        stack.append([n, current_minimum])
        current_minimum = min(current_minimum, n)
    return False


print(find132pattern([1, 0, 1, -4, -3]))
print(find132pattern([3, 5, 0, 3, 4]))


def count_homogenous(s: str) -> int:
    """
     1234567 = 1
        123456 234567 = 2
        12345 23456 34567 = 3
        1234 2345 3456 4567 = 4
        123 234 345 456 567 = 5
        12 23 34 45 56 67 = 6

        12345 = 1
        1234 2345 = 2
        123 234 345 = 3
        12 23 34 45 = 4

        123456 = 1
        12345 23456 = 2
        1234 2345 3456 = 3
        123 234 345 456 = 4
        12 23 34 45 56 = 5

        You can use the formula for the sum of an arithmetic series:
        Sum = (n/2) * (first number + last number)
    """
    result = 0
    for k, group in groupby(s):
        n = len(list(group))
        if n == 1:
            result += n
        else:
            result += int((n / 2) * (1 + n))
    return result % (10 ** 9 + 7)


def count_homogenous_v2(s: str) -> int:
    result = 0
    mod_value = 10 ** 9 + 7
    n = 1  # Initialize n with 1 to account for the last character

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            n += 1
        else:
            result = (result + (n * (n + 1) // 2)) % mod_value
            n = 1

    result = (result + (n * (n + 1) // 2)) % mod_value
    return result


def count_homogenous_v3(self, s: str) -> int:
    ans = 0
    for k, g in groupby(s):
        temp = len(list(g))
        ans = (ans + temp * (temp + 1) // 2) % (10 ** 9 + 7)

    return ans


ic(count_homogenous("abbcccaa"))
ic(count_homogenous("zzzzz"))
