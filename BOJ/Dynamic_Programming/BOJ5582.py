# 공통 부분 문자열

import sys

line1 = sys.stdin.readline().strip()
n = len(line1)

line2 = sys.stdin.readline().strip()
m = len(line2)

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
result = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if line1[i - 1] == line2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        result = max(result, dp[i][j])

print(result)
