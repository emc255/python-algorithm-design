from icecream import ic


def insertion_sort(arr):
    N = len(arr)
    for i in range(1, N):
        j = i
        while j >= 1 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


ic(insertion_sort([9, 2, 5, 7, 6, -1]))
