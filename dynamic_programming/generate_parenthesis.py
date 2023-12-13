def generate_parentheses(n):
    if n == 0:
        return []

    # Initialize the DP array with the base case
    dp = [[""]]

    for i in range(1, n + 1):
        parentheses = []
        for j in range(i):
            for inner in dp[j]:
                for outer in dp[i - j - 1]:
                    parentheses.append(f"({inner}){outer}")
        dp.append(parentheses)
    print(dp)
    return dp[n]


# Test the function
n = 3
result = generate_parentheses(n)
print(result)
