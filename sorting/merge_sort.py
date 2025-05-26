from icecream import ic


def merge_sort(arr):
    def merge(left_arr, right_arr):
        result = []
        i = 0
        j = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                result.append(left_arr[i])
                i += 1
            else:
                result.append(right_arr[j])
                j += 1

        result.extend(left_arr[i:] + right_arr[j:])
        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


ic(merge_sort([9, 2, 5, 7, 6, -1]))
