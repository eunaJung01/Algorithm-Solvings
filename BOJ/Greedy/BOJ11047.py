# 동전 0

import sys

N, K = map(int, sys.stdin.readline().split())
lst = [int(sys.stdin.readline().strip()) for _ in range(N)]
lst.sort(reverse=True)

result = 0

for m in lst:
    if K == 0:
        break
    result += K // m
    K %= m

print(result)
