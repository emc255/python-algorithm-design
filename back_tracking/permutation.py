import string


def permutation(s: string, prefix: str = "") -> None:
    if len(s) == 0:
        print(prefix)
        return

    for i in range(len(s)):
        permutation(s[:i] + s[i + 1:], prefix + s[i])


permutation("ABC")
