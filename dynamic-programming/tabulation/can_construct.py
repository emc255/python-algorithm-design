def can_construct(target_string: str, words: list) -> bool:
    dp = [False for _ in range(len(target_string) + 1)]
    dp[0] = True

    for i in range(len(dp)):
        for word in words:
            new_string = target_string[i:]
            if new_string.startswith(word) and dp[i] and i + len(word) < len(dp):
                dp[i + len(word)] = True

    return dp[len(target_string)]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                    ["eee",
                     "eeee",
                     "eeeee",
                     "eeeeee",
                     "eeeeeee"]))
