# 줄 세우기

import sys

input = sys.stdin.readline

N = int(input().strip())
line = list(map(int, input().split()))

dp = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for num in line:
    if num > 1:
        if visited[num - 1]:
            dp[num] = dp[num - 1] + 1
        else:
            dp[num] = 1
        visited[num] = True

print(N - max(dp))
