# 징검다리 건너기 (small)

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
rock = list(map(int, input().split()))
dp = [False for _ in range(N)]
dp[0] = True

for i in range(N):
    for j in range(0, i):
        if not dp[j]:
            continue
        if (i - j) * (1 + abs(rock[i] - rock[j])) <= K:
            dp[i] = True

if dp[N - 1]:
    print("YES")
else:
    print("NO")
