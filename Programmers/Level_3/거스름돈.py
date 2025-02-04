def solution(n, money):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    for m in money:
        for i in range(m, n + 1):
            dp[i] += dp[i - m]
    return dp[n] % 1_000_000_007
