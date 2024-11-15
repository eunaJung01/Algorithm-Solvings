def solution(n):
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]
    dp[0][1] = 1
    dp[1][0] = 1

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 2][0] + dp[i - 2][1]
    return (dp[n][0] + dp[n][1]) % 1234567
