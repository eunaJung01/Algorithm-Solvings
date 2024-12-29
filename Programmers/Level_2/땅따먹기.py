def solution(land):
    N = len(land)
    M = 4

    dp = [[0 for _ in range(M)] for _ in range(N)]
    dp[0] = land[0]

    for y in range(1, N):
        for x in range(4):
            for i in range(4):
                if i == x:
                    continue
                dp[y][x] = max(dp[y][x], dp[y - 1][i] + land[y][x])
    return max(dp[N - 1])
