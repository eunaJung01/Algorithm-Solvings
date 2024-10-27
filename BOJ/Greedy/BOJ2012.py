# 등수 매기기

import sys

input = sys.stdin.readline

N = int(input().strip())
score = [int(input().strip()) for _ in range(N)]
score.sort()

result = 0
for i, s in enumerate(score):
    result += abs(s - (i + 1))
print(result)
