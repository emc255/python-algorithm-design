"""
2391. Minimum Amount of Time to Collect Garbage

You are given a 0-indexed array of strings garbage where garbage[i] represents
the assortment of garbage at the ith house.
garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal,
paper and glass garbage respectively.
Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel
where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city,
each responsible for picking up one type of garbage.
Each garbage truck starts at house 0 and must visit each house in order;
however, they do not need to visit every house.

Only one garbage truck may be used at any given moment.
While one truck is driving or picking up garbage,
the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.

Example 1:
Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
Output: 21
Explanation:
The paper garbage truck:
1. Travels from house 0 to house 1
2. Collects the paper garbage at house 1
3. Travels from house 1 to house 2
4. Collects the paper garbage at house 2
Altogether, it takes 8 minutes to pick up all the paper garbage.
The glass garbage truck:
1. Collects the glass garbage at house 0
2. Travels from house 0 to house 1
3. Travels from house 1 to house 2
4. Collects the glass garbage at house 2
5. Travels from house 2 to house 3
6. Collects the glass garbage at house 3
Altogether, it takes 13 minutes to pick up all the glass garbage.
Since there is no metal garbage, we do not need to consider the metal garbage truck.
Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.

Example 2:
Input: garbage = ["MMM","PGM","GP"], travel = [3,10]
Output: 37
Explanation:
The metal garbage truck takes 7 minutes to pick up all the metal garbage.
The paper garbage truck takes 15 minutes to pick up all the paper garbage.
The glass garbage truck takes 15 minutes to pick up all the glass garbage.
It takes a total of 7 + 15 + 15 = 37 minutes to collect all the garbage.

Constraints:
2 <= garbage.length <= 105
garbage[i] consists of only the letters 'M', 'P', and 'G'.
1 <= garbage[i].length <= 10
travel.length == garbage.length - 1
1 <= travel[i] <= 100

"""
from collections import defaultdict

from icecream import ic


def garbage_collection(garbage: list, travel: list) -> int:
    total_time = 0
    trucks = defaultdict(int)
    for i in range(len(garbage)):
        if "M" in garbage[i]:
            trucks["M"] = i
        if "P" in garbage[i]:
            trucks["P"] = i
        if "G" in garbage[i]:
            trucks["G"] = i

    for k, v in trucks.items():
        for index in range(v + 1):
            if index == 0:
                total_time += garbage[index].count(k)
            else:
                total_time += travel[index - 1] + garbage[index].count(k)

    return total_time


def garbage_collection_v2(garbage: list, travel: list) -> int:
    ans = 0

    n = len(garbage)

    m, p, g = False, False, False
    for i in range(n - 1, -1, -1):
        if not g and "G" in garbage[i]:
            g = True
            ans += sum(travel[:i])
        if not m and "M" in garbage[i]:
            m = True
            ans += sum(travel[:i])
        if not p and "P" in garbage[i]:
            p = True
            ans += sum(travel[:i])
        if all([m, p, g]):
            break
    
    return len("".join(garbage)) + ans


ic(garbage_collection(["G", "P", "GP", "GG"], [2, 4, 3]))

ic(garbage_collection_v2(["MMM", "PGM", "GP"], [3, 10]))
