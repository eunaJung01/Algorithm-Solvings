# 욕심쟁이 판다

import sys

sys.setrecursionlimit(300000)
input = sys.stdin.readline

n = int(input().strip())
bamboos = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def DFS(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and bamboos[y][x] < bamboos[ny][nx]:
            dp[y][x] = max(dp[y][x], DFS(ny, nx) + 1)
    return dp[y][x]


ans = 0
for y in range(n):
    for x in range(n):
        ans = max(ans, DFS(y, x))
print(ans)
