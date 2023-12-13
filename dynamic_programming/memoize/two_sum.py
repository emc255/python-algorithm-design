def two_sum(nums: list, target: int) -> list:
    remainders = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in remainders:
            return [remainders[difference], i]
        else:
            remainders[nums[i]] = i


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([0, 4, 3, 0], 0))
