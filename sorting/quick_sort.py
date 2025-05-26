from icecream import ic


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [n for n in arr if n < pivot]
    mid = [n for n in arr if n == pivot]
    right = [n for n in arr if n > pivot]

    return quick_sort(left) + mid + quick_sort(right)


ic(quick_sort([9, 2, 5, 7, 6, -1]))
