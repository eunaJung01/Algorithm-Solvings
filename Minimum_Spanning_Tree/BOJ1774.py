# 우주신과의 교감

import sys
from math import sqrt

input = sys.stdin.readline


def union(a, b):
    root_a, root_b = find(a), find(b)
    parent[max(root_a, root_b)] = min(root_a, root_b)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


N, M = map(int, input().split())  # N : 우주신들의 개수 / M : 이미 연결된 신들과의 통로의 개수
parent = [i for i in range(N + 1)]

gods = []  # 우주신들이 좌표
for i in range(N):
    x, y = map(int, input().split())
    gods.append((i + 1, x, y))

for _ in range(M):  # 이미 연결된 통로
    god1, god2 = map(int, input().split())
    union(god1, god2)

distances = []
for i in range(N - 1):
    for j in range(i + 1, N):
        god1, god2 = gods[i], gods[j]
        distance = sqrt((god1[1] - god2[1]) ** 2 + (god1[2] - god2[2]) ** 2)
        distances.append((god1[0], god2[0], distance))
distances.sort(key=lambda x: x[2])

result = 0
for a, b, distance in distances:
    if find(a) != find(b):
        result += distance
        union(a, b)

print("%.2f" % result)
