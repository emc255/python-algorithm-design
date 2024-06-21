"""
Grumpy Bookstore Owner

There is a bookstore owner that has a store open for n minutes.
Every minute, some number of customers enter the store.
You are given an integer array customers of length n where customers[i] is
the number of the customer that enters the store at the start of the ith minute
and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.
You are given a binary array grumpy where grumpy[i] is 1 if
the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of
that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves
not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Example 2:
Input: customers = [1], grumpy = [0], minutes = 1
Output: 1

Constraints:
n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.

"""

from icecream import ic


def max_satisfied(customers: list[int], grumpy: list[int], minutes: int) -> int:
    # Calculate the number of satisfied customers when the owner is not grumpy
    always_satisfied = sum(customers[i] for i in range(len(customers)) if not grumpy[i])

    # Calculate the initial window of "grumpy" customers that can be made satisfied
    max_satisfied_extra = 0
    current_satisfied_extra = 0
    for i in range(minutes):
        if grumpy[i]:
            current_satisfied_extra += customers[i]
    max_satisfied_extra = current_satisfied_extra

    # Slide the window across the grumpy list
    for i in range(minutes, len(customers)):
        if grumpy[i]:
            current_satisfied_extra += customers[i]
        if grumpy[i - minutes]:
            current_satisfied_extra -= customers[i - minutes]
        max_satisfied_extra = max(max_satisfied_extra, current_satisfied_extra)

    # Total satisfied customers = always satisfied + the best window we found
    return always_satisfied + max_satisfied_extra


"""
1 0 1 2 1 1 7 5
0 1 0 1 0 1 0 1
"""
ic(max_satisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
