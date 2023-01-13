# 약수의 합

import sys

input = sys.stdin.readline

T = int(input().strip())
N = [int(input().strip()) for _ in range(T)]

max_T = 1000000
dp = [0 for _ in range(max_T + 1)]  # f(n) 저장

for n in range(1, 1001):
    for i in range(1, int(max_T / n) + 1):
        if n <= i:
            dp[n * i] += n
        if n < i:
            dp[n * i] += i  # n=i인 경우는 제곱수 -> i 한번만 더함

for i in range(1, max_T + 1):  # g(n) 계산
    dp[i] += dp[i - 1]

result = []
for n in N:
    result.append(dp[n])

for r in result:
    print(r)
