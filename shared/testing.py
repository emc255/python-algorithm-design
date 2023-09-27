from collections import deque

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
