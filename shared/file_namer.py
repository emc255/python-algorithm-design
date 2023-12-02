from icecream import ic


def file_namer(s: str) -> str:
    return s.replace(' ', '_').lower()


filename = "minimumOneBitOperations"
ic(file_namer(filename))


def function_namer(s: str) -> str:
    new_name = []

    for c in s:
        if c.isupper():
            new_name.extend(['_', c.lower()])
        else:
            new_name.append(c)

    return ''.join(new_name)


func = "minimumOneBitOperations"
ic(function_namer(func))
