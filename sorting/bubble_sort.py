from icecream import ic


def bubble_sort(arr):
    N = len(arr)
    is_sorted = True
    while is_sorted:
        is_sorted = False
        for i in range(1, N):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                is_sorted = True
    return arr


ic(bubble_sort([9, 2, 5, 7, 6, -1]))
