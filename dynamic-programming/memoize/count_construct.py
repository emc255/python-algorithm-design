def count_construct(target_string: str, words: list, memoize: dict = None) -> int:
    result = 0
    if memoize is None:
        memoize = {}

    if target_string in memoize:
        return memoize[target_string]

    if len(target_string) == 0:
        return 1

    for word in words:
        if target_string.startswith(word):
            new_target_string = target_string[len(word):]
            result += count_construct(new_target_string, words, memoize)

    memoize[target_string] = result
    return result


print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                      ["eee",
                       "eeeee",
                       "eeeee",
                       "eeeeee",
                       "eeeeeee"]))
