from icecream import ic


def format_file_name(s: str) -> str:
    return s.replace(' ', '_').lower()


def camel_to_snake_case(s: str) -> str:
    new_name = []

    for c in s:
        if c.isupper():
            new_name.extend(['_', c.lower()])
        else:
            new_name.append(c)

    return ''.join(new_name)


filename = "Zero Array Transformation I"
ic(format_file_name(filename))

func = "isZeroArray"
ic(camel_to_snake_case(func))


def isZeroArray(nums: list[int], queries: list[list[int]]) -> bool:
    N = len(nums)
    arr = [0] * (N + 1)
    for l, r in queries:
        arr[l] += 1
        arr[r + 1] -= 1
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    ic(arr)
    for i in range(N):
        if arr[i] < nums[i]:
            return False

    return True


ic(isZeroArray([1, 0, 1], queries=[[0, 2]]))
