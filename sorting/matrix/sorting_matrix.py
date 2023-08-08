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
    def merge():
        result = []
        left_index = 0
        right_index = 0
        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] < right_array[right_index]:
                result.append(left_array[left_index])
                left_index += 1
            else:
                result.append(right_array[right_index])
                right_index += 1

        result.extend(left_array[left_index:])
        result.extend(right_array[right_index:])

        return result

    if len(array) <= 1:
        return array

    mid_index = 0 + len(array) // 2
    left_array = merge_sort(array[:mid_index])
    right_array = merge_sort(array[mid_index:])

    return merge()


print(sorting_matrix([[22, 44, 5, 6], [8, 54, 99], [44, 42, 64, 11]]))

print(quicksort([22, 44, 5, 6]))
print(merge_sort([44, 42, 64, 11]))
