# 나머지 합

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

prefixSum = 0
remainders = [0 for _ in range(M)]

for i in range(N):
    prefixSum += A[i]
    remainders[prefixSum % M] += 1

ans = remainders[0]
for i in range(M):
    if remainders[i] >= 2:
        ans += (remainders[i] * (remainders[i] - 1)) // 2
print(ans)
