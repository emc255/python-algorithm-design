def all_construct(s: str, words: list) -> list:
    memoize = {}
    return all_construct_helper(s, words, memoize)


def all_construct_helper(s: str, words: list, memoize: dict) -> list:
    if s in memoize:
        return memoize[s]

    if len(s) == 0:
        return [[]]

    result = []
    for word in words:
        if s.startswith(word):
            new_string = s[len(word):]
            combinations = all_construct_helper(new_string, words, memoize)
            result.extend([[word] + combination for combination in combinations])

    memoize[s] = result
    return result


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                    ["eee",
                     "eeeee",
                     "eeeee",
                     "eeeeee",
                     "eeeeeee"]))
print(all_construct("", ["aa", "bb"]))
