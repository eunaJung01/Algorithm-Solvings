# 서강그라운드

import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())  # 지역의 개수, 수색 범위, 길의 개수
t = list(map(int, input().split()))  # 각 구역에 있는 아이템의 수

INF = int(1e9)
roads = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for n in range(1, n + 1):
    roads[n][n] = 0

for _ in range(r):
    a, b, l = map(int, input().split())  # 지역 번호 a, b, 길의 길이 l
    roads[a][b] = l
    roads[b][a] = l

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if roads[a][b] > roads[a][k] + roads[k][b]:
                roads[a][b] = roads[a][k] + roads[k][b]

result = 0
for a in range(1, n + 1):
    items = 0
    for b in range(1, n + 1):
        if roads[a][b] <= m:
            items += t[b - 1]
    result = max(result, items)
print(result)
