# 최소 스패닝 트리

import sys

input = sys.stdin.readline

V, E = map(int, input().split())
parent = [i for i in range(V + 1)]

kruskal = []
for i in range(E):
    A, B, C = map(int, input().split())  # C는 가중치
    kruskal.append((A, B, C))
kruskal.sort(key=lambda x: x[2])  # 가중치 기준 오름차순 정렬


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


weight_sum = 0
for a, b, w, in kruskal:
    if find(a) != find(b):
        a, b = find(a), find(b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
        weight_sum += w

print(weight_sum)
