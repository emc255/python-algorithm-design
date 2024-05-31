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


filename = "Single Number III"
ic(format_file_name(filename))

func = "singleNumber"
ic(camel_to_snake_case(func))
