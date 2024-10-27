# 치킨 배달

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

home, chicken = [], []  # 집 좌표, 치킨집 좌표

for y in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for x in range(N):
        if lst[x] == 1:
            home.append((y, x))
        elif lst[x] == 2:
            chicken.append((y, x))


# 치킨 거리 계산
def chicken_distance(c):
    d = 0
    for hy, hx in home:
        temp = 99999
        for cy, cx in c:
            temp = min(temp, abs(hy - cy) + abs(hx - cx))
        d += temp
    return d


result = 99999
if len(chicken) == M:
    result = chicken_distance(chicken)
else:
    left_chicken = list(combinations(chicken, M))  # 조합 list
    for l in left_chicken:
        result = min(result, chicken_distance(l))

print(result)
