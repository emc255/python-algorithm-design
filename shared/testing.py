from collections import deque

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

class Elevator:
    def __init__(self, floors: int):
        self.max_floor = floors
        self.queue = deque()
        self.current_floor = 1
        self.floor_request = -1

    def request_floor(self, floor: int):
        if self.max_floor > floor:
            self.queue.append(floor)
        else:
            self.queue.append(self.max_floor)

    def get_action(self):
        if len(self.queue) == 0 and self.floor_request == -1:
            return "No op"

        if len(self.queue) > 0 and self.floor_request == -1:
            self.floor_request = self.queue.popleft()

        if self.current_floor in self.queue:
            self.queue = deque([x for x in self.queue if x != self.current_floor])
            temp = self.current_floor
            return f"open and close / CURRENT FLOOR: {temp} floor"

        if self.floor_request == self.current_floor:
            temp = self.current_floor
            self.current_floor, self.floor_request = self.floor_request, -1
            return f"{temp} floor open/close"

        if self.floor_request > self.current_floor:
            self.current_floor += 1
            return f"up 1 floor / CURRENT FLOOR: {self.current_floor} floor"
        else:
            self.current_floor -= 1
            return f"down 1 floor / CURRENT FLOOR: {self.current_floor} floor"


e = Elevator(10)

e.request_floor(3)
e.request_floor(1)
ic(e.get_action())
ic(e.get_action())
ic(e.get_action())
ic(e.get_action())
e.request_floor(2)
e.request_floor(8)
ic(e.get_action())

ic(e.get_action())
ic(e.get_action())

ic(e.get_action())
ic(e.get_action())

ic(e.get_action())
