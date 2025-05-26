from icecream import ic


def selection_sort(arr):
    N = len(arr)
    for i in range(N):
        min_index = i
        for j in range(i + 1, N):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


ic(selection_sort([9, 2, 5, 7, 6, -1]))
