# 평범한 배낭

import sys

N, K = map(int, sys.stdin.readline().split())  # 물품의 수, 버틸 수 있는 무게

W = []  # 각 물건의 무게
V = []  # 각 물건의 가치
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    W.append(w)
    V.append(v)

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if W[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], V[i - 1] + dp[i - 1][j - W[i - 1]])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])
