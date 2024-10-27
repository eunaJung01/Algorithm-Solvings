# 도영이가 만든 맛있는 음식

import sys
from itertools import combinations

N = int(sys.stdin.readline().strip())
taste = []  # [sour, bitter]
for _ in range(N):
    taste.append(list(map(int, sys.stdin.readline().split())))

combs = []  # 모든 음식 조홥
for i in range(1, N + 1):
    combs.append(list(map(list, combinations(taste, i))))

min_sub = 999999999
for com in combs:
    for co in com:
        sour = co[0][0]
        bitter = co[0][1]
        for c in co[1:]:
            sour *= c[0]
            bitter += c[1]

        sub = abs(sour - bitter)
        min_sub = min(sub, min_sub)

print(min_sub)
