"""
729. My Calendar I

You are implementing a program to use as your calendar.
We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty
intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end
that represents a booking on the half-open interval [start, end),
the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to
the calendar successfully without causing a double booking. Otherwise,
return false and do not add the event to the calendar.

Example 1:
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]
Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False,
It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True,
The event can be booked, as the first event takes every time less than 20, but not including 20.

Constraints:
0 <= start < end <= 109
At most 1000 calls will be made to book.

"""
import bisect

from icecream import ic


class MyCalendar:
    def __init__(self):
        self.booking_schedule = []

    def book(self, start: int, end: int) -> bool:
        # Find the insertion point for the new interval (start, end)
        idx = bisect.bisect_right(self.booking_schedule, (start, end))
        ic(idx)
        # Check with the previous interval (if it exists)
        if idx > 0 and self.booking_schedule[idx - 1][1] > start:
            return False  # Overlap with previous booking

        # Check with the next interval (if it exists)
        if idx < len(self.booking_schedule) and self.booking_schedule[idx][0] < end:
            return False  # Overlap with next booking

        # If no overlap, insert the booking at the correct position
        self.booking_schedule.insert(idx, (start, end))
        ic(self.booking_schedule)
        return True


c = MyCalendar()
ic(c.book(15, 25))
ic(c.book(10, 20))
