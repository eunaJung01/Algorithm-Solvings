# 행복 유치원

import sys

N, K = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))

d = []  # 키 차이
for i in range(N - 1):
    d.append((h[i + 1] - h[i]))
d.sort()

# 가장 큰 수 ~ K-1번째 가장 큰 수 제외, 키 차이들을 전부 더한 것과 같음
result = 0
for i in range(N - K):
    result += d[i]
print(result)
