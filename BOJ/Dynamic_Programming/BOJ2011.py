# 암호코드

import sys

key = list(map(int, list(sys.stdin.readline().strip())))
key_len = len(key)

dp = [0] * (key_len + 1)

if key[0] == 0:
    print(0)
else:
    key = [0] + key
    dp[0] = 1
    dp[1] = 1

    for i in range(2, key_len + 1):
        one = key[i]
        two = key[i - 1] * 10 + key[i]

        if 1 <= one <= 9:
            dp[i] += dp[i - 1]
        if 10 <= two <= 26:
            dp[i] += dp[i - 2]
        dp[i] %= 1000000

    print(dp[key_len])
