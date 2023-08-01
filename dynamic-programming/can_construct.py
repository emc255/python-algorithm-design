def can_construct(target_string: str, string_list: list, memoize: dict = None) -> bool:
    if memoize is None:
        memoize = {}

    if target_string in memoize:
        return memoize[target_string]

    if len(target_string) == 0:
        return True

    for s in string_list:
        if target_string.startswith(s):
            new_target_string = target_string[len(s):]
            if can_construct(new_target_string, string_list, memoize):
                memoize[target_string] = True
                return True

    memoize[target_string] = False
    return False


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                    ["eee",
                     "eeee",
                     "eeeee",
                     "eeeeee",
                     "eeeeeee"]))
