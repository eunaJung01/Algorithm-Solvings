# 팰린드롬?

import sys

input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().split()))

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]  # 시작점 × 끝점

# 길이가 1
for i in range(N):
    dp[i][i] = 1

# 길이가 2
for i in range(N - 1):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = 1

# 길이가 3 이상
for length in range(2, N):
    for start in range(N - length):
        # 1. 시작점과 끝점의 값이 같고
        # 2. 그 두 점을 제외한 구간이 팰린드롬이어야 한다.
        if numbers[start] == numbers[start + length] and dp[start + 1][start + length - 1] == 1:
            dp[start][start + length] = 1

M = int(input().strip())
for _ in range(M):
    x, y = map(int, input().split())
    print(dp[x - 1][y - 1])
