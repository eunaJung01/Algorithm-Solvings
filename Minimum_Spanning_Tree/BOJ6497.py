# 전력난

import sys

input = sys.stdin.readline


def union(u, v):
    root_u, root_v = find(u), find(v)
    parent[max(root_u, root_v)] = min(root_u, root_v)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


results = []
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = [i for i in range(m)]

    road, total_money = [], 0
    for _ in range(n):
        x, y, z = map(int, input().split())  # x번 집, y번 집, 거리 z 미터
        road.append((x, y, z))
        total_money += z
    road.sort(key=lambda x: x[2])

    min_money = 0
    for u, v, d in road:
        if find(u) != find(v):
            min_money += d
            union(u, v)
    results.append(total_money - min_money)

for r in results:
    print(r)
