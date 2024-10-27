# 최소 스패닝 트리

import sys

input = sys.stdin.readline

V, E = map(int, input().split())  # 노드의 개수, 간선의 개수
parent = [i for i in range(V + 1)]

kruskal = []
for i in range(E):
    A, B, C = map(int, input().split())  # 노드 a, 노드 b, 가중치 w
    kruskal.append((A, B, C))
kruskal.sort(key=lambda x: x[2])  # 가중치 기준 오름차순 정렬


def union(a, b):
    parent[max(a, b)] = min(a, b)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])  # 최적화를 위한 Path Compression
    return parent[x]


min_weight = 0
for a, b, w, in kruskal:
    root_a, root_b = find(a), find(b)
    if root_a != root_b:
        min_weight += w
        union(root_a, root_b)

print(min_weight)
