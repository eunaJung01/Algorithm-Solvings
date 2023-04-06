# 수열

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

temp_sum = sum(temperatures[:K])
result = temp_sum

for i in range(N - K):
    temp_sum += -temperatures[i] + temperatures[i + K]
    result = max(result, temp_sum)
print(result)
