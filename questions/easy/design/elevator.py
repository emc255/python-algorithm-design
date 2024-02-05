from collections import deque

from icecream import ic


class Elevator:
    def __init__(self, floors: int):
        self.min_floor = 1
        self.max_floor = floors
        self.queue = deque()
        self.current_floor = 1
        self.floor_request = -1

    def request_floor(self, floor: int):
        if floor < self.min_floor:
            self.queue.append(self.min_floor)
        elif floor > self.max_floor:
            self.queue.append(self.max_floor)
        else:
            self.queue.append(floor)

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
            return f"open and close / CURRENT FLOOR: {temp} floor"

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
e.request_floor(2)
e.request_floor(8)
for _ in range(20):
    ic(e.get_action())
