def count_construct(target_string: str, words: list) -> int:
    dp = [0 for _ in range(len(target_string) + 1)]
    dp[0] = 1
    for i in range(len(target_string)):
        if dp[i] > 0:
            for word in words:
                new_string = target_string[i:]
                if new_string.startswith(word) and i + len(word) < len(dp):
                    dp[i + len(word)] += dp[i]

    return dp[len(target_string)]


print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                      ["eee",
                       "eeeee",
                       "eeeee",
                       "eeeeee",
                       "eeeeeee"]))
