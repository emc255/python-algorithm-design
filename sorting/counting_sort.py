from icecream import ic


def counting_sort(arr):
    maximum = max(arr)
    counts = [0] * (maximum + 1)
    for n in arr:
        counts[n] += 1

    i = 0
    for j in range(len(counts)):
        while counts[j] > 0:
            arr[i] = j
            i += 1
            counts[j] -= 1

    return arr


ic(counting_sort([9, 2, 5, 10, 4, 2, 4, 6]))
