# 지능형 기차 2

import sys

input = sys.stdin.readline

train = [list(map(int, input().split())) for _ in range(10)]
result, n = 0, 0

for minus, plus in train:
    n -= minus
    result = max(result, n)
    n += plus
    result = max(result, n)
print(result)
