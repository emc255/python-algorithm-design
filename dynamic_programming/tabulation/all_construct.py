def all_construct(s: str, words: list) -> list:
    dp = [[] for _ in range(len(s) + 1)]
    dp[0] = [[]]

    for i in range(len(s)):
        if dp[i]:
            for word in words:
                new_string = s[i:]
                if new_string.startswith(word) and i + len(word) < len(dp):
                    combinations = [combination + [word] for combination in dp[i]]
                    dp[i + len(word)].extend(combinations)

    return dp[len(s)]


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                    ["eee",
                     "eeeee",
                     "eeeee",
                     "eeeeee",
                     "eeeeeee"]))
print(all_construct("", ["aa", "bb"]))
