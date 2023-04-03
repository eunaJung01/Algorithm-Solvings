# 가장 긴 바이토닉 부분 수열

import sys

input = sys.stdin.readline

N = int(input().strip())
line = list(map(int, input().split()))


def longest_increasing_seq(l):
    dp = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if l[j] < l[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


dp_asc = longest_increasing_seq(line)
dp_desc = longest_increasing_seq(line[::-1])

result = [0 for _ in range(N)]
for i in range(N):
    result[i] = dp_asc[i] + dp_desc[N - i - 1] - 1
print(max(result))
