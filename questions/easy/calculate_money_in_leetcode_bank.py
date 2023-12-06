"""
1716. Calculate Money in Leetcode Bank

Hercy wants to save money for his first car.
He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day.
Every day from Tuesday to Sunday, he will put in $1 more than the day before.
On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money
he will have in the Leetcode bank at the end of the nth day.

Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day,
the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37.
Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day,
the total is
(1 + 2 + 3 + 4 + 5 + 6 + 7)
+ (2 + 3 + 4 + 5 + 6 + 7 + 8)
+ (3 + 4 + 5 + 6 + 7 + 8) = 96.

Constraints:
1 <= n <= 1000
"""
from icecream import ic


def total_money(n: int) -> int:
    day = 1
    week = 0
    result = 0
    for i in range(1, n + 1):
        result += day
        day += 1
        if i % 7 == 0:
            week += 1
            day = 1 + week
    # low = 1
    # high = 7 if n > 7 else n
    # total = (high + low) * high // 2
    # weeks = n // 7
    # remaining_days = n % 7
    # increment_weeks = weeks - 1 if weeks > 1 else 0
    # iw = increment_weeks * 7
    # ic(remaining_days)
    # if remaining_days:
    #     rdl = 1 + weeks
    #     rdh = remaining_days + weeks + 1
    #     remaining_days = (rdh + rdl) * remaining_days // 2
    #     ic(rdl)
    #     ic(rdh)
    # ic((weeks * total) + iw)
    # return (weeks * total) + iw + remaining_days
    return result


def total_money_v2(n: int) -> int:
    low = 1
    high = min(7, n)
    total = (high + low) * high // 2
    weeks = n // 7
    remaining_days = n % 7
    increment_weeks = weeks - 1 if weeks > 1 else 0
    increment_weeks_total = 0
    for i in range(1, increment_weeks + 1):
        increment_weeks_total += 7 * i

    if remaining_days:
        rdl = 1 + weeks
        rdh = remaining_days + weeks
        remaining_days = (rdh + rdl) * remaining_days // 2

    return (weeks * total) + increment_weeks_total + remaining_days


def total_money_v3(n):
    low = 1
    high = min(7, n)
    total = (high + low) * high // 2
    weeks = n // 7
    remaining_days = n % 7

    increment_weeks_total = sum(7 * i for i in range(1, weeks)) if weeks > 1 else 0
    remaining_days_total = 0
    
    if remaining_days:
        remaining_days_total = sum(range(weeks + 1, weeks + remaining_days + 1))

    return (weeks * total) + increment_weeks_total + remaining_days_total


# Test the function
# ic(total_money(20))
# ic(total_money(10))

ic(total_money_v3(20))
