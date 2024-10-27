import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

if n == m == 1:
    print(arr[0][0])
    exit()

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    if arr[i][0] == 1:
        dp[i][0] = 1
for j in range(m):
    if arr[0][j] == 1:
        dp[0][j] = 1

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

result = 0
for row in dp:
    result = max(result, max(row))
print(result ** 2)
