# 카드 구매하기

import sys

N = int(sys.stdin.readline().strip())

price = [0]
line = list(map(int, sys.stdin.readline().split()))
for l in line:
    price.append(l)

dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + price[j])

print(dp[N])
