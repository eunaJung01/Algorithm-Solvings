def solution(sticker):
    n = len(sticker)

    if n <= 2:
        return max(sticker)

    dp_0 = [[0 for _ in range(2)] for _ in range(n - 1)]
    dp_0[0][0] = sticker[0]

    dp_1 = [[0 for _ in range(2)] for _ in range(n)]

    return max(get_max(sticker, dp_0, n - 1),
               get_max(sticker, dp_1, n))


def get_max(sticker, dp, length):
    for i in range(1, length):
        dp[i][0] = dp[i - 1][1] + sticker[i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])

    return max(dp[length - 1][0], dp[length - 1][1])
