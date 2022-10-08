# 코스튬 파티

import sys

input = sys.stdin.readline

N, S = map(int, input().split())
cow = [int(input().strip()) for _ in range(N)]
cow.sort()

result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if cow[i] + cow[j] <= S:
            result += 1
print(result)
