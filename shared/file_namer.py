from icecream import ic


def file_namer(s: str) -> str:
    return s.replace(' ', '_').lower()


filename = "Minimum Time Visiting All Points"
ic(file_namer(filename))


def function_namer(s: str) -> str:
    new_name = []

    for c in s:
        if c.isupper():
            new_name.extend(['_', c.lower()])
        else:
            new_name.append(c)

    return ''.join(new_name)


func = "minTimeToVisitAllPoints"
ic(function_namer(func))
