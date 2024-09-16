"""
539. Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format,
return the minimum minutes difference between any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:
2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".

"""
from icecream import ic


def find_minimum_difference(time_points: list[str]) -> int:
    # Helper function to convert time to minutes since midnight
    def time_to_minutes(time: str) -> int:
        hours, minutes = map(int, time.split(":"))
        return hours * 60 + minutes

    # Convert all time points to minutes
    minutes_list = [time_to_minutes(time) for time in time_points]
    # Sort the list of minutes
    minutes_list.sort()

    # Initialize result with a large number
    result = float('inf')

    # Calculate the difference between consecutive times
    for i in range(1, len(minutes_list)):
        result = min(result, minutes_list[i] - minutes_list[i - 1])

    # Also check the difference between the first and last times (circular wrap)
    result = min(result, 1440 + minutes_list[0] - minutes_list[-1])

    return result


ic(find_minimum_difference(["00:00", "23:59", "00:00"]))
ic(find_minimum_difference(["00:00", "23:59"]))
