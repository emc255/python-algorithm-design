from icecream import ic


def rotate_string(s: str, goal: str) -> bool:
    for i in range(len(s)):
        suffix = s[:i]
        prefix = s[i:]
        if prefix + suffix == goal:
            return True

    return False


ic(rotate_string(s="abcde", goal="cdeab"))
