# 별자리 만들기

import sys
from math import sqrt

input = sys.stdin.readline

n = int(input().strip())
stars = [list(map(float, input().split())) for _ in range(n)]
parent = [i for i in range(n)]

distances = []
for i in range(n - 1):
    for j in range(i + 1, n):
        star1, star2 = stars[i], stars[j]
        distance = sqrt((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2)
        distances.append((i, j, distance))
distances.sort(key=lambda x: x[2])


def union(u, v):
    root_u, root_v = find(u), find(v)
    parent[max(root_u, root_v)] = min(root_u, root_v)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


result = 0
for u, v, d in distances:
    if find(u) != find(v):
        result += d
        union(u, v)
print("%.2f" % result)
