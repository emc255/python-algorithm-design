def sorting_matrix(matrix: list) -> list:
    result = []
    arr = []
    column_size = len(matrix[0])

    for i in range(len(matrix)):
        arr.extend(matrix[i])

    sorted_arr = quicksort(arr)

    temp = []
    for i in range(len(sorted_arr)):
        temp.append(sorted_arr[i])

        if len(temp) == column_size:
            result.append(list(temp))
            temp.clear()

    return result


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + mid + quicksort(right)


def merge_sort(array: list) -> list:
    if len(array) < 1:
        mid = len(array) // 2
        merge_sort(array[:mid])
        merge_sort(array[mid + 1:])

    i = 0
    j = 0
    k = 0
    

print(sorting_matrix([[22, 44, 5, 6], [8, 54, 88, 99], [44, 42, 64, 11]]))

print(quicksort([22, 44, 5, 6]))
