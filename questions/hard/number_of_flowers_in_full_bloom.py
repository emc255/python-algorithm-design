"""
2251. Number of Flowers in Full Bloom

You are given a 0-indexed 2D integer array flowers,
where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive).
You are also given a 0-indexed integer array people of size n,
where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n,
where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

Example 1:
Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

Example 2:
Input: flowers = [[1,10],[3,3]], poeple = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

Constraints:
1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= people.length <= 5 * 104
1 <= people[i] <= 109

"""
from collections import defaultdict


def full_bloom_flowers(flowers: list, people: list) -> list:
    blooms = {}
    for flower in flowers:
        start = flower[0]
        end = flower[1] + 1
        for i in range(start, end):
            blooms[i] = 1 + blooms.get(i, 0)

    result = []
    for p in people:
        result.append(blooms.get(p, 0))
    return result


def full_bloom_flowers_v2(flowers: list, people: list) -> list:
    blooming = defaultdict(int)  # use line sweep
    for start, end in flowers:
        blooming[start] += 1
        blooming[end + 1] -= 1

    result = {}
    bloom_count = 0
    people_time = sorted(people, reverse=True)  # sort persons desc so we can pop from last index

    for time in sorted(blooming.keys()):  # loop over sorted status updates
        bloom_change = blooming[time]

        while people_time and time > people_time[-1]:  # if current time is greater than
            result[people_time.pop()] = bloom_count  # current person answer is last bloom_cnt

        if not people_time: break

        bloom_count += bloom_change

    return [result[p] if p in result else 0 for p in people]


# print(full_bloom_flowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]))
# print(full_bloom_flowers([[1, 10], [3, 3]], [3, 3, 2]))

print(full_bloom_flowers_v2([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]))
