"""
Daily Temperatures

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days
you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible,
keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

"""
from icecream import ic


def daily_temperatures(temperatures: list[int]) -> list[int]:
    # TLE
    result = [0 for _ in range(len(temperatures))]
    for i in range(1, len(temperatures)):
        j = i
        counter = 0
        found = False
        while j < len(temperatures):
            if temperatures[i - 1] < temperatures[j]:
                counter += 1
                found = True
                break
            counter += 1
            j += 1
        result[i - 1] = counter if found else 0
    return result


def daily_temperatures_v2(temperatures: list[int]) -> list[int]:
    result = [0 for _ in range(len(temperatures))]
    stack = []
    for index, temperature in enumerate(temperatures):
        while stack and stack[-1][0] < temperature:
            t, i = stack.pop()
            result[i] = index - i
        stack.append((temperature, index))
    return result


ic(daily_temperatures_v2([73, 74, 75, 71, 69, 72, 76, 73]))
